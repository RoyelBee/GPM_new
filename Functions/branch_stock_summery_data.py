
import pandas as pd
import numpy as np
import xlsxwriter
import xlrd
import sys
import Functions.operational_functionality as ofn

# # -------------------------------------------------------------------
# # ------ Branch wise stock summery -----------------------------------

def generate_summery_data():
    df = pd.read_excel('Data/gpm_data.xlsx')
    # print(df)

    cols = range(52, 83)
    df2 = pd.read_excel('Data/gpm_data.xlsx', usecols=cols)
    l = list(df2.columns)
    # print(l)

    cols2 = range(19, 50)
    df3 = pd.read_excel('Data/gpm_data.xlsx', usecols=cols2)
    l2 = list(df3.columns)
    # print(l2)

    # sys.exit()

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

        total_stock = sum_new_list_nill + sum_new_list_super_under_stock + sum_new_list_under_stock + sum_new_list_normal_stock + sum_new_list_over_stock + sum_new_list_super_over_stock

        sum_list = [total_stock, sum_new_list_nill, sum_new_list_super_under_stock, sum_new_list_under_stock,
                    sum_new_list_normal_stock, sum_new_list_over_stock, sum_new_list_super_over_stock]
        final_list.append(sum_list)

    workbook = xlsxwriter.Workbook('Data/branch_wise_stock_status.xlsx')
    worksheet = workbook.add_worksheet()

    len = range(1, len(l) + 1)

    for i, j in zip(l, len):
        worksheet.write(j, 0, i)

    stock_list = ['Branch', 'Total Item', 'Nill', 'Super Under Stock', 'Under Stock', 'Normal Stock', 'Over Stock',
                  'Super Over Stock']

    len2 = range(0, 8)
    for i, j in zip(stock_list, len2):
        worksheet.write(0, j, i)

    # Branch wise value set
    all_row_length = range(0, 31)
    all_len = range(0, 7)

    for a in all_row_length:
        for b in all_len:
            c = final_list[a][b]
            # print(c)
            worksheet.write(a + 1, b + 1, c)
    workbook.close()
    print('Branch wise stock status data generated')