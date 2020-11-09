import pandas as pd


def number_style(value):
    if (len(value) > 6):
        return str(value[0:len(value) - 6] + "," + value[len(value) - 6:len(value) - 3] + ","
                   + value[len(value) - 3:len(value)])
    elif (len(value) > 3):
        return str(value[0:len(value) - 3] + "," + value[len(value) - 3:len(value)])
    elif (len(value) > 1):
        return value

    elif (len(value) == 1 and str(value) == '0'):
        return '-'
    else:
        return value


def warning(daily_sales, total_stock):
    if daily_sales <= 0:
        return False
    else:
        days_passed = total_stock / daily_sales
        # Color for NIL
        if days_passed <= 0:
            set_color = '#ff2300'

        # Super Under Stock
        elif days_passed >= 15:
            set_color = '#ff971a'

        # Under Stock
        elif days_passed <= 35:
            set_color = '#eee298'

        # Color for Normal
        elif days_passed <= 45:
            set_color = '#ffffff'

        # Color for Over Stock
        elif days_passed <= 60:
            set_color = '#cbe14c'
        else:
            # Super over stock
            set_color = '#fff900'

        return set_color


def branch_warning(total_stock):
    s = str(total_stock)

    if s== '-' or total_stock <= 0:
        set_color = 'red'
    # if total_stock <= 0:
    #     set_color = '#ff2300'

    # Super Under Stock
    elif total_stock >= 1 and total_stock <= 15:
        set_color = '#ff971a'

    # Under Stock
    elif total_stock >= 16 and total_stock <= 35:
        set_color = '#eee298'

    # Color for Normal
    elif total_stock >= 36 and total_stock <= 45:
        set_color = '#ffffff'

    # Color for Over Stock
    elif total_stock >= 46 and total_stock <= 60:
        set_color = '#cbe14c'

    elif total_stock >= 61 and total_stock <= 300000:
        set_color = '#fff900'
    else:
        # Super over stock
        set_color = 'red'

    return set_color


def create_dup_count_list(excel, colName):
    df = pd.DataFrame(excel)
    colRaw = df[colName].tolist()
    df1 = df
    df1.loc[df1.duplicated(subset=[colName]), colName] = ''
    colDup = df1[colName].tolist()
    k = 0
    colList = []
    for j in colDup:
        item1 = j
        i = 0
        for item in colRaw:
            if (item == item1):
                i = i + 1
        colList.insert(k, i)
        k = k + 1
    return colList


def status_color(status):
    if status == 'Within 15 Days':
        color = '#e82b04'

    elif status == 'Within 30 Days':
        color = '#ff7100'

    elif status == 'Within 60 Days':
        color = '#ffd100'

    elif status == 'Within 90 Days':
        color = '#bed32e'

    elif status == 'More Than 120 Days':
        color = '#6ef607'

    elif status == 'More Than 1 Year':
        color = '#6ef607'
    else:
        color = '#ff0000'
    return color
