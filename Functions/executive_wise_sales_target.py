import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
import numpy as np

name = 'Dr. Shafiqul Mawla'

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

def executive_sales_target(name):
    try:
        executive_target_df = pd.read_sql_query("""
                                            Declare @CurrentMonth NVARCHAR(MAX);
                                            Declare @DaysInMonth NVARCHAR(MAX);
                                            Declare @DaysInMonthtilltoday NVARCHAR(MAX);
                                            SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                                            SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
                                            SET @DaysInMonthtilltoday = right(convert(varchar(8), GETDATE(),112),2)
                                            select CP01 as ExecutiveName, isnull((sum(QTY)/@DaysInMonth)*@DaysInMonthtilltoday,0) as MTDTargetQty
                                            from PRINFOSKF 
                                            left join ARCSECONDARY.dbo.RfieldForceProductTRG
                                            on RfieldForceProductTRG.ITEMNO = PRINFOSKF.ITEMNO
                                            where YEARMONTH = CONVERT(varchar(6), dateAdd(month,0,getdate()), 
                                            112) and GPMNAME like ?
                                            group by CP01
                                            order by CP01 asc """, connection,params={name})

        Executive_name = executive_target_df['ExecutiveName'].tolist()
        Executive_target = executive_target_df['MTDTargetQty'].tolist()
        # print(Executive_name)
        # print(Executive_target)

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
        new_name3 = MS_Replace(new_name2)
        # print(new_name3)

        executive_sales_df = pd.read_sql_query("""select CP01 as ExecutiveName, isnull(sum(QTYSHIPPED),0) as ItemSales from OESalesDetails
                                left join PRINFOSKF
                                on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
                                where left(TRANSDATE,10) between convert(varchar(10),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()-1), 0),112)
                                                and convert(varchar(10),getdate(), 112)
                                and PRINFOSKF.GPMNAME like ?
                                group by CP01
                                order by CP01 asc""", connection,params={name})

        Executive_sale = executive_sales_df['ItemSales'].tolist()
        # print(Executive_sale)

        fig, ax = plt.subplots(figsize=(9.6, 4.8))

        colors = ['#3F93D0']
        bars = plt.bar(new_name3, Executive_sale, color=colors, width=.4)

        plt.title("Executive Wise MTD Target & Sales", fontsize=12, color='black', fontweight='bold')
        plt.xlabel('Executive', fontsize=10, color='black', fontweight='bold')
        plt.xticks(new_name3, rotation=90)
        plt.ylabel('Sales', fontsize=10, color='black', fontweight='bold')

        plt.rcParams['text.color'] = 'black'

        for bar, achv in zip(bars, Executive_sale):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',') #+ '\n' + str(achv) + '%'
            plt.text(bar.get_x(), yval, data)

        lines = plt.plot(new_name3, Executive_target, 'o-', color='Red')
        plt.yticks(np.arange(0, max(Executive_target) + 0.9 * max(Executive_target), max(Executive_target) / 5))
        for i, j in zip(new_name3, Executive_target):
            label = format(int(j), ',')
            plt.annotate(label, (i, j), textcoords="offset points", xytext=(0, 4), ha='center', rotation=45)

        # print(mtd_achivemet)
        plt.legend(['Target','Sales'])
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/executive_wise_target_vs_sold_quantity.png')
        print('Executive figure generated')
    except:
        fig, ax = plt.subplots(figsize=(9.6, 4.8))
        plt.title("Executive Wise MTD Target & Sales", fontsize=12, color='black', fontweight='bold')
        plt.xlabel('Executive', fontsize=10, color='black', fontweight='bold')
        plt.ylabel('Sales', fontsize=10, color='black', fontweight='bold')

        plt.text(0.2, 0.5, 'Due to target unavailability the chart could not get generated.', color='red', fontsize=14)
        plt.legend(['Target', 'Sales'])
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/executive_wise_target_vs_sold_quantity.png')
        print('Executive figure generated')
