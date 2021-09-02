import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
import numpy as np
from datetime import date
import calendar
import datetime
import Functions.db_connection as dbc


def convert(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number


def cumulative_target_sales(name):
    try:
        everday_sale_df = pd.read_sql_query(""" 
        select  right(TRANSDATE, 2) as Date, isnull(sum(EXTINVMISC),0) as ItemSales from OESalesDetails
        left join PRINFOSKF
        on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
        where left(TRANSDATE, 8) between convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112) and convert(varchar(8),DATEADD(D,0,GETDATE()-1),112)
        and PRINFOSKF.GPMNAME like ?
        and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name like ?)
        group by right(TRANSDATE, 2)
        order by right(TRANSDATE, 2)
            
            """, dbc.connection, params=(name, name))

        day_wise_date = everday_sale_df['Date'].tolist()
        day_to_day_sale = everday_sale_df['ItemSales'].tolist()
        # print('day wise date list : ', day_wise_date)
        # print('day wise sales list : ', day_to_day_sale)

        from datetime import date
        today = date.today()

        current_day = today.strftime("%d")
        current_day_in_int = int(current_day)
        # print("Current days in month till today: ", current_day_in_int)

        final_days_array = []
        final_sales_array = []
        for t_va in range(0, current_day_in_int - 1):
            final_days_array.append(day_wise_date[t_va])
            final_sales_array.append(day_to_day_sale[t_va])

        # print('Reduced 0 value days from the list : ', final_days_array)
        # print('Sales Taken According to the value of days : ', final_sales_array)

        EveryDay_target_df = pd.read_sql_query("""   
            Declare @CurrentMonth NVARCHAR(MAX);
            Declare @DaysInMonth NVARCHAR(MAX);
            SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
            SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
            select  isnull(sum(TRGVAL),0)/@DaysInMonth as MonthsTargetQty
            from ARCSECONDARY.dbo.PRODUCT_WISE_TRG
            left join PRINFOSKF
            on PRODUCT_WISE_TRG.ITEM = PRINFOSKF.ITEMNO
            where YRM = CONVERT(varchar(6), dateAdd(month,0,getdate()), 112) and GPMNAME LIKE ?
            and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name LIKE ?)

                                
            """, dbc.connection, params=(name, name))

        single_day_target = EveryDay_target_df['MonthsTargetQty'][0]
        # print('Single Day Target : ', single_day_target)

        y_pos = np.arange(len(final_days_array))

        n = 1
        labell_to_plot = []
        for z in y_pos:
            labell_to_plot.append(n)
            n = n + 1
        # print('Final label to plot : ', labell_to_plot)

        # ----------------code for cumulitive sales------------

        now = datetime.datetime.now()
        total_days = calendar.monthrange(now.year, now.month)[1]
        # print('Total number of days in this month : ', total_days)

        # monthly_trend = (sum(final_sales_array) / (current_day_in_int-1))*total_days
        # print('Monthly Trend: ',monthly_trend)

        monthly_trend_per_day = (sum(final_sales_array) / (current_day_in_int - 1))
        # print('Monthly Trend Per Day: ', monthly_trend_per_day)

        # trend_achievement = str(round((sum(final_sales_array)/monthly_trend)*100,1))
        # print('Trend Achievement: ',trend_achievement)

        # final_target_day_wise = 0
        cumulative_target_that_needs_to_plot = []
        cumulative_trend_that_needs_to_plot = []
        for t_value in range(0, total_days + 1):
            final_target_day_wise = single_day_target * t_value
            final_trend_day_wise = monthly_trend_per_day * t_value
            cumulative_target_that_needs_to_plot.append(final_target_day_wise / 1000)
            cumulative_trend_that_needs_to_plot.append(final_trend_day_wise / 1000)
            # final_target_day_wise = 0
        # print('cumulative target from 0 to final day of the month : ', cumulative_target_that_needs_to_plot)
        # print('cumulative trend from 0 to final day of the month : ', cumulative_trend_that_needs_to_plot)

        # new_array_of_cumulative_sales = [0]
        # final = 0
        # for val in final_sales_array:
        #     # print(val)
        #     get_in = final_sales_array.index(val)
        #     # print(get_in)
        #     if get_in == 0:
        #         new_array_of_cumulative_sales.append(val / 1000)
        #     else:
        #         for i in range(0, get_in + 1):
        #             final = (final + final_sales_array[i]) / 1000
        #         new_array_of_cumulative_sales.append(final)
        #         final = 0

        series = pd.Series(final_sales_array)
        cumsum = series.cumsum()
        final_cumulative = cumsum.tolist()
        new_array_of_cumulative_sales = [0]

        for cum_value in final_cumulative:
            new_array_of_cumulative_sales.append(int(cum_value / 1000))

        # print('Cumulative sales list from 0 to current day of month : ', new_array_of_cumulative_sales)  #
        # --------------------------sales data

        # sys.exit()

        length_of_cumulative_target = range(len(cumulative_target_that_needs_to_plot))
        length_of_cumulative_sales = range(len(new_array_of_cumulative_sales))

        list_index_for_target = len(cumulative_target_that_needs_to_plot) - 1
        # print('index size for target : ', list_index_for_target)
        # sys.exit()

        list_index_for_sale = len(new_array_of_cumulative_sales) - 1
        # print('index size for sale : ', list_index_for_sale)
        # sys.exit()

        cumulative_achv_label = []
        for loop_value in range(1, list_index_for_sale + 1):
            cumulative_achv = str(round(
                (new_array_of_cumulative_sales[loop_value] / cumulative_target_that_needs_to_plot[loop_value]) * 100,
                1)) + '%'
            cumulative_achv_label.append(cumulative_achv)

        # print('cumulative achievement list: ',cumulative_achv_label)

        for z in range(0, (total_days - list_index_for_sale)):
            cumulative_achv_label.append('')
        # print('cumulative achv with Faka values: ',cumulative_achv_label)

        days_list = np.arange(1, total_days + 1, 1)
        # print('days list: ',days_list)

        new_generated_label_list = []
        for new_generated_label_value in range(0, total_days):
            new_generated_label_list.append(
                str(days_list[new_generated_label_value]) + ' (' + str(cumulative_achv_label[
                                                                           new_generated_label_value]) + ')')

        fig, ax = plt.subplots(figsize=(9.6, 4.8))

        plt.fill_between(length_of_cumulative_target, cumulative_trend_that_needs_to_plot, color="green", alpha=.15)
        plt.fill_between(length_of_cumulative_sales, new_array_of_cumulative_sales, color="green", alpha=1)
        plt.plot(length_of_cumulative_target, cumulative_target_that_needs_to_plot, color="red", linewidth=3,
                 linestyle="-")

        # # Trend val with percent
        plt.text(list_index_for_target, cumulative_trend_that_needs_to_plot[list_index_for_target],
                 format(int(cumulative_trend_that_needs_to_plot[list_index_for_target]), ',') + 'K\n('
                 + str(round((cumulative_trend_that_needs_to_plot[list_index_for_target] /
                              cumulative_target_that_needs_to_plot[list_index_for_target]) * 100, 1)) + '%)',
                 color='black', fontsize=10, fontweight='bold')

        # # Trend scatter point
        plt.scatter(list_index_for_target, cumulative_trend_that_needs_to_plot[list_index_for_target], s=60,
                    facecolors='green', edgecolors='white')

        # # Target value
        plt.text(list_index_for_sale - 1, cumulative_target_that_needs_to_plot[list_index_for_sale] * 1.2,
                 format(int(cumulative_target_that_needs_to_plot[list_index_for_sale]), ',') + 'K',
                 color='red', fontsize=10, fontweight='bold', rotation=20)

        # # MTD Target point
        plt.scatter(list_index_for_sale, cumulative_target_that_needs_to_plot[list_index_for_sale], s=60,
                    facecolors='red',
                    edgecolors='white')

        # # Sales value 
        plt.text(list_index_for_sale + .2, new_array_of_cumulative_sales[list_index_for_sale] * .3,
                 format(int(new_array_of_cumulative_sales[list_index_for_sale]), ',') + 'K',
                 color='green', fontsize=10, fontweight='bold')

        # plt.scatter(list_index_for_sale, new_array_of_cumulative_sales[list_index_for_sale], s=60, facecolors='#113d3c',
        #             edgecolors='white')

        # # Final Months Target
        plt.text(list_index_for_target - 1, cumulative_target_that_needs_to_plot[list_index_for_target] + 2,
                 format(round(cumulative_target_that_needs_to_plot[list_index_for_target]), ',') + 'K',
                 color='red', fontsize=10, fontweight='bold')

        # # Months Target Point
        plt.scatter(list_index_for_target, cumulative_target_that_needs_to_plot[list_index_for_target], s=60,
                    facecolors='red', edgecolors='white')

        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)

        plt.xticks(np.arange(1, total_days + 1, 1), new_generated_label_list, fontsize=12, rotation=90)
        plt.xlabel('Days', color='black', fontsize=12, fontweight='bold')
        plt.ylabel('Amount(K)', color='black', fontsize=12, fontweight='bold')

        date = datetime.datetime.now()
        month = date.strftime("%b")
        year = date.strftime("%y")

        plt.title('Day wise Cumulative MTD Target VS Sales (' + str(month) + "' " + str(year) + ')', color='black', \
                  fontweight='bold', fontsize=16)

        plt.legend(['Target', 'Trend with Achiv%', 'Sales'], loc='upper left')
        # print(max(cumulative_target_that_needs_to_plot))
        plt.yticks(
            np.arange(0, max(cumulative_target_that_needs_to_plot) + 0.4 * max(cumulative_target_that_needs_to_plot),
                      max(cumulative_target_that_needs_to_plot) / 5))
        plt.tight_layout()

        plt.savefig("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
        # plt.show()
        print('4. Cumulative day wise target sales generated')

    except:
        plt.subplots(figsize=(9.6, 4.8))
        plt.text(0.2, 0.5, 'Sorry this chart could not get generated.', color='red', \
                 fontsize=14)
        plt.xlabel('Days', color='black', fontsize=14, fontweight='bold')
        plt.ylabel('Amount(K)', color='black', fontsize=10, fontweight='bold')
        plt.title('Cumulative Day Wise Stock & Sales', color='black', fontweight='bold', fontsize=12)

        plt.tight_layout()
        plt.savefig("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
        # plt.show()
        print('4. Error Cumulative day wise target sales generated')
