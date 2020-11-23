import pandas as pd
def dataFormating():
    # 1st excel file
    cols_1 = 0, 1, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67
    df_1 = pd.read_excel('./Data/branch_wise_aging_stock.xlsx', usecols=cols_1)

    writer = pd.ExcelWriter('./Data/branch_wise_aging_stock_copy.xlsx', engine='xlsxwriter')
    df_1.to_excel(writer, sheet_name='Sheet1', index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 50)
    worksheet.set_column('C:AH', 16)
    writer.save()

    # 2nd excel file
    df_2 = pd.read_excel('./Data/branch_wise_stock_status.xlsx')
    writer2 = pd.ExcelWriter('./Data/branch_wise_stock_status_copy.xlsx', engine='xlsxwriter')
    df_2.to_excel(writer2, sheet_name='Sheet1', index=False)
    worksheet2 = writer2.sheets['Sheet1']
    worksheet2.set_column('B:B', 15)
    worksheet2.set_column('D:H', 20)
    writer2.save()

    # 3rd excel file
    cols_7 = range(0, 10)
    df_7 = pd.read_excel('./Data/item_wise_yesterday_sales.xlsx', usecols=cols_7)

    writer7 = pd.ExcelWriter('./Data/item_wise_yesterday_sales_copy.xlsx', engine='xlsxwriter')
    df_7.to_excel(writer7, sheet_name='Sheet1', index=False)

    worksheet7 = writer7.sheets['Sheet1']
    worksheet7.set_column('B:B', 16)
    worksheet7.set_column('D:D', 40)
    worksheet7.set_column('F:F', 20)
    worksheet7.set_column('H:I', 20)
    writer7.save()

    # 4th excel file
    cols_8 = range(0, 5)
    df_8 = pd.read_excel('./Data/NoSales.xlsx', usecols=cols_8)

    writer8 = pd.ExcelWriter('./Data/NoSales_last_three_month_copy.xlsx', engine='xlsxwriter')
    df_8.to_excel(writer8, sheet_name='Sheet1', index=False)

    worksheet8 = writer8.sheets['Sheet1']
    worksheet8.set_column('B:B', 16)
    worksheet8.set_column('D:D', 40)
    writer8.save()

    # 5th excel file
    cols_9 = range(0, 7)
    df_9 = pd.read_excel('./Data/NoStock.xlsx', usecols=cols_9)

    writer9 = pd.ExcelWriter('./Data/NoStock_last_three_month_copy.xlsx', engine='xlsxwriter')
    df_9.to_excel(writer9, sheet_name='Sheet1', index=False)

    worksheet9 = writer9.sheets['Sheet1']
    worksheet9.set_column('B:B', 16)
    worksheet9.set_column('D:D', 40)
    worksheet9.set_column('F:G', 20)
    writer9.save()



    # 6th excel file
    cols_11 = range(0, 5)
    df_11 = pd.read_excel('./Data/yesterday_no_sales.xlsx', usecols=cols_11)

    writer11 = pd.ExcelWriter('./Data/yesterday_no_sales_copy.xlsx', engine='xlsxwriter')
    df_11.to_excel(writer11, sheet_name='Sheet1', index=False)

    worksheet11 = writer11.sheets['Sheet1']
    worksheet11.set_column('B:B', 16)
    worksheet11.set_column('D:D', 40)
    writer11.save()


    # 7th excel file
    cols_main = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 50, 51
    df_main = pd.read_excel('./Data/html_data_Sales_and_Stock.xlsx', usecols=cols_main)

    cols_main_2 = 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35
    df_main_2 = pd.read_excel('./Data/item_wise_stock_days.xlsx', usecols=cols_main_2)

    writer = pd.ExcelWriter('./Data/branch_wise_detailed_data_Sales_and_Stock-Copy.xlsx', engine='xlsxwriter')
    df_main.to_excel(writer, sheet_name='Sheet1', index=False, startcol=0, startrow=0)
    df_main_2.to_excel(writer, sheet_name='Sheet1', index=False, startcol=21, startrow=0)

    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('D:D', 40)
    worksheet.set_column('F:AZ', 20)
    worksheet.set_column('BA:CE', 15)
    worksheet.set_column('CF:CJ', 20)

    writer.save()

    print("19. All attached excels files are processed.")
