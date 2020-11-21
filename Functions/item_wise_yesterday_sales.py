import Functions.operational_functionality as ofn
import pandas as pd
import xlrd


def item_wise_yesterday_sales_Records():
    df_y_scock = pd.read_excel('Data/gpm_data.xlsx')
    df_stock = df_y_scock.drop(
        df_y_scock.columns[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                            27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                            47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                            70,
                            71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]], axis=1)

    yesterday_sales = df_stock.loc[df_stock['YesterdaySalesQty'] >= 1]
    yesterday_no_sales = df_stock.loc[df_stock['YesterdaySalesQty'] <= 0]

    import numpy as np
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales = yesterday_no_sales.drop(yesterday_no_sales.columns[[2]], axis=1)
    yesterday_no_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_no_sales)) + 1)
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales.to_excel('Data/yesterday_no_sales.xlsx', index=False)
    print('11. Yesterday No Sales Data Saved')

    yesterday_sales = yesterday_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty',
       'TP', 'TP Sales Value', 'Net Sales Value', 'Discount']]

    yesterday_sales = yesterday_sales.drop(yesterday_sales.columns[[2]], axis=1)
    yesterday_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_sales)) + 1)
    yesterday_sales = yesterday_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty',
       'TP', 'TP Sales Value', 'Net Sales Value', 'Discount']]
    yesterday_sales.to_excel('Data/item_wise_yesterday_sales.xlsx', index=False)


    #-----------------change excel percentage---------------------

    dataf = pd.read_excel('Data/item_wise_yesterday_sales.xlsx')

    yesterday_sales_quantity = dataf['YesterdaySalesQty'].to_list()

    yesterday_sales_quantity_sum = sum(yesterday_sales_quantity)

    yesterdaySalesQtyPercentList = []

    for i in yesterday_sales_quantity:
        var = str(round(((i / yesterday_sales_quantity_sum) * 100), 2)) + '%'
        yesterdaySalesQtyPercentList.append(var)

    net_Sales_Value = dataf['Net Sales Value'].to_list()
    net_Sales_Value_Sum = sum(net_Sales_Value)

    netSalesValuePercentList = []

    for i in net_Sales_Value:
        var = str(round(((i / net_Sales_Value_Sum) * 100), 2)) + '%'
        netSalesValuePercentList.append(var)

    df_four = pd.DataFrame(yesterdaySalesQtyPercentList)
    df_five = pd.DataFrame(netSalesValuePercentList)

    col_one = 0, 1, 2, 3, 4, 5
    dataframe_one = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', usecols=col_one)

    col_two = 6, 7, 8
    dataframe_two = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', usecols=col_two)

    col_three = 9, 10
    dataframe_three = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', usecols=col_three)

    writer = pd.ExcelWriter('Data/item_wise_yesterday_sales_Copy2.xlsx', engine='xlsxwriter')
    dataframe_one.to_excel(writer, sheet_name='Sheet1', index=False, startcol=0, startrow=0)
    df_four.to_excel(writer, sheet_name='Sheet1', index=False, startcol=6, startrow=0)
    dataframe_two.to_excel(writer, sheet_name='Sheet1', index=False, startcol=7, startrow=0)
    df_five.to_excel(writer, sheet_name='Sheet1', index=False, startcol=10, startrow=0)
    dataframe_three.to_excel(writer, sheet_name='Sheet1', index=False, startcol=11, startrow=0)

    writer.save()

    print('11.1. Yesterday Item wise sales data saved')


    excel_data_df = pd.read_excel('Data/item_wise_yesterday_sales_Copy2.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/item_wise_yesterday_sales_Copy2.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    tabletd = ""
    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td class=\"serial\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            # ITemNo
            tabletd = tabletd + "<td class=\"serial\">" + str(int((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td class=\"y_desc_sales\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(str(int((sh.cell_value(i, j))))) + "</td>\n"

        for j in range(6, 7):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(7, 8):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(str(int((sh.cell_value(i, j))))) + "</td>\n"

        for j in range(8, 9):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(str(int((sh.cell_value(i, j))))) + "</td>\n"

        for j in range(9, 10):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(str(int((sh.cell_value(i, j))))) + "</td>\n"

        for j in range(10, 11):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(11, 12):
            # unit
            tabletd = tabletd + "<td class=\"number_style\">" + \
                      ofn.number_style(str(int((sh.cell_value(i, j))))) + "</td>\n"

        table1 = tabletd + "</tr>\n"

    print("11.2. Yesterday Item wise sale table Created")
    return table1


def grandtotal():
    excel_data_df = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySalesQty',
       'TP', 'TP Sales Value', 'Net Sales Value', 'Discount'])
    yesterday_sale_list = excel_data_df['TP Sales Value'].tolist()
    sum_yesterday_value = int(sum(yesterday_sale_list))
    discountval_list = excel_data_df['Net Sales Value'].tolist()
    sum_discountval_value = int(sum(discountval_list))
    salesval_list = excel_data_df['Discount'].tolist()
    sum_salesval_value = int(sum(salesval_list))

    tabletd = ""

    tabletd = tabletd + "<tr>\n"

    tabletd = tabletd + "<td colspan='8' class=\"grand_total\">" + str('Grand Total') + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" \
              + ofn.number_style(str(sum_yesterday_value)) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + ofn.number_style(
        str(sum_discountval_value)) + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + '' + "</td>\n"

    tabletd = tabletd + "<td class=\"grand_total\" style=\"text-align: right\">" + ofn.number_style(str(
        sum_salesval_value)) + "</td>\n"

    tab = tabletd + "</tr>\n"
    print("11.3. Yesterday grand total value added at the bottom of the table\n")
    return tab


def item_wise_yesterday_no_sales_Records():
    df_y_scock = pd.read_excel('Data/yesterday_no_sales.xlsx')

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

    print("12. Yesterday No sale table Created\n")
    return table1
