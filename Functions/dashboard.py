from PIL import Image, ImageFont, ImageDraw
import pyodbc
import pandas as pd
from calendar import monthrange
from datetime import date, datetime
import sys
import path as dir
from datetime import datetime
import calendar

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=137.116.139.217;'
                      'DATABASE=ARCHIVESKF;'
                      'UID=sa;'
                      'PWD=erp@123;')


def dash_kpi_generator(name):
    total_sku = pd.read_sql_query(""" select gpmname,count(distinct BRAND) as 'total brand',count(itemno) as 'total_SKU' from PRINFOSKF
                    where status=1 and brand in (select distinct brand from GPMBRAND where Name like ?)
                    and gpmname like ?
                    group by gpmname  
                   """, conn, params=(name, name))

    total_sku_list = total_sku['total_SKU'].to_list()
    total_brand_list = total_sku['total brand'].tolist()
    # print('one')

    sold_sku = pd.read_sql_query(""" select count(distinct item) as 'Sold_SKU' from OESalesDetails
                where item in(select itemno from PRINFOSKF
                where status=1 and brand in (select distinct brand from GPMBRAND where Name like ?)
                and gpmname like ?)
                and transtype = 1
                and left(transdate,6)=CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

                                   """, conn, params=(name, name))

    sold_sku_list = sold_sku['Sold_SKU'].to_list()
    # no_sales_sku = total_sku_list[0] - sold_sku_list[0]

    no_stock_sku = pd.read_sql_query("""select count(a.itemno) 'no stock item' from
            (select itemno from PRINFOSKF
            where status=1 and brand in (select distinct brand from GPMBRAND where Name like ?)
            and gpmname like ? ) as a
            left join
            (select itemno,isnull(sum(QTYONHAND),0) as stock from ICStockStatusCurrentLOT
            group by itemno) as b
            on a.itemno = b.itemno
            where stock = 0 """, conn, params=(name, name))

    no_stock_sku_list = no_stock_sku['no stock item'].to_list()
    read_file_for_all_data = pd.read_excel('./Data/gpm_data.xlsx')
    total_target = read_file_for_all_data['MTD Sales Target'].to_list()
    total_sales = read_file_for_all_data['Actual Sales MTD'].to_list()
    # print('three')

    # if sum(total_target) == 0:
    #     achivemet = 0
    # else:
    #     achivemet = (sum(total_sales) / sum(total_target)) * 100

    from datetime import datetime
    today = str(date.today())
    datee = datetime.strptime(today, "%Y-%m-%d")
    date_val = int(datee.day)
    num_days = monthrange(datee.year, datee.month)[1]
    trend = (sum(total_sales) / date_val) * num_days

    # if trend <= 0:
    #     trend_achivement = 0
    # else:
    #     trend_achivement = (sum(total_sales) / trend) * 100

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

    # ----------------------------------------------------------------------------------------------------
    # ---------------------------------kpi 6-10 ------------------------------------------

    gpm_target = pd.read_sql_query(""" Declare @CurrentMonth NVARCHAR(MAX);
                Declare @DaysInMonth NVARCHAR(MAX);
                Declare @DaysInMonthtilltoday NVARCHAR(MAX);
                SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
                SET @DaysInMonthtilltoday = right(convert(varchar(8), GETDATE(),112),2)
                select CP01 as ExecutiveName, isnull(sum(TRGQTY),0) as TargetQty,isnull(sum(TRGVAL)/@DaysInMonth,0) as Targetvalue
                from PRINFOSKF 
                left join ARCSECONDARY.dbo.PRODUCT_WISE_TRG
                on PRODUCT_WISE_TRG.ITEM = PRINFOSKF.ITEMNO
                where YRM = CONVERT(varchar(6), dateAdd(month,0,getdate()), 
                112) and GPMNAME like ?
                and PRINFOSKF.brand in (select distinct brand from GPMBRAND where Name like ?)
                group by CP01
                order by CP01 asc 
                """, conn, params=(name, name))

    GPM_target_list = gpm_target['Targetvalue'].to_list()
    # print(GPM_target_list)
    GPM_TARGET_SUM = sum(GPM_target_list)
    # print('four')

    if len(str(int(GPM_TARGET_SUM))) >= 8:
        Target_value_in_crore = str("{:.2f}".format((GPM_TARGET_SUM / 10000000), 2)) + ' Cr'
    else:
        Target_value_in_crore = str("{:.2f}".format((GPM_TARGET_SUM / 1000000), 2)) + ' M'

    # print('target = ', Target_value_in_crore)

    gpm_sales_inv_line = pd.read_sql_query(""" 
                select GPMNAME,GPMID,EXID,CP01,isnull(sum(EXTINVMISC), 0) as SalesValue,
                isnull(count(distinct INVNUMBER), 0) as  num_of_inv,
                isnull(sum(LINECOUNT), 0) as num_of_inv_line from (
                select item,INVNUMBER,sum(EXTINVMISC) as EXTINVMISC,sum(QTYSHIPPED) as QTYSHIPPED,count(item) as LINECOUNT from OESalesDetails
                where TRANSDATe= convert(varchar(10),getdate()-1, 112) and TRANSTYPE=1
                group by item,INVNUMBER) sales
                right join 
                (select ITEMNO,GPMNAME,GPMID,EXID,CP01 from PRINFOSKF where GPMNAME like ?
                and brand in (select distinct BRAND from gpmbrand where [name] like ? )) as item
                on sales.ITEM=item.ITEMNO
                group by GPMNAME,GPMID,EXID,CP01
                         """, conn, params=(name, name))

    GPM_sales_list = gpm_sales_inv_line['SalesValue'].to_list()
    gpm_invoice_list = gpm_sales_inv_line['num_of_inv'].to_list()
    gpm_invoice_line_list = gpm_sales_inv_line['num_of_inv_line'].to_list()
    # print(GPM_sales_list)
    GPM_SALES_SUM = sum(GPM_sales_list)
    gpm_invoice_sum = sum(gpm_invoice_list)
    gpm_invoice_line_sum = sum(gpm_invoice_line_list)
    # print(gpm_invoice_sum)
    # print('Sales', GPM_SALES_SUM)
    # print('five')

    if len(str(int(GPM_SALES_SUM))) >= 8:
        Sales_value_in_crore = str("{:.2f}".format((GPM_SALES_SUM / 10000000), 2)) + ' Cr'
    else:
        Sales_value_in_crore = str("{:.2f}".format((GPM_SALES_SUM / 1000000), 2)) + ' M'

    # print('Sales', Sales_value_in_crore)

    try:
        achievement_target_sales = str("{:.2f}".format(((GPM_SALES_SUM / GPM_TARGET_SUM) * 100), 2)) + ' %'
        # print(achievement_target_sales)
    except:
        achievement_target_sales = str(0) + ' %'
    brand_no_of_invoice = str("{:.2f}".format(gpm_invoice_sum / 1000, 2)) + ' K'
    # print(brand_no_of_invoice)

    if gpm_invoice_sum <= 0:
        average_no_of_invoice_line = 0
    else:
        average_no_of_invoice_line = str("{:.2f}".format(gpm_invoice_line_sum / gpm_invoice_sum, 2))
    # print(average_no_of_invoice_line)

    # # --------------------------- MTD summery --------------------------------------------------
    # # ------------------------------------------------------------------------------------------

    mtd_sales_df = pd.read_sql_query(""" select GPMNAME,GPMID,EXID,CP01,isnull(sum(EXTINVMISC), 0) as SalesValue,
                isnull(count(distinct INVNUMBER), 0) as  num_of_inv,
                isnull(sum(LINECOUNT), 0) as num_of_inv_line from (
                select item,INVNUMBER,sum(EXTINVMISC) as EXTINVMISC,sum(QTYSHIPPED) as QTYSHIPPED,count(item) as LINECOUNT from OESalesDetails
                where TRANSDATE between  convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112)
                and  convert(varchar(10),getdate()-1, 112)
                group by item,INVNUMBER) sales
                right join 
                (select ITEMNO,GPMNAME,GPMID,EXID,CP01 from PRINFOSKF where GPMNAME like ?
                and brand in (select distinct BRAND from gpmbrand where [name] like ? )) as item
                on sales.ITEM=item.ITEMNO
                group by GPMNAME,GPMID,EXID,CP01 """, conn, params=(name, name))

    mtd_sale = sum(mtd_sales_df.SalesValue.tolist())
    if len(str(int(mtd_sale))) >= 8:
        mtd_sales = str("{:.2f}".format((mtd_sale / 10000000), 2)) + ' Cr'
    else:
        mtd_sales = str("{:.2f}".format((mtd_sale / 1000000), 2)) + ' M'

    # # ----- MTD Target --------------------------------------------
    import datetime
    now = datetime.datetime.now()
    current_date = now.day

    mtd_target = GPM_TARGET_SUM * (current_date - 1)
    if len(str(int(mtd_target))) >= 8:
        mtd_targets = str("{:.2f}".format((mtd_target / 10000000), 2)) + ' Cr'
    else:
        mtd_targets = str("{:.2f}".format((mtd_target / 1000000), 2)) + ' M'

    # # ----------------- mtd_achivement ---------------------------------------------------------
    try:
        mtd_achiv = str("{:.2f}".format((mtd_sale / mtd_target) * 100)) + ' %'
    except:
        mtd_achiv = '0 %'

    # # ------------- Growth Rate ------------------------------------------------------------------
    growth_df = pd.read_sql_query(""" select sum(LastMonthMTDSales) as LastMonthMTDSales, sum(ThisMonthMTDSales) as ThisMonthMTDSales
                from (
                select ITEM, 
                    sum(case when TRANSDATE between  convert(varchar(8), DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE())-1, 0), 112)
                    and   left(convert(varchar(8), DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE())-1,0), 112), 6) + right(convert(varchar(8), GETDATE()-1, 112), 2)
                  and TRANSTYPE=1 then EXTINVMISC else 0 end) as LastMonthMTDSales, 
                
                    isnull(sum(case when TRANSDATE between  convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112)
                    and  convert(varchar(10),getdate()-1, 112)  and TRANSTYPE=1 then EXTINVMISC else 0 end), 0) as ThisMonthMTDSales
                from OESalesDetails
                group by ITEM
                ) sales
                right join 
                (select ITEMNO,GPMNAME,GPMID,EXID,CP01 from PRINFOSKF where GPMNAME like ?
                and brand in (select distinct BRAND from gpmbrand where [name] like ? )) as item
                on sales.ITEM=item.ITEMNO
                where LastMonthMTDSales is not null

                """, conn, params=(name, name))

    last_month_mtd_sales = int(growth_df.LastMonthMTDSales)
    thismonth_mtd_sales = int(growth_df.ThisMonthMTDSales)

    mtd_growth = str(
        "{:.2f}".format(((thismonth_mtd_sales - last_month_mtd_sales) / last_month_mtd_sales) * 100)) + ' %'

    # # ------------- MTD Trend --------------------------------------------------------------------
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    try:
        mtd_trend = ((mtd_sale / (current_date - 1)) * days_in_month)

        if len(str(int(mtd_trend))) >= 8:
            mtd_trend = str("{:.2f}".format((mtd_trend / 10000000), 2)) + ' Cr'
        else:
            mtd_trend = str("{:.2f}".format((mtd_trend / 1000000), 2)) + ' M'

    except:
        mtd_trend = '0'



    # # -------------------------------------------------------------------------------------------
    image = Image.open(dir.get_directory() + "/Images/dash_kpi.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(dir.get_directory() + '/Images/FrancoisOne-Regular.ttf', 30)
    draw.text((80, 83), str(total_brand_list[0]), font=font, fill=(39, 98, 236))
    draw.text((225, 83), str(len(y2)) + ' (' + brand_coverage + ')', font=font, fill=(39, 95, 236))
    draw.text((460, 83), str(total_sku_list[0]), font=font, fill=(39, 98, 236))

    draw.text((610, 83), str(sold_sku_list[0]) + ' (' + sold_sku_percentage + ')', font=font, fill=(39, 98, 236))
    draw.text((805, 83), str(no_stock_sku_list[0]) + ' (' + No_stock_sku_percentage + ')', font=font, fill=(39, 98,
                                                                                                            236))

    draw.text((60, 177), Target_value_in_crore, font=font, fill=(39, 98, 236))
    draw.text((250, 177), Sales_value_in_crore, font=font, fill=(39, 98, 236))
    draw.text((425, 177), achievement_target_sales, font=font, fill=(39, 98, 236))
    draw.text((635, 177), brand_no_of_invoice, font=font, fill=(39, 98, 236))
    draw.text((835, 177), str(average_no_of_invoice_line), font=font, fill=(39, 98, 236))

    draw.text((60, 315), mtd_targets, font=font, fill=(0, 0, 0))
    draw.text((250, 315), mtd_sales, font=font, fill=(0, 0, 0))
    draw.text((425, 315), mtd_achiv, font=font, fill=(0, 0, 0))
    draw.text((610, 315), mtd_trend, font=font, fill=(0, 0, 0))
    draw.text((820, 315), mtd_growth, font=font, fill=(0, 0, 0))

    # image.show()
    image.save('./Images/dashboard.png')

    print('3. Dash generated\n')
