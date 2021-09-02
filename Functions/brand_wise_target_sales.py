import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def brand_wise_target_sales():
    try:
        cols = ['BRAND', 'MTD Sales Target Value', 'Actual Sales MTD Value']
        df = pd.read_excel('./Data/gpm_data.xlsx', usecols=cols)
        # df = df[df['MTD Sales Target Value'] != 0]

        data = df.groupby('BRAND')['MTD Sales Target Value', 'Actual Sales MTD Value'].sum()
        # print(data)

        # data['Brand'] = data['BRAND']
        MTD_Achivment = (data['Actual Sales MTD Value'] / data['MTD Sales Target Value']) * 100
        data['MTD Sales Acv'] = MTD_Achivment
        data.to_csv('./Data/brand_wise_target_sales.csv', index=True)
        d = data.sort_values(by='Actual Sales MTD Value', ascending=False)
        d.to_csv('./Data/brand_wise_target_sales.csv', index=True)

        data = pd.read_csv('./Data/brand_wise_target_sales.csv')
        brand = data['BRAND'].to_list()
        mtd_sales = data['Actual Sales MTD Value'].to_list()
        # mtd_sales=mtd_sales[:10]
        new_list = range(len(mtd_sales))
        mtd_target = data['MTD Sales Target Value'].to_list()
        # mtd_target = mtd_target[:10]
        mtd_achivemet = data['MTD Sales Acv'].to_list()
        # mtd_achivemet = mtd_achivemet[:10]
        # print(mtd_achivemet)
        plt.subplots(figsize=(18, 6))

        new_label_list = []
        for x, y in zip(brand, mtd_achivemet):
            try:
                new_label = str(x) + ' (' + str(round(y)) + '%)'
                new_label_list.append(new_label)
            except:
                new_label = str(x) + '(0 %)'
                new_label_list.append(new_label)

        # print(new_list)
        # print(new_label_list)

        bars = plt.bar(new_list, mtd_sales, color='#1cbceb', width=.75)

        plt.title("Brand wise MTD Target VS Sold Value", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Brands', fontsize=12, color='black', fontweight='bold')
        plt.xticks(new_list, new_label_list, rotation=90, fontsize=9)
        plt.ylabel('Amount (K)', fontsize=12, color='black', fontweight='bold')

        for bar, achv in zip(bars, mtd_achivemet):
            yval = bar.get_height()
            wval = bar.get_width()
            data = str(float("{:.1f}".format(yval / 1000, ','))) + 'K'
            plt.text(bar.get_x() + .6 - wval / 2, yval * .5, data, color='#000543', fontweight='bold', fontsize=8)

        plt.plot(new_list, mtd_target, 'o-', color='Red')

        for i, j in zip(new_list, mtd_target):
            label = str(float("{:.1f}".format(j / 1000, ',')))
            plt.annotate(str(label) + 'K', (i, j), rotation=90, textcoords="offset points", xytext=(0, 15),
                         ha='center', fontsize=8)

        plt.legend(['Target', 'Sales'], loc='best', fontsize='14')
        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/brand_wise_target_vs_sold_quantity.png')
        print('7. Brand Figure generated \n')

    except:

        plt.subplots(figsize=(18, 6))
        plt.title("Brand wise MTD Target VS Sold Quantity", fontsize=16, color='black', fontweight='bold')
        plt.text(0.2, 0.5, 'Due to target unavailability the chart could not generated.', color='red', fontsize=14)
        plt.xlabel('Brand', fontsize=14, color='black', fontweight='bold')
        plt.ylabel('Amount (K)', fontsize=14, color='black', fontweight='bold')
        # plt.legend(['Target', 'Sales with Ach%'], loc='best', fontsize='14')

        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/brand_wise_target_vs_sold_quantity.png')
        print('7. exception for Brand Figure generated \n')
