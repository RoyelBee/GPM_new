import pandas as pd
import xlrd
import Functions.operational_functionality as ofn


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

def item_stock_days():
    excel_data_df = pd.read_excel('Data/item_wise_stock_days.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND'])
    # bslno = excel_data_df['BSL NO'].tolist()
    # brand = excel_data_df['BRAND'].tolist()

    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/item_wise_stock_days.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    # print('No Sales dataset Start printing in HTML')
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
            tabletd = tabletd + "<td class=\"serial\">" + str(int((sh.cell_value(i, j)))) + "</td>"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td class=\"serial\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"remarks\">" + str((sh.cell_value(i, j))) + "</td>"


        for j in range(5, 36):
            # Estimated Sales
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      set_color(sh.cell_value(i, j)) + "\">" + seperator(sh.cell_value(i, j)) + "</td>\n"

        table6 = tabletd + "</tr>\n"

    print('16. Item wise stock days table created\n')
    return table6
