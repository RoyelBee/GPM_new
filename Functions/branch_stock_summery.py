import pandas as pd
import numpy as np
import xlsxwriter
import xlrd
import sys
import Functions.operational_functionality as ofn

def branch_wise_nil_us_ss():
    excel_data_df = pd.read_excel('Data/branch_wise_nil_us_ss.xlsx', sheet_name='Sheet1',
                                  usecols=['Branch', 'Nill', 'Super Under Stock', 'Under Stock', 'Normal Stock', 'Over Stock', 'Super Over Stock'])
    bslno = excel_data_df['Branch'].tolist()
    brand = excel_data_df['Nill'].tolist()

    wb = xlrd.open_workbook('Data/branch_wise_nil_us_ss.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    print('No Sales dataset Start printing in HTML')
    #
    tabletd=""
    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            tabletd = tabletd + "<td class=\"serial\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                (sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            tabletd = tabletd + "<td class=\"style1\" rowspan=\"" + str(int(brand[i - 1])) + "\">" + str(
                sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            # ITemNo
            tabletd = tabletd + "<td class=\"style1\">" + str(int((sh.cell_value(i, j)))) + "</td>"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td class=\"style1\">" + str(int((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"style1\">" + str(int((sh.cell_value(i, j)))) + "</td>"

        for j in range(5, 6):
            # Total Ordered
            tabletd = tabletd + "<td class=\"style1\">" + str(ofn.number_style(str(int(sh.cell_value(i,
                                                                                                     j))))) + "</td>"

        for j in range(6, 7):
            # Estimated Sales
            tabletd = tabletd + "<td class=\"style1\">" + str(ofn.number_style(str(int(sh.cell_value(i,
                                                                                                     j))))) + "</td>"

        table6 = tabletd + "</tr>\n"
    print("No Sales table Created")
    return table6


