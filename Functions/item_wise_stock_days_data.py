
import pandas as pd
import numpy as np
import xlsxwriter
import sys
import xlrd
import re
import Functions.operational_functionality as ofn

df_main = pd.read_excel('Data/gpm_data.xlsx')
df0 = df_main[df_main['Avg Sales/Day'] != 0]
df0.to_excel('Data/gpm_stock_data_for_day_diff.xlsx', index=False)
# sys.exit()

df = pd.read_excel('Data/gpm_stock_data_for_day_diff.xlsx')
cols = range(52, 83)
df2 = pd.read_excel('Data/gpm_stock_data_for_day_diff.xlsx', usecols=cols)
l = list(df2.columns)
# print(l)

cols2 = range(19, 50)
df3 = pd.read_excel('Data/gpm_stock_data_for_day_diff.xlsx', usecols=cols2)
l2 = list(df3.columns)
# print(l2)

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

    # print(branch_current_stock)
    # print(branch_avg_sell)

    np.seterr(divide='ignore', invalid='ignore')
    branch_stock_limit = np.divide(branch_current_stock, branch_avg_sell)
    branch_stock_limit_list = list(branch_stock_limit)

    # print(branch_stock_limit_list)
    # sys.exit()
    each_branch_analytics_value = []

    for i in branch_stock_limit_list:
        limit_value = 35
        if i <= limit_value:
            index_of_values = branch_stock_limit_list.index(i)
            month = int(i / 30)
            Day = int(i % 30)
            quantity_value = str(branch_current_stock[index_of_values])
            value_to_be_shown = quantity_value + '  -' + str(month) + "M" + str(Day) + "D" + ""
            each_branch_analytics_value.append(value_to_be_shown)
        # Super Under Stock
        elif i > 35:
            index_of_values = branch_stock_limit_list.index(i)
            month = int(i / 30)
            Day = int(i % 30)
            quantity_value =  str(branch_current_stock[index_of_values])
            value_to_be_shown = quantity_value + '  ' + str(month) + "M" + str(Day) + "D" + ""
            each_branch_analytics_value.append(value_to_be_shown)
    # print(each_branch_analytics_value)
    final_list.append(each_branch_analytics_value)
# print(final_list)
# sys.exit()
first_column = df['BSL NO'].tolist()
second_column = df['BRAND'].tolist()
third_column = df['ISL NO'].tolist()
fourth_column = df['Item Name'].tolist()
fifth_column = df['UOM'].tolist()

label_list = ['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'BOG', 'BSL', 'COM', 'COX', 'CTG', 'CTN', 'DNJ', 'FEN',
              'FRD', 'GZP', 'HZJ', 'JES', 'KHL', 'KRN', 'KSG', 'KUS', 'MHK', 'MIR', 'MLV', 'MOT', 'MYM', 'NAJ', 'NOK',
              'PAT', 'PBN', 'RAJ', 'RNG', 'SAV', 'SYL', 'TGL', 'VRB']
third_column_serial_change=range(1, len(first_column)+1)

workbook = xlsxwriter.Workbook('Data/item_wise_stock_days.xlsx')
worksheet = workbook.add_worksheet()

length_of_label = range(0, len(label_list))
length_of_column_values = range(1, len(first_column) + 1)
# print(length)

for i, j, k, l, m, n in zip(first_column, second_column, third_column_serial_change, fourth_column, fifth_column,
                            length_of_column_values):
    worksheet.write(n, 0, i)
    worksheet.write(n, 1, j)
    worksheet.write(n, 2, k)
    worksheet.write(n, 3, l)
    worksheet.write(n, 4, m)
for o, p in zip(label_list, length_of_label):
    worksheet.write(0, p, o)

a_range = length_of_column_values
# print(a_range)

b_range = range(5, len(label_list))
# print(b_range)

# sys.exit()

for b in b_range:  # starts from 5
    for a in a_range:  # start from 1
        c = final_list[b - 5][a - 1]
        # print(c)
        worksheet.write(a, b, c)
workbook.close()
print('Item wise stock days data generated')

def seperator(val):
    a = val.split('  ')
    c = str(a[0]) + "\n" + str(a[1])
    return c

def set_color(val):
    if '-' in val:
        color = '#ffba62'
    else:
        color = '#80ffff'

    return color