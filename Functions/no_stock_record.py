import pandas as pd
import xlrd

import Functions.operational_functionality as ofn

def get_No_Stock_Records():
    excel_data_df = pd.read_excel('Data/NOStock.xlsx', sheet_name='Sheet1', usecols=['BSL NO', 'BRAND'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/NOStock.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    # print('No Sales dataset Start printing in HTML')
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
            tabletd = tabletd + "<td class=\"number_style\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            # Total Ordered
            tabletd = tabletd + "<td class=\"number_style\">" + str(ofn.number_style(str(int(sh.cell_value(i,
                                                                                                     j))))) + "</td>\n"

        for j in range(6, 7):
            # Estimated Sales
            tabletd = tabletd + "<td class=\"number_style\">" + str(ofn.number_style(str(int(sh.cell_value(i,
                                                                                                     j))))) + "</td>\n"

        table1 = tabletd + "</tr>\n"
    print("No Stock table Created")
    return table1


def get_No_Stock_Records1():
    wb = xlrd.open_workbook('Data/NOStock.xlsx', sheet_name='Sheet1')
    sh = wb.sheet_by_name('Sheet1')
    th = ""
    td = ""
    for i in range(0, 1):
        th = th + "<tr>\n"
        th = th + "<th class=\"table7head\">SL</th>"

        for j in range(0, sh.ncols):
            th = th + "<th class=\"table7head\" >" + str(sh.cell_value(i, j)) + "</th>\n"
            th = th + "</tr>\n"


        table1 = th + td + "</tr>\n"
        print("No Stock table Created")
        return table1
