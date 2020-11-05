import pandas as pd
import pyodbc as db

# akhtar_data_df = pd.read_excel('brand_list/akhter.xlsx', sheet_name='Sheet1')
# # print(akhtar_data_df)
#
# name = akhtar_data_df['name'].iloc[0]
# emailAddress = akhtar_data_df['email'].iloc[0]
# branch = []
# total_brands = len(akhtar_data_df['brand'])

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')


def getGPMName(name):
    df = pd.read_sql_query(""" select Name, Email, count(brand) as TotalBrands from GPMBRAND
            where Name like ?
            group by Name, Email """, connection, params={name})
    name = df['Name'].iloc[0]
    return name


def getGPMEmail(name):
    df = pd.read_sql_query(""" select Name, Email, count(brand) as TotalBrands from GPMBRAND
            where Name like ?
            group by Name, Email""", connection, params={name})
    email = df['Email'].iloc[0]
    email_format = [email, '']
    brands = df['TotalBrands'].iloc[0]
    return email_format


def getGPMNumberofBrands(name):
    df = pd.read_sql_query(""" select Name, Email, count(brand) as TotalBrands from GPMBRAND
                where Name like ?
                group by Name, Email""", connection, params={name})

    brands = df['TotalBrands'].iloc[0]
    return brands


def getGPMNFullInfo(name):
    df = pd.read_sql_query(""" select Name, Email,Phone, Designation, count(brand) as TotalBrands from GPMBRAND
                where Name like ?
                group by Name, Email, Phone, Designation """, connection, params={name})
    name = str(df['Name'].iloc[0])
    email = str(df['Email'].iloc[0])
    phone = str(df['Phone'].iloc[0])
    designation = str(df['Designation'].iloc[0])
    brands = str(df['TotalBrands'].iloc[0])

    all = name + " || Designation : " + designation + " || Phone : " + phone + "  ||  Email : " + email
    return all


# print(getGPMEmail('Akhter'))
# print(getGPMNumberofBrands('Dr. Shafiqul Mawla'))

# print(getGPMNFullInfo('Mr. Rubaeadul Hasan Lashkar'))

# print(getGPMEmail('Mr. Mohammad Akhter Alam Khan'))