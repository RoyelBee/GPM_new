
from PIL import Image, ImageFont, ImageDraw
import pyodbc
import pandas as pd
from calendar import monthrange
from datetime import date, datetime
import sys
import path as dir

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=137.116.139.217;'
                      'DATABASE=ARCHIVESKF;'
                      'UID=sa;'
                      'PWD=erp@123;')

def dash_kpi_generator(name):
    total_sku = pd.read_sql_query("""select gpmname,count(distinct BRAND) as 'total brand',count(itemno) as 'total_SKU' from PRINFOSKF
               where status=1
               and gpmname like ?
               group by gpmname 
               """, conn, params={name})

    total_sku_list = total_sku['total_SKU'].to_list()
    total_brand_list = total_sku['total brand'].tolist()

    sold_sku = pd.read_sql_query("""select count(distinct item) as 'Sold_SKU' from OESalesDetails
               where item in(select itemno from PRINFOSKF
               where status=1
               and gpmname like ? )
               and transtype = 1
               and left(transdate,6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)
               
               """ , conn, params={name})

    sold_sku_list = sold_sku['Sold_SKU'].to_list()
    no_sales_sku = total_sku_list[0] - sold_sku_list[0]
    no_stock_sku = pd.read_sql_query("""select count(a.itemno) 'no stock item' from
                   (select itemno from PRINFOSKF
                   where status=1
                   and gpmname like ? ) as a
                   left join
                   (select itemno,isnull(sum(QTYONHAND),0) as stock from ICStockStatusCurrentLOT
                   group by itemno) as b
                   on a.itemno = b.itemno
                   where stock = 0 """, conn, params={name})

    no_stock_sku_list = no_stock_sku['no stock item'].to_list()
    read_file_for_all_data = pd.read_excel('./Data/gpm_data.xlsx')
    total_target = read_file_for_all_data['MTD Sales Target'].to_list()
    total_sales = read_file_for_all_data['Actual Sales MTD'].to_list()

    if sum(total_target) == 0:
        achivemet = 0
    else:
        achivemet = (sum(total_sales) / sum(total_target)) * 100

    today = str(date.today())
    datee = datetime.strptime(today, "%Y-%m-%d")
    date_val = int(datee.day)
    num_days = monthrange(datee.year, datee.month)[1]
    trend = (sum(total_sales) / date_val) * num_days

    trend_achivement = (sum(total_sales) / trend) * 100

    # def currency_converter(num):
    #     num_size = len(str(num))
    #     if num_size >= 4:
    #         number = str(int(num / 1000)) + 'K'
    #     else:
    #         number = num
    #     return number

    image = Image.open(dir.get_directory() + "/images/dash_kpi.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(dir.get_directory() + '/Images/FrancoisOne-Regular.ttf', 30)
    draw.text((80, 80), str(total_brand_list[0]), font=font, fill=(39, 98, 236))
    draw.text((270, 80), str(total_sku_list[0]), font=font, fill=(39, 98, 236))
    draw.text((460, 80), str(sold_sku_list[0]), font=font, fill=(39, 98, 236))
    draw.text((650, 80), str(no_sales_sku), font=font, fill=(39, 98, 236))
    draw.text((840, 80), str(no_stock_sku_list[0]), font=font, fill=(39, 98, 236))

    draw.text((70, 220), str(int(sum(total_target) / 1000)) + 'K', font=font, fill=(255, 255, 255))
    draw.text((260, 220), str(int(sum(total_sales) / 1000)) + 'K', font=font, fill=(255, 255, 255))
    draw.text((435, 220), str(round(achivemet, 1)) + '%', font=font, fill=(255, 255, 255))
    draw.text((625, 220), str(int(trend / 1000)) + 'K', font=font, fill=(255, 255, 255))
    draw.text((830, 220), str(round(trend_achivement, 1)) + '%', font=font, fill=(255, 255, 255))
    # image.show()
    image.save('./Images/dashboard.png')
    print('Dash generated')



