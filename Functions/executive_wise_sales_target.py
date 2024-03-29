import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import Functions.db_connection as dbc


def executive_sales_target(name):
    try:
        executive_target_sales_df = pd.read_sql_query("""
                    Declare @CurrentMonth NVARCHAR(MAX);
                    Declare @DaysInMonth NVARCHAR(MAX);
                    Declare @DaysInMonthtilltoday NVARCHAR(MAX);
                    SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                    SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
                    SET @DaysInMonthtilltoday = right(convert(varchar(8), GETDATE(),112),2)

                    select exe_sales.ExecutiveName as ExecutiveName,exe_sales.shortname as shortname,exe_sales.ItemSales as ItemSales,isnull(exe_target.MTDTargetValue, 0) as MTDTargetValue from
                    (select CP01 as ExecutiveName,b.[Executive ShortName] as shortname,cast(isnull(sum(EXTINVMISC),
                    0)/1000 as int) as ItemSales from OESalesDetails
                    left join PRINFOSKF
                    on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
                    right join
                    (select * from GPMExecutive_ShortName) as b
                    on b.[ExecutiveName]=PRINFOSKF.cp01
                    where left(TRANSDATE,10) between convert(varchar(10),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()-1), 0),112)
                                    and convert(varchar(10),getdate(), 112)
                    and PRINFOSKF.GPMNAME like ?
                    and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name like ?)
                    group by CP01,b.[Executive ShortName]) as exe_sales
                    left join
                    (select CP01 as ExecutiveName, cast(isnull((sum(TRGVAL)/@DaysInMonth)*@DaysInMonthtilltoday,0)/1000 as int) as MTDTargetValue
                    from PRINFOSKF 
                    left join ARCSECONDARY.dbo.PRODUCT_WISE_TRG
                    on PRODUCT_WISE_TRG.ITEM = PRINFOSKF.ITEMNO
                    where YRM = CONVERT(varchar(6), dateAdd(month,0,getdate()), 
                    112) and GPMNAME like ?
                    and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name like ?)
                    group by CP01) as exe_target
                    on exe_sales.ExecutiveName = exe_target.ExecutiveName
                    order by exe_sales.ItemSales desc
                     """, dbc.connection, params=(name, name, name, name))

        Executive_name = executive_target_sales_df['ExecutiveName'].tolist()
        Executive_target = executive_target_sales_df['MTDTargetValue'].tolist()

        # print('Executive target list = ', Executive_target)

        def Dr_Replace(customer_name):
            md_replaced_result = [sub.replace('Dr. ', '') for sub in customer_name]
            return md_replaced_result

        def Mr_Replace(customer_name):
            md_replaced_result = [sub.replace('Mr. ', '') for sub in customer_name]
            return md_replaced_result

        def MS_Replace(customer_name):
            md_replaced_result = [sub.replace('Ms. ', '') for sub in customer_name]
            return md_replaced_result

        new_name = Dr_Replace(Executive_name)
        new_name2 = Mr_Replace(new_name)
        MS_Replace(new_name2)

        # print(executive_target_df)
        Executive_sale = executive_target_sales_df['ItemSales'].tolist()
        short_name = executive_target_sales_df['shortname'].tolist()
        # print(Executive_sale)
        # print(short_name)

        achievement_list = []
        for x, y in zip(Executive_sale, Executive_target):
            try:
                achv = (x / y) * 100
                achievement_list.append(achv)
            except:
                achv = 0
                achievement_list.append(achv)
        # print("Achv list", achievement_list)

        new_label_list = []
        for x, y in zip(short_name, achievement_list):
            new_label = str(x) + ' (' + str(round(y)) + '%)'
            new_label_list.append(new_label)
        # print("new label list= ", new_label_list)
        # print("Executive sales = ", Executive_sale)

        # z = range(0, len(new_label_list))
        # print(range(0, len(new_label_list)))
        plt.subplots(figsize=(9.6, 4.8))

        colors = ['#3F93D0']
        bars = plt.bar(new_label_list, Executive_sale, color=colors, width=.6)

        plt.title("Executive wise MTD Target & Sales", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Executive', fontsize=12, color='black', fontweight='bold')
        plt.xticks(new_label_list, rotation=45)
        plt.ylabel('Amount (K)', fontsize=12, color='black', fontweight='bold')

        plt.rcParams['text.color'] = 'black'

        for bar, achv in zip(bars, Executive_sale):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',') + 'K'  # + '\n' + str(achv) + '%'
            plt.text(bar.get_x() + .45 - wval / 2, yval / 2, data)

        plt.plot(new_label_list, Executive_target, 'o-', color='Red')

        if max(Executive_target) > 1:
            plt.yticks(
                np.arange(0, int(max(Executive_target) + 0.9 * max(Executive_target)), int(max(Executive_target) / 5)))

        for i, j in zip(new_label_list, Executive_target):
            label = format(int(j), ',') + 'K'
            plt.annotate(label, (i, j), textcoords="offset points", xytext=(0, 4), ha='center')

        plt.legend(['Target', 'Sales'])
        plt.tight_layout()
        # plt.show()

        plt.savefig('./Images/executive_wise_target_vs_sold_quantity.png')
        print('5. Executive figure generated \n')

    except:
        plt.subplots(figsize=(9.6, 4.8))
        plt.title("Executive Wise MTD Target & Sales", fontsize=12, color='black', fontweight='bold')
        plt.xlabel('Executive', fontsize=10, color='black', fontweight='bold')
        plt.ylabel('Sales Value', fontsize=10, color='black', fontweight='bold')

        plt.text(0.2, 0.4, 'Sorry, this chart could not get generated.', color='red', fontsize=16)
        # plt.legend(['Target', 'Sales'])
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/executive_wise_target_vs_sold_quantity.png')
        print('5. Executive figure Not generated \n')
