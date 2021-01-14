import Functions.operational_functionality as ofn
import pandas as pd
import xlrd
import numpy as np
from calendar import monthrange
from datetime import date, datetime
import Functions.db_connection as dbc

def formater(val):
    val = str(val)
    if len(val) > 0:
        val = int(val)
    else:
        val = ''
    return val


def item_wise_yesterday_sales_Records():
    df_y_scock = pd.read_excel('Data/gpm_data.xlsx')
    df_stock = df_y_scock.drop(
        df_y_scock.columns[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                            27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                            47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                            70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]], axis=1)

    yesterday_sales = df_stock.loc[df_stock['YesterdaySalesQty'] >= 1]
    masterData = df_y_scock.loc[df_stock['YesterdaySalesQty'] >= 1]

    yesterday_no_sales = df_stock.loc[df_stock['YesterdaySalesQty'] <= 0]

    import numpy as np
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales = yesterday_no_sales.drop(yesterday_no_sales.columns[[2]], axis=1)
    yesterday_no_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_no_sales)) + 1)
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales.to_excel('Data/yesterday_no_sales.xlsx', index=False)

    print('12. Yesterday No Sales Data Saved')

    yesterday_sales = yesterday_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty',
                                       'TP', 'TP Sales Value', 'Net Sales Value', 'Discount']]

    yesterday_sales = yesterday_sales.drop(yesterday_sales.columns[[2]], axis=1)
    yesterday_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_sales)) + 1)

    # -----------------change excel percentage---------------------

    yesterday_sales_quantity = yesterday_sales['YesterdaySalesQty'].to_list()
    yesterday_sales_quantity_sum = sum(yesterday_sales_quantity)
    yesterdaySalesQtyPercentList = []

    for i in yesterday_sales_quantity:
        var = str(round(((i / yesterday_sales_quantity_sum) * 100), 2)) + '%'
        yesterdaySalesQtyPercentList.append(var)

    net_Sales_Value = yesterday_sales['Net Sales Value'].to_list()
    net_Sales_Value_Sum = sum(net_Sales_Value)

    netSalesValuePercentList = []

    for i in net_Sales_Value:
        var = str(round(((i / net_Sales_Value_Sum) * 100), 2))
        netSalesValuePercentList.append(var)

    monthlySalesTarget = masterData['Monthly Sales Target'].to_list()

    actualSalesMTD = masterData['Actual Sales MTD'].to_list()

    dayWiseTarget = np.subtract(monthlySalesTarget, actualSalesMTD)

    dayWiseTarget2 = [0 if i < 0 else i for i in dayWiseTarget]

    today = str(date.today())
    datee = datetime.strptime(today, "%Y-%m-%d")
    date_val = int(datee.day)
    num_days = monthrange(datee.year, datee.month)[1]
    rest_of_day = (num_days - date_val) + 1

    dayWiseTarget3 = np.divide(dayWiseTarget2, rest_of_day)
    dayTarget = []
    for a in dayWiseTarget3:
        dayTarget.append(int(a))

    df = pd.DataFrame()  # 'BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty',
    # 'TP', 'TP Sales Value', 'Net Sales Value', 'Discount'
    df['BSL NO'] = yesterday_sales['BSL NO']
    df['BRAND'] = yesterday_sales['BRAND']
    df['ISL NO'] = yesterday_sales['ISL NO']
    df['Item Name'] = yesterday_sales['Item Name']
    df['UOM'] = yesterday_sales['UOM']
    df['Sales Quantity'] = yesterday_sales['YesterdaySalesQty']

    df['Sales Quantity %'] = netSalesValuePercentList
    df['Monthly Target'] = monthlySalesTarget
    df['MTD Sales Target'] = actualSalesMTD

    df['TP'] = yesterday_sales['TP']
    df['TP Sales Value'] = yesterday_sales['TP Sales Value']
    df['Net Sales Value'] = yesterday_sales['Net Sales Value']
    df['Net Sakes %'] = netSalesValuePercentList
    df['Discount'] = yesterday_sales['Discount']
    df['LD Target Qty/Day'] = dayTarget
    df.to_excel('Data/item_wise_yesterday_sales.xlsx', index=False)

    print('12.1. Yesterday Item wise sales data saved')

    excel_data_df = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/item_wise_yesterday_sales.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    tabletd = ""
    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td class=\"sl_center\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            tabletd = tabletd + "<td class=\"sl_center\">" + str(int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(3, 4):
            tabletd = tabletd + "<td class=\"y_desc_sales\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            tabletd = tabletd + "<td class=\"number_style\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        for j in range(6, 7):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str((sh.cell_value(i, j))) + '%' + "</td>\n"

        for j in range(7, 8):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        for j in range(8, 9):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        for j in range(9, 10):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        for j in range(10, 11):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        for j in range(11, 12):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"
        for j in range(12, 13):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(((sh.cell_value(i, j)))) + '%' + "</td>\n"
        for j in range(13, 14):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(14, 15):
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str(ofn.number_style(str(int(sh.cell_value(i, j))))) + "</td>\n"

        table1 = tabletd + "</tr>\n"

    print("12.2. Yesterday Item wise sale table Created")
    return table1


def grandtotal():
    excel_data_df = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'Sales Quantity',
                                           'Sales Quantity %', 'Monthly Target', 'MTD Sales Target', 'TP',
                                           'TP Sales Value', 'Net Sales Value', 'Net Sakes %',
                                           'Discount', 'LD Target Qty/Day'])

    yesterday_sales_quantity_list = excel_data_df['Sales Quantity'].tolist()
    sum_yesterday_sales_quantity_value = int(sum(yesterday_sales_quantity_list))

    yesterday_sales_quantity_percent_list = excel_data_df['Sales Quantity %'].tolist()
    sum_yesterday_sales_quantity_percent_value = sum(yesterday_sales_quantity_percent_list)

    monthly_target_list = excel_data_df['Monthly Target'].tolist()
    sum_monthly_target_value = sum(monthly_target_list)

    MTD_target_list = excel_data_df['MTD Sales Target'].tolist()
    sum_MTD_target_value = sum(MTD_target_list)

    TP_sales_value_list = excel_data_df['TP Sales Value'].tolist()
    sum_TP_Sales_value = sum(TP_sales_value_list)

    Net_sales_value_list = excel_data_df['Net Sales Value'].tolist()
    sum_Net_Sales_value = sum(Net_sales_value_list)

    Net_sales_value_percent_list = excel_data_df['Net Sakes %'].tolist()
    sum_Net_Sales_percent_value = sum(Net_sales_value_percent_list)

    discount_list = excel_data_df['Discount'].tolist()
    sum_discount_value = sum(discount_list)

    LD_target_quantity_list = excel_data_df['LD Target Qty/Day'].tolist()
    sum_LD_target_quantity_value = sum(LD_target_quantity_list)

    tabletd = ""

    tabletd = tabletd + "<tr>\n"

    tabletd = tabletd + "<td colspan='5' class=\"grand_total\">" + str('Grand Total') + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(sum_yesterday_sales_quantity_value)) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + str(round(sum_yesterday_sales_quantity_percent_value)) + "%" + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(sum_monthly_target_value)) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(sum_MTD_target_value)) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + '' + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(round(sum_TP_Sales_value))) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(round(sum_Net_Sales_value))) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + str(round(sum_Net_Sales_percent_value)) + "%" + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + ofn.number_style(
        str(int(sum_discount_value))) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + ofn.number_style(str(
        sum_LD_target_quantity_value)) + "</td>\n"

    tab = tabletd + "</tr>\n"
    print("12.3. Yesterday grand total value added at the bottom of the table")
    return tab


