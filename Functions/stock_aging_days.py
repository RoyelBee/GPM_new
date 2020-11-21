
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
                Select  
Sum(case when AGEING='Within 15 Days' then TotalStock Else 0 end) 'Within 15 Days' 
,Sum(case when AGEING='Within 15 Days' then TotalBrand Else 0 end) '15 Days Brand' 
,Sum(case when AGEING='Within 15 Days' then TotalSKU Else 0 end) '15 Days SKU' 
 
,Sum(case when AGEING='Within 30 Days' then TotalStock Else 0 end) 'Within 30 Days' 
,Sum(case when AGEING='Within 30 Days' then TotalBrand Else 0 end) '30 Days Brand'
,Sum(case when AGEING='Within 30 Days' then TotalSKU Else 0 end) '30 Days SKU' 

,Sum(case when AGEING='Within 60 Days' then TotalStock Else 0 end) 'Within 60 Days'
,Sum(case when AGEING='Within 60 Days' then TotalBrand Else 0 end) '60 Days Brand'
,Sum(case when AGEING='Within 60 Days' then TotalSKU Else 0 end) '60 Days SKU' 
  
,sum(case when AGEING='Within 90 Days' then TotalStock Else 0 end) 'Within 90 Days' 
,Sum(case when AGEING='Within 90 Days' then TotalBrand Else 0 end) '90 Days Brand'
,Sum(case when AGEING='Within 90 Days' then TotalSKU Else 0 end) '90 Days SKU' 
 
,Sum(case when AGEING='Within 120 Days' then TotalStock Else 0 end) 'Within 120 Days' 
,Sum(case when AGEING='Within 120 Days' then TotalBrand Else 0 end) '120 Days Brand'
,Sum(case when AGEING='Within 120 Days' then TotalSKU Else 0 end) '120 Days SKU'

,Sum(case when AGEING='More Than 120 Days' then TotalStock Else 0 end) 'More Than 120 Days'
,Sum(case when AGEING='More Than 120 Days' then TotalBrand Else 0 end) 'More Than 120 Days Brand'
,Sum(case when AGEING='More Than 120 Days' then TotalSKU Else 0 end) 'More Than 120 Days SKU'

 
,Sum(case when AGEING='More Than 1 Year' then TotalStock Else 0 end) 'More Than 1 Year'
,Sum(case when AGEING='More Than 1 Year' then TotalBrand Else 0 end) 'More Than 1 Year Brand'
,Sum(case when AGEING='More Than 1 Year' then TotalSKU Else 0 end) 'More Than 1 Year SKU'

,Sum(case when AGEING='Expired' then TotalStock Else 0 end) 'Expired'
,Sum(case when AGEING='Expired' then TotalBrand Else 0 end) 'Expired Brand'
,Sum(case when AGEING='Expired' then TotalSKU Else 0 end) 'Expired SKU'

from 
(select AGEING,count(distinct brand) as TotalBrand,count (distinct itemname) as TotalSKU, SUM(QTYAVAIL) AS TotalStock  from 
(select ITEMNO,AUDTORG,AGEING,QTYAVAIL,EXPIRYDATE from ICStockCurrent_Lot WHERE AUDTORG<>'SKFDAT') as T1
LEFT JOIN
(select ITEMNO,ITEMNAME,BRAND,PACKSIZE,GPMNAME from PRINFOSKF)as T2
ON (T1.ITEMNO=T2.ITEMNO)
WHERE T2.GPMNAME like ?
Group by  AGEING)as T3
                 """, connection, params={name})

        fifteen_days = executive_target_df['Within 15 Days'].tolist()
        thirty_days = executive_target_df['Within 30 Days'].tolist()
        sixty_days = executive_target_df['Within 60 Days'].tolist()
        ninety_days = executive_target_df['Within 90 Days'].tolist()
        # onetwenty_days = executive_target_df['More Than 120 Days'].tolist()
        # one_year = executive_target_df['More Than 1 Year'].tolist()
        Expired = executive_target_df['Expired'].tolist()

        # print(fifteen_days[0])
        fifteen_days_sku = executive_target_df['15 Days SKU'].tolist()
        thirty_days_sku = executive_target_df['30 Days SKU'].tolist()
        sixty_days_sku = executive_target_df['60 Days SKU'].tolist()
        ninety_days_sku = executive_target_df['90 Days SKU'].tolist()
        # onetwenty_days = executive_target_df['More Than 120 Days'].tolist()
        # one_year = executive_target_df['More Than 1 Year'].tolist()
        Expired_sku = executive_target_df['Expired SKU'].tolist()

        fifteen_days_brand = executive_target_df['15 Days Brand'].tolist()
        thirty_days_brand = executive_target_df['30 Days Brand'].tolist()
        sixty_days_brand = executive_target_df['60 Days Brand'].tolist()
        ninety_days_brand = executive_target_df['90 Days Brand'].tolist()
        # onetwenty_days = executive_target_df['More Than 120 Days'].tolist()
        # one_year = executive_target_df['More Than 1 Year'].tolist()
        Expired_brand = executive_target_df['Expired Brand'].tolist()

        list_to_plot=[Expired[0], fifteen_days[0],thirty_days[0],sixty_days[0],ninety_days[0]]
        list_to_sku = [Expired_sku[0], fifteen_days_sku[0],thirty_days_sku[0],sixty_days_sku[0],ninety_days_sku[0]]
        list_to_brand=[int(Expired_brand[0]), int(fifteen_days_brand[0]),int(thirty_days_brand[0]),int(sixty_days_brand[0]),int(ninety_days_brand[0])]

        # print(list_to_brand)
        # print(list_to_sku)
        # print(list_to_plot)

        list_of_label=['Expired', 'Within 15 Days','Within 30 Days','Within 60 Days','Within 90 Days']

        looping_range=np.arange(len(list_of_label))
        # sys.exit()
        fig, ax = plt.subplots(figsize=(9.6, 4.8))
        width=1

        # colors = ['#933636', '#f40d0d', '#ff8600', '#e1e300', '#b2eb05']
        colors = ['#ff8600', '#ff8600', '#ff8600', '#ff8600', '#ff8600']
        colors1 = ['#e1e300', '#e1e300', '#e1e300', '#e1e300', '#e1e300']
        colors2 = ['#b2eb05', '#b2eb05', '#b2eb05', '#b2eb05', '#b2eb05']

        bars = ax.bar(looping_range-width/4, list_to_brand, color=colors, width=.2)

        bars1 = plt.bar(looping_range, list_to_sku, color=colors1, width=.2)

        bars2 = plt.bar(looping_range+width/4, list_to_plot, color=colors2, width=.2)

        print("done")
        plt.title("Stock Aging Information", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Aging Days', fontsize=12, color='black', fontweight='bold')
        plt.xticks(looping_range,list_of_label, rotation=90)
        plt.ylabel('Quantity', fontsize=12, color='black', fontweight='bold')

        plt.rcParams['text.color'] = 'black'

        for bar, achv in zip(bars, list_to_brand):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',')
            plt.text(bar.get_x()+wval/3, yval+5, data)

        for bar, achv in zip(bars1, list_to_sku):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',')
            plt.text(bar.get_x()+wval/3, yval+5, data)

        for bar, achv in zip(bars2, list_to_plot):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval), ',')
            plt.text(bar.get_x()+wval/4, yval+5, data)

        ax.legend(["Brand","SKU","Quantity"])
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