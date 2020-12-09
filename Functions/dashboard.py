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

                   """, conn, params={name})

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

    sold_sku_percentage = str(round((sold_sku_list[0] / total_sku_list[0]) * 100)) + '%'
    # print(sold_sku_percentage)

    yesterdaySalesQty = pd.read_excel(dir.get_directory() + '/Data/html_data_Sales_and_Stock.xlsx')
    # y = yesterdaySalesQty['YesterdaySalesQty'] != 0

    y2 = yesterdaySalesQty['BRAND'].unique()

    brand_coverage = str(round((len(y2) / total_brand_list[0]) * 100)) + '%'

    # print(No_sold_sku_percentage)

    No_stock_sku_percentage = str(round((no_stock_sku_list[0] / total_sku_list[0]) * 100)) + '%'
    # print(No_stock_sku_percentage)


#----------------------------------------------------------------------------------------------------
    #---------------------------------kpi 6-10 ------------------------------------------
    try:

        gpm_target = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                                    Declare @DaysInMonth NVARCHAR(MAX);
                                    Declare @DaysInMonthtilltoday NVARCHAR(MAX);
                                    SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                                    SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
                                    SET @DaysInMonthtilltoday = right(convert(varchar(8), GETDATE(),112),2)
    select CP01 as ExecutiveName, isnull(sum(QTY),0) as TargetQty,isnull(sum(VALUE)/@DaysInMonth,0) as Targetvalue
                                            from PRINFOSKF 
                                            left join ARCSECONDARY.dbo.RfieldForceProductTRG
                                            on RfieldForceProductTRG.ITEMNO = PRINFOSKF.ITEMNO
                                            where YEARMONTH = CONVERT(varchar(6), dateAdd(month,0,getdate()), 
                                            112) and GPMNAME like ?
                                            group by CP01
                                            order by CP01 asc""", conn, params={name})

        GPM_target_list = gpm_target['Targetvalue'].to_list()
        # print(GPM_target_list)
        GPM_TARGET_SUM=sum(GPM_target_list)
        # print(GPM_TARGET_SUM)

        Target_value_in_crore = str(round((GPM_TARGET_SUM/10000000),1))+' Cr'
        # print(Target_value_in_crore)
    except:
        Target_value_in_crore = str(0)+" Cr"

    gpm_sales_inv_line = pd.read_sql_query("""select CP01 as ExecutiveName,b.[Executive ShortName] as shortname,
                            isnull(sum(EXTINVMISC),0) as SalesValue,count(distinct INVNUMBER)
                            as num_of_inv,count(INVNUMBER) as num_of_inv_line from OESalesDetails
                            left join PRINFOSKF
                            on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
                            left join
                            (select * from GPMExecutive_ShortName) as b
                            on b.[ExecutiveName]=PRINFOSKF.cp01
                            where left(TRANSDATE,8)=convert(varchar(10),getdate()-1, 112)
                            and PRINFOSKF.GPMNAME like ?
                            group by CP01,b.[Executive ShortName]
                            order by CP01 asc""", conn, params={name})

    GPM_sales_list = gpm_sales_inv_line['SalesValue'].to_list()
    gpm_invoice_list = gpm_sales_inv_line['num_of_inv'].to_list()
    gpm_invoice_line_list = gpm_sales_inv_line['num_of_inv_line'].to_list()
    # print(GPM_sales_list)
    GPM_SALES_SUM = sum(GPM_sales_list)
    gpm_invoice_sum = sum(gpm_invoice_list)
    gpm_invoice_line_sum = sum(gpm_invoice_line_list)
    # print(GPM_SALES_SUM)

    Sales_value_in_crore = str(round((GPM_SALES_SUM / 10000000), 1)) + ' Cr'
    print(Sales_value_in_crore)
    try:
        achievement_target_sales = str(round(((GPM_SALES_SUM/GPM_TARGET_SUM)*100),1)) + ' %'
        print(achievement_target_sales)
    except:
        achievement_target_sales = str(0)+' %'
    brand_no_of_invoice = str(int(gpm_invoice_sum/1000))+' K'
    print(brand_no_of_invoice)
    average_no_of_invoice_line = str(round(gpm_invoice_line_sum/gpm_invoice_sum,2))
    print(average_no_of_invoice_line)

    image = Image.open(dir.get_directory() + "/Images/dash_kpi10.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(dir.get_directory() + '/Images/FrancoisOne-Regular.ttf', 30)
    draw.text((80, 83), str(total_brand_list[0]), font=font, fill=(39, 98, 236))
    draw.text((225, 83), str(len(y2)) + ' (' + brand_coverage + ')', font=font, fill=(39, 95, 236))
    draw.text((460, 83), str(total_sku_list[0]), font=font, fill=(39, 98, 236))

    draw.text((610, 83), str(sold_sku_list[0]) + ' (' + sold_sku_percentage + ')', font=font, fill=(39, 98, 236))
    draw.text((805, 83), str(no_stock_sku_list[0]) + ' (' + No_stock_sku_percentage + ')', font=font, fill=(39, 98,
                                                                                                            236))

    draw.text((60, 177),Target_value_in_crore , font=font, fill=(39, 98, 236))
    draw.text((250, 177),Sales_value_in_crore , font=font, fill=(39, 98, 236))
    draw.text((435, 177),achievement_target_sales , font=font, fill=(39, 98, 236))
    draw.text((640, 177), brand_no_of_invoice, font=font, fill=(39, 98, 236))
    draw.text((835, 177), average_no_of_invoice_line, font=font, fill=(39, 98, 236))
    # image.show()
    image.save('./Images/dashboard.png')

    print('3. Dash generated\n')
