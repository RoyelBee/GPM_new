
import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
import numpy as np
import sys

# name ='Mr. A. K. M. Nawajesh Hossain'
#
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

def stock_aging_chart(name):
    try:
        executive_target_df = pd.read_sql_query("""
                Select Sum(case when AGEING='Within 15 Days' then TotalStock Else 0 end) 'Within 15 Days'  
                ,Sum(case when AGEING='Within 30 Days' then TotalStock Else 0 end) 'Within 30 Days'  
                ,Sum(case when AGEING='Within 60 Days' then TotalStock Else 0 end) 'Within 60 Days'  
                ,sum(case when AGEING='Within 90 Days' then TotalStock Else 0 end) 'Within 90 Days'  
                ,Sum(case when AGEING='Within 120 Days' then TotalStock Else 0 end) 'Within 120 Days'  
                ,Sum(case when AGEING='More Than 120 Days' then TotalStock Else 0 end) 'More Than 120 Days'  
                ,Sum(case when AGEING='More Than 1 Year' then TotalStock Else 0 end) 'More Than 1 Year'
                ,Sum(case when AGEING='Expired' then TotalStock Else 0 end) 'Expired'
                from 
                (select AGEING,SUM(QTYAVAIL) AS TotalStock  from 
                (select ITEMNO,AUDTORG,AGEING,QTYAVAIL,EXPIRYDATE from ICStockCurrent_Lot WHERE AUDTORG<>'SKFDAT') as T1
                LEFT JOIN
                (select ITEMNO,ITEMNAME,BRAND,PACKSIZE,GPMNAME from PRINFOSKF)as T2
                ON (T1.ITEMNO=T2.ITEMNO)
                WHERE T2.GPMNAME LIKE ?
                Group by AGEING)as T3
                 """, connection, params={name})

        fifteen_days = executive_target_df['Within 15 Days'].tolist()
        thirty_days = executive_target_df['Within 30 Days'].tolist()
        sixty_days = executive_target_df['Within 60 Days'].tolist()
        ninety_days = executive_target_df['Within 90 Days'].tolist()
        onetwenty_days = executive_target_df['More Than 120 Days'].tolist()
        one_year = executive_target_df['More Than 1 Year'].tolist()
        Expired = executive_target_df['Expired'].tolist()

        # print(fifteen_days[0])

        list_to_plot=[Expired[0], fifteen_days[0],thirty_days[0],sixty_days[0],ninety_days[0]]
        list_of_label=['Expired', 'Within 15 Days','Within 30 Days','Within 60 Days','Within 90 Days']
        # sys.exit()
        fig, ax = plt.subplots(figsize=(9.6, 4.8))

        colors = ['#933636', '#f40d0d', '#ff8600', '#e1e300', '#b2eb05']
        bars = plt.bar(list_of_label, list_to_plot, color=colors, width=.4)

        plt.title("Stock Aging Information", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Aging Days', fontsize=12, color='black', fontweight='bold')
        plt.xticks(list_of_label, rotation=90)
        plt.ylabel('Quantity', fontsize=12, color='black', fontweight='bold')

        plt.rcParams['text.color'] = 'black'

        for bar, achv in zip(bars, list_to_plot):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',')
            plt.text(bar.get_x()+wval/3, yval+5, data)

        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/aging_stock_information.png')
        print('7. Stock Aging figure generated \n')
    except:
        fig, ax = plt.subplots(figsize=(9.6, 4.8))
        plt.title("Executive Wise MTD Target & Sales", fontsize=12, color='black', fontweight='bold')
        plt.xlabel('Executive', fontsize=10, color='black', fontweight='bold')
        plt.ylabel('Sales', fontsize=10, color='black', fontweight='bold')

        plt.text(0.2, 0.5, 'Due to target unavailability the chart could not get generated.', color='red', fontsize=14)
        plt.legend(['Target', 'Sales'])
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/aging_stock_information.png')
        print('7. Error !!!! Stock Aging figure not generated\n')