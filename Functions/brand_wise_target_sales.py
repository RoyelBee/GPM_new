import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def brand_wise_target_sales():
    try:
        df = pd.read_excel('./Data/gpm_data.xlsx')
        read_file_for_all_data = df[df['MTD Sales Target'] != 0]
        read_file_for_all_data = read_file_for_all_data.sort_values('Actual Sales MTD', ascending=False)
        brand = read_file_for_all_data['BRAND'].to_list()
        mtd_sales = read_file_for_all_data['Actual Sales MTD'].to_list()
        # mtd_sales=mtd_sales[:10]
        new_list = range(len(mtd_sales))
        mtd_target = read_file_for_all_data['MTD Sales Target'].to_list()
        # mtd_target = mtd_target[:10]
        mtd_achivemet = read_file_for_all_data['MTD Sales Acv'].to_list()
        # mtd_achivemet = mtd_achivemet[:10]

        plt.subplots(figsize=(18, 6))
        colors = ['#3F93D0']

        new_label_list = []
        for x, y in zip(brand, mtd_achivemet):
            new_label = str(x) + ' (' + str(round(y)) + '%)'
            new_label_list.append(new_label)

        bars = plt.bar(new_list, mtd_sales, color=colors, width=.75)

        plt.title("Brand wise Target VS Sold Quantity", fontsize=16, color='black', fontweight='bold')
        plt.xlabel('Brand', fontsize=12, color='black', fontweight='bold')
        plt.xticks(new_list, new_label_list, rotation=90, fontsize=8)
        plt.ylabel('Quantity(K)', fontsize=12, color='black', fontweight='bold')






        # plt.rcParams['text.color'] = 'black'
        #
        for bar, achv in zip(bars, mtd_achivemet):
            yval = bar.get_height()
            wval = bar.get_width()
            data = format(int(yval / 1000), ',') # +'K(' + str(achv) + '%)'
            plt.text(bar.get_x() + .5 - wval / 2, yval * .5, data, fontsize=8, rotation=90)  # - wval / 2

        lines = plt.plot(new_list, mtd_target, 'o-', color='Red')
        #

        for i, j in zip(new_list, mtd_target):
            label = format(int(j / 1000), ',')
            plt.annotate(str(label) + 'K', (i, j), rotation=90, textcoords="offset points", xytext=(0, 15),
                         ha='center', fontsize=8)


        plt.legend(['Target', 'Sales & Achiv%'], loc='best', fontsize='14')
        plt.tight_layout()
        plt.savefig('./Images/brand_wise_target_vs_sold_quantity.png')
        print('6. Brand Figure generated \n')

    except:

        fig, ax = plt.subplots(figsize=(9.6, 4.8))
        plt.title("Brand wise Target VS Sold Quantity", fontsize=16, color='black', fontweight='bold')
        plt.text(0.2, 0.5, 'Due to target unavailability the chart could not get generated.', color='red', fontsize=14)
        plt.xlabel('Brand', fontsize=14, color='black', fontweight='bold')
        plt.ylabel('Sales', fontsize=14, color='black', fontweight='bold')
        # plt.legend(['Target', 'Sales with Ach%'], loc='best', fontsize='14')

        plt.tight_layout()
        # plt.show()
        plt.savefig('./Images/brand_wise_target_vs_sold_quantity.png')
        print('6. exception for Brand Figure generated \n')
