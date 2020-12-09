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

,Sum(case when AGEING='Within 180 Days' then TotalStock Else 0 end) 'Within 180 Days' 
,Sum(case when AGEING='Within 180 Days' then TotalBrand Else 0 end) '180 Days Brand'
,Sum(case when AGEING='Within 180 Days' then TotalSKU Else 0 end) '180 Days SKU'

,Sum(case when AGEING='Within 210 Days' then TotalStock Else 0 end) 'Within 210 Days'
,Sum(case when AGEING='Within 210 Days' then TotalBrand Else 0 end) 'Within 210 Days Brand'
,Sum(case when AGEING='Within 210 Days' then TotalSKU Else 0 end) 'Within 210 Days SKU'

,Sum(case when AGEING='More Than 210 Days' then TotalStock Else 0 end) 'More Than 210 Days'
,Sum(case when AGEING='More Than 210 Days' then TotalBrand Else 0 end) 'More Than 210 Days Brand'
,Sum(case when AGEING='More Than 210 Days' then TotalSKU Else 0 end) 'More Than 210 Days SKU'


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


        fifteen_days_brand = executive_target_df['15 Days Brand'].tolist()
        thirty_days_brand = executive_target_df['30 Days Brand'].tolist()
        sixty_days_brand = executive_target_df['60 Days Brand'].tolist()
        ninety_days_brand = executive_target_df['90 Days Brand'].tolist()
        Expired_brand = executive_target_df['Expired Brand'].tolist()
        one_eighty_days_brand = executive_target_df['180 Days Brand'].tolist()
        two_ten_days_brand = executive_target_df['Within 210 Days Brand'].tolist()
        print(one_eighty_days_brand)

        list_to_brand = [int(Expired_brand[0]), int(fifteen_days_brand[0]), int(thirty_days_brand[0]),
                         int(sixty_days_brand[0]), int(ninety_days_brand[0]), int(one_eighty_days_brand[0]),
                         int(two_ten_days_brand[0])]
        total=sum(list_to_brand)

        list_of_label = ['Expired', '1 - 15 Days', '16 - 30 Days', '31 - 60 Days', '61 - 90 Days', '91 - 180 Days',
                         '181 - 210 Days']

        fig, ax = plt.subplots(figsize=(6, 4.8))
        width = 1

        # colors = ['yellow', 'orange', 'violet', '#DADADA', '#003f5c', '#665191', '#a05195', '#d45087', '#ff7c43',
        #           '#ffa600']
        colors = ['#933636', '#f40d0d', '#ff8600', '#e1e300', '#b2eb05', '#629B00', '#124B00']
        bars = plt.bar(list_of_label, height=list_to_brand, color=colors, width=.4)

        plt.title("Brand wise Stock Aging ("+str(total)+")", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Aging Days', fontsize=12, color='black', fontweight='bold')
        plt.xticks(list_of_label, rotation=90)
        plt.ylabel('Brand', fontsize=12, color='black', fontweight='bold')

        for bar in bars:
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval))
            plt.text((bar.get_x() + wval / 4), yval, data, fontweight='bold',rotation=30)
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/brand_wise_aging_stock_information.png')
        print('7.1 Brand wise Stock Aging figure generated ')


    except:
        fig, ax = plt.subplots(figsize=(6, 4.8))
        ax.title("Executive Wise MTD Target & Sales", fontsize=12, color='black', fontweight='bold')
        ax.xlabel('Executive', fontsize=10, color='black', fontweight='bold')
        ax.ylabel('Sales', fontsize=10, color='black', fontweight='bold')
        ax.text(0.2, 0.5, 'Due to target unavailability the chart could not get generated.', color='red', fontsize=14)
        ax.legend(['Target', 'Sales'])
        ax.tight_layout()
        print('7.1 Error !!!! brand wise Stock Aging figure not generated\n')