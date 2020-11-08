import pandas as pd
import numpy as np
import xlsxwriter
import xlrd
import sys
import Functions.operational_functionality as ofn

# # -------------------------------------------------------------------
# # ------ Branch wise stock summery -----------------------------------


df = pd.read_excel('Data/gpm_data.xlsx')

cols = range(52, 83)
df2 = pd.read_excel('Data/gpm_data.xlsx', usecols=cols)
l = list(df2.columns)

cols2 = range(19, 50)
df3 = pd.read_excel('Data/gpm_data.xlsx', usecols=cols2)
l2 = list(df3.columns)

final_list = []

for branches, avgq in zip(l, l2):
    branch_current_stock = df[branches].to_list()

    branch_avg_sell = df[avgq].to_list()

    for each, each2 in zip(branch_current_stock, branch_avg_sell):
        if each == 0:
            index = branch_current_stock.index(each)
            branch_current_stock[index] = 1
        if each2 == 0:
            index2 = branch_avg_sell.index(each2)
            branch_avg_sell[index2] = 1

    np.seterr(divide='ignore', invalid='ignore')
    branch_stock_limit = np.divide(branch_current_stock, branch_avg_sell)
    branch_stock_limit_list = list(branch_stock_limit)

    new_list_nill = []
    new_list_super_under_stock = []
    new_list_under_stock = []
    new_list_normal_stock = []
    new_list_over_stock = []
    new_list_super_over_stock = []

    for i in branch_stock_limit_list:
        # Color for NIL
        if i <= 0:
            new_list_nill.append(i)
        # Super Under Stock
        elif i <= 15:
            new_list_super_under_stock.append(i)

        # Under Stock
        elif i <= 35:
            new_list_under_stock.append(i)

        # Color for Normal
        elif i <= 45:
            new_list_normal_stock.append(i)

        # Color for Over Stock
        elif i <= 60:
            new_list_over_stock.append(i)
        else:
            # Super over stock
            new_list_super_over_stock.append(i)

    sum_new_list_nill = len(new_list_nill)
    sum_new_list_super_under_stock = len(new_list_super_under_stock)
    sum_new_list_under_stock = len(new_list_under_stock)
    sum_new_list_normal_stock = len(new_list_normal_stock)
    sum_new_list_over_stock = len(new_list_over_stock)
    sum_new_list_super_over_stock = len(new_list_super_over_stock)

    sum_list = [sum_new_list_nill, sum_new_list_super_under_stock, sum_new_list_under_stock,
                sum_new_list_normal_stock, sum_new_list_over_stock, sum_new_list_super_over_stock]
    final_list.append(sum_list)

workbook = xlsxwriter.Workbook('Data/branch_wise_nil_us_ss.xlsx')
worksheet = workbook.add_worksheet()

len = range(1, len(l) + 1)

for i, j in zip(l, len):
    worksheet.write(j, 0, i)

stock_list = ['Branch', 'Nill', 'Super Under Stock', 'Under Stock', 'Normal Stock', 'Over Stock',
              'Super Over Stock']

len2 = range(0, 7)
for i, j in zip(stock_list, len2):
    worksheet.write(0, j, i)

# Branch wise value set
all_row_length = range(0, 31)
all_len = range(0, 6)

for a in all_row_length:
    for b in all_len:
        c = final_list[a][b]
        # print(c)
        worksheet.write(a + 1, b + 1, c)
workbook.close()
print('Branch wise stock summery Data generated')


def branch_wise_nil_us_ss():
    excel_data_df = pd.read_excel('Data/branch_wise_nil_us_ss.xlsx', sheet_name='Sheet1',
                                  usecols=['Branch', 'Nill', 'Super Under Stock', 'Under Stock', 'Normal Stock',
                                           'Over Stock', 'Super Over Stock'])
    bslno = excel_data_df['Branch'].tolist()
    brand = excel_data_df['Nill'].tolist()

    wb = xlrd.open_workbook('Data/branch_wise_nil_us_ss.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    # print('No Sales dataset Start printing in HTML')
    #
    tabletd = ""
    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            tabletd = tabletd + "<td class=\"serial\" style=\"font-weight: bold;\"" + str(bslno[i - 1]) + "\"> " + str(
                (sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            tabletd = tabletd + "<td class=\"style1\" rowspan=\"" + str(int(brand[i - 1])) + "\">" \
                      + str(int( sh.cell_value(i, j)) ) + "</td>\n"

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
    # print("No Sales table Created")
    return table6