def item_wise_yesterday_no_sales_Records():
    excel_data_df = pd.read_excel('Data/yesterday_no_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/yesterday_no_sales.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    tabletd = ""
    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td class=\"serialno\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            # ITemNo
            tabletd = tabletd + "<td class=\"serialno\">" + str(int((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td class=\"y_desc_sales\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + str((sh.cell_value(i, j))) + "</td>\n"

        table1 = tabletd + "</tr>\n"

    print("13. Yesterday No sale table Created\n")
    return table1


def region_wise_yesterday_item_sales(name):
    df = pd.read_sql_query("""
            select BrandName as BRAND, ROW_NUMBER() OVER (ORDER BY (SELECT 1)) AS number, * from(select * from (select PRINFOSKF.BRAND as BrandName, OESalesDetails.[DESC] as [Item Description], rsmtr,isnull(sum(extinvmisc),0) as sales from OESalesDetails
            left join prinfoskf
            on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
            
            left join GPMBRAND
            on PRINFOSKF.BRAND = GPMBRAND.Brand
            where GPMBRAND.Name like ? and  transdate=  convert(varchar(8),getdate()-1, 112) and TRANSTYPE = 1
            group by PRINFOSKF.brand,rsmtr, OESalesDetails.item, OESalesDetails.[DESC]) as t1
            pivot
            (
            SUM(sales)
            --for EXE in (' + @cols + ')
            for rsmtr in ([BB],[BJ],[BN],[CD],[CG],[CH],[CL],[CR],[CS],[CT],[DB],[DD],[DK],[DM],[DS],[DT],[FK],[FR],[GK],[JS],[KB],[KC],[KN],[MG],[MH],
            [ML],[MS],[ND],[NM],[PB],[PS],[RK],[RN],[SB],[SM],[SS],[TJ],[UM],[WS],[ZREGION]) 
            ) piv
            ) main
            ORDER BY BRAND
            """, dbc.connection, params={name})

    df = df.drop(['BrandName'], axis=1)
    df = df.fillna(0)

    df.to_excel('Data/items_region_wise_yesterday_sales.xlsx', index=False)
    import time
    time.sleep(5)


    excel_data_df = pd.read_excel('Data/items_region_wise_yesterday_sales.xlsx', sheet_name='Sheet1')


    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/items_region_wise_yesterday_sales.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    tabletd = ""
    th = ""
    # for i in range(0, 1):
    #     th = th + "<tr>\n"
    #     # th = th + "<th class=\"unit\">ID</th>"
    #     for j in range(0, 1):
    #         # Brand
    #         th = th + "<th class=\"brandtd\" >" + str(sh.cell_value(i, j)) + "</th>\n"
    #     for j in range(1, 2):
    #         # SL
    #         th = th + "<th class=\"serialno\" >" + str(sh.cell_value(i, j)) + "</th>\n"
    #
    #     for j in range(2, 3):
    #         # Desc
    #         th = th + "<th class=\"y_desc_sales\" >" + str(sh.cell_value(i, j)) + "</th>\n"
    #
    #     for j in range(3, sh.ncols):
    #         # All
    #         th = th + "<th class=\"unit\" >" + str(sh.cell_value(i, j)) + "</th>\n"
    #     th = th + "</tr>\n"

    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"

        for j in range(0, 1):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"



        for j in range(1, 2):
            # SL
            tabletd = tabletd + "<td class=\"serialno\">" + str(int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(2, 3):
            # item Desc
            tabletd = tabletd + "<td class=\"y_desc_sales\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(3, 43):
            tabletd = tabletd + "<td class=\"number_style\">" + str(ofn.number_style1((sh.cell_value(i, j)))) + "</td>\n"

        table1 = th + tabletd + "</tr>\n"

    print("13#. Region wise Items yesterday sales \n")
    return table1
