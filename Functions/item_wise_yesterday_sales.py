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

    yesterday_sales = df_stock.loc[df_stock['YesterdaySales'] >= 1]
    yesterday_no_sales = df_stock.loc[df_stock['YesterdaySales'] <= 0]

    import numpy as np
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales = yesterday_no_sales.drop(yesterday_no_sales.columns[[2]], axis=1)
    yesterday_no_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_no_sales)) + 1)
    yesterday_no_sales = yesterday_no_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    yesterday_no_sales.to_excel('Data/yesterday_no_sales.xlsx', index=False)

    yesterday_sales = yesterday_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySales']]
    yesterday_sales = yesterday_sales.drop(yesterday_sales.columns[[2]], axis=1)
    yesterday_sales.insert(loc=2, column='ISL NO', value=np.arange(len(yesterday_sales)) + 1)
    yesterday_sales = yesterday_sales[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySales']]
    yesterday_sales.to_excel('Data/item_wise_yesterday_sales.xlsx', index=False)

    print('yesterday sales and no sales excel generated')

    excel_data_df = pd.read_excel('Data/item_wise_yesterday_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'YesterdaySales'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/item_wise_yesterday_sales.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    print('No Sales dataset Start printing in HTML')
    #
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
            tabletd = tabletd + "<td class=\"descriptiontd\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"style1\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            # unit
            tabletd = tabletd + "<td class=\"style1\">" + \
                      ofn.number_style(str(int((sh.cell_value(i,j))))) + "</td>\n"

        table1 = tabletd + "</tr>\n"
    print("item wise yesterday sale table Created")
    return table1


def item_wise_yesterday_no_sales_Records():
    df_y_scock = pd.read_excel('Data/yesterday_no_sales.xlsx')

    excel_data_df = pd.read_excel('Data/yesterday_no_sales.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/yesterday_no_sales.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    print('Yesterday  No sales ')
    #
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
            tabletd = tabletd + "<td class=\"descriptiontd\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"style1\">" + str((sh.cell_value(i, j))) + "</td>\n"

        table1 = tabletd + "</tr>\n"
    print("item wise yesterday No sale table Created")
    return table1
