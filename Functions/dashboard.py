from PIL import Image, ImageFont, ImageDraw
import pandas as pd
from calendar import monthrange
from datetime import date, datetime
import path as dir
import Functions.db_connection as dbc

def dash_kpi_generator(name):
    total_sku = pd.read_sql_query("""select gpmname,count(distinct BRAND) as 'total brand',count(itemno) as 'total_SKU' from PRINFOSKF
                   where status=1
                   and gpmname like ?
                   group by gpmname 
                   """, dbc.connection, params={name})

    total_sku_list = total_sku['total_SKU'].to_list()
    total_brand_list = total_sku['total brand'].tolist()

    sold_sku = pd.read_sql_query(""" select count(distinct item) as 'Sold_SKU' from OESalesDetails
                   where item in(select itemno from PRINFOSKF
                   where status=1
                   and gpmname like ? )
                   and transtype = 1
                  and left(transdate,6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

                   """, dbc.connection, params={name})

    sold_sku_list = sold_sku['Sold_SKU'].to_list()
    # no_sales_sku = total_sku_list[0] - sold_sku_list[0]

    no_stock_sku = pd.read_sql_query("""select count(a.itemno) 'no stock item' from
                       (select itemno from PRINFOSKF
                       where status=1
                       and gpmname like ? ) as a
                       left join
                       (select itemno,isnull(sum(QTYONHAND),0) as stock from ICStockStatusCurrentLOT
                       group by itemno) as b
                       on a.itemno = b.itemno
                       where stock = 0 """, dbc.connection, params={name})

    no_stock_sku_list = no_stock_sku['no stock item'].to_list()

    sold_sku_percentage = str(round((sold_sku_list[0] / total_sku_list[0]) * 100)) + '%'
    yesterdaySalesQty = pd.read_excel(dir.get_directory() + '/Data/html_data_Sales_and_Stock.xlsx')
    y2 = yesterdaySalesQty['BRAND'].unique()
    brand_coverage = str(round((len(y2) / total_brand_list[0]) * 100)) + '%'
    No_stock_sku_percentage = str(round((no_stock_sku_list[0] / total_sku_list[0]) * 100)) + '%'

    # ----------------------------------------------------------------------------------------------------
    gpm_target = pd.read_sql_query(""" 
                Declare @CurrentMonth NVARCHAR(MAX);
                Declare @DaysInMonth NVARCHAR(MAX);
                Declare @DaysInMonthtilltoday NVARCHAR(MAX);
                SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                SET @DaysInMonth =  DAY(EOMONTH(GETDATE()))
                SET @DaysInMonthtilltoday =  right(convert(varchar(8), GETDATE()-1,112),2)
                select CP01 as ExecutiveName, isnull(sum(QTY),0) as TargetQty,isnull(sum(VALUE)/@DaysInMonth,0) as Targetvalue
                    from PRINFOSKF 
                    left join ARCSECONDARY.dbo.RfieldForceProductTRG
                    on RfieldForceProductTRG.ITEMNO = PRINFOSKF.ITEMNO
                    where YEARMONTH = CONVERT(varchar(6), dateAdd(month,0,getdate()), 
                    112) and GPMNAME like ?
                    group by CP01
                    order by CP01 asc
                    """, dbc.connection, params={name})

    GPM_target_list = gpm_target['Targetvalue'].to_list()
    GPM_TARGET_SUM = int(sum(GPM_target_list))

    # # -------- Targets -----------------------------------------------------------
    if len(str(GPM_TARGET_SUM)) >= 8:
        Target_value_in_crore = str(round(GPM_TARGET_SUM / 10000000, 1)) + ' Cr'
    else:
        Target_value_in_crore = str(round(GPM_TARGET_SUM / 1000000, 1)) + ' M'


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
                                order by CP01 asc""", dbc.connection, params={name})

    GPM_sales_list = gpm_sales_inv_line['SalesValue'].to_list()
    gpm_invoice_list = gpm_sales_inv_line['num_of_inv'].to_list()
    gpm_invoice_line_list = gpm_sales_inv_line['num_of_inv_line'].to_list()
    GPM_SALES_SUM = sum(GPM_sales_list)
    gpm_invoice_sum = sum(gpm_invoice_list)
    gpm_invoice_line_sum = sum(gpm_invoice_line_list)

    # # ------------ Sales Value ----------------------------------------------
    if len(str(int(GPM_SALES_SUM))) >= 8:
        Sales_value_in_crore = str(round(GPM_SALES_SUM / 10000000, 1)) + ' Cr'
    else:
        Sales_value_in_crore = str(round(GPM_SALES_SUM / 1000000, 1)) + ' M'

    # # --------------- Sales Achievement --------------------------------------
    try:
        achievement_target_sales = str(round(((GPM_SALES_SUM / GPM_TARGET_SUM) * 100), 1)) + ' %'
    except:
        achievement_target_sales = str(0) + ' %'

    # # Brand Number of Invoice -----------------------------------------------
    if len(str(gpm_invoice_sum)) >=4:
        brand_no_of_invoice = str(round(gpm_invoice_sum / 1000)) + ' K'
    else:
        brand_no_of_invoice = str(gpm_invoice_sum)

    # # ------------- Average Number of Invoice Per line ----------------------
    if gpm_invoice_sum <= 0:
        average_no_of_invoice_line = 0
    else:
        average_no_of_invoice_line = str(round(gpm_invoice_line_sum / gpm_invoice_sum, 2))

    # # ------ Point all data in image -------------------------------------
    image = Image.open(dir.get_directory() + "/Images/dash_kpi10.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(dir.get_directory() + '/Images/FrancoisOne-Regular.ttf', 30)
    draw.text((80, 83), str(total_brand_list[0]), font=font, fill=(39, 98, 236))
    draw.text((225, 83), str(len(y2)) + ' (' + brand_coverage + ')', font=font, fill=(39, 95, 236))
    draw.text((460, 83), str(total_sku_list[0]), font=font, fill=(39, 98, 236))

    draw.text((610, 83), str(sold_sku_list[0]) + ' (' + sold_sku_percentage + ')', font=font, fill=(39, 98, 236))
    draw.text((805, 83), str(no_stock_sku_list[0]) + ' (' + No_stock_sku_percentage + ')', font=font, fill=(39, 98,
                                                                                                     236))

    # # --------- Yesterday Values data points -------------------------------
    draw.text((60, 177), Target_value_in_crore, font=font, fill=(39, 98, 236))
    draw.text((250, 177), Sales_value_in_crore, font=font, fill=(39, 98, 236))
    draw.text((435, 177), achievement_target_sales, font=font, fill=(39, 98, 236))
    draw.text((640, 177), brand_no_of_invoice, font=font, fill=(39, 98, 236))
    draw.text((835, 177), str(average_no_of_invoice_line), font=font, fill=(39, 98, 236))
    # image.show()
    image.save('./Images/dashboard.png')

    print('3. Dash generated\n')
