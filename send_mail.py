import datetime
import os
import smtplib
from _datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import Functions.design_report_layout as layout
import pandas as pd
import numpy as np
import path as d
import xlsxwriter


def send_mail(gpm_name):
    print('This project has 17 KPI, It takes time to generate. Keep patience.\n')

    import Functions.banner_code as ban
    import Functions.generate_data as gdata
    import Functions.dashboard as dash
    import Functions.cumulative_target_sales as cm
    import Functions.executive_wise_sales_target as ex
    import Functions.brand_wise_target_sales as b
    # import Functions.stock_aging_days as aging
    import Functions.brand_wise_aging_information_bar as brand_bar
    import Functions.SKU_wise_aging_information_bar as SKU_bar
    import Functions.quantity_wise_aging_information_bar as quantity_bar
    import Functions.branch_wise_stock_aging as branch_stock_aging
    import Functions.item_wise_stock_days_data as item_stock_days_data
    import Functions.branch_stock_summery_data as bsdata
    import Functions.arranging_the_column_size as acs

    # ban.banner(gpm_name) # 01
    # gdata.GenerateReport(gpm_name) # 02
    # dash.dash_kpi_generator(gpm_name) # 03
    # cm.cumulative_target_sales(gpm_name) # 4
    # ex.executive_sales_target(gpm_name)  # 5
    # b.brand_wise_target_sales()  # 6
    # # # aging.stock_aging_chart(gpm_name) # 7
    # brand_bar.stock_aging_chart(gpm_name)#7.1
    # SKU_bar.stock_aging_chart(gpm_name)#7.2
    # quantity_bar.stock_aging_chart(gpm_name)#7.3
    # item_stock_days_data.create_item_wise_stock_days_data() # 8
    # bsdata.branch_stock_summery_data() # 9
    # branch_stock_aging.get_branch_aging_stock_status(gpm_name) # 10
    # acs.dataFormating()

    ## 11 to 17 KPI are comes from "design_report_layout.py" file in ascending order.


    # # --------- Add Image Border ---------------------------------------
    # from PIL import Image
    # da = Image.open("./Images/dashboard.png")
    # imageSize = Image.new('RGB', (962, 110))
    # imageSize.paste(da, (1, 0))
    # imageSize.save("./Images/dashboard.png")
    #
    # kpi1 = Image.open("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
    # imageSize = Image.new('RGB', (962, 481))
    # imageSize.paste(kpi1, (1, 0))
    # imageSize.save("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
    # #
    # kpi2 = Image.open("./Images/executive_wise_target_vs_sold_quantity.png")
    # imageSize = Image.new('RGB', (962, 481))
    # imageSize.paste(kpi2, (1, 0))
    # imageSize.save("./Images/executive_wise_target_vs_sold_quantity.png")
    # #
    # kpi3 = Image.open("./Images/brand_wise_target_vs_sold_quantity.png")
    # imageSize = Image.new('RGB', (1802, 601))
    # imageSize.paste(kpi3, (1, 0))
    # imageSize.save("./Images/brand_wise_target_vs_sold_quantity.png")
    # #
    # kpi4 = Image.open("./Images/aging_stock_information.png")
    # imageSize = Image.new('RGB', (962, 481))
    # imageSize.paste(kpi4, (1, 0))
    # imageSize.save("./Images/aging_stock_information.png")
    # kpi7_1 = Image.open("./Images/brand_wise_aging_stock_information.png")
    # kpi7_2 = Image.open("./Images/SKU_wise_aging_stock_information.png")
    # kpi7_3 = Image.open("./Images/Quantity_wise_aging_stock_information.png")
    # imageSize = Image.new('RGB', (1804, 481))
    # imageSize.paste(kpi7_1, (1, 0))
    # imageSize.paste(kpi7_2, (602, 0))
    # imageSize.paste(kpi7_3, (1203, 0))
    # imageSize.save("./Images/aging_stock_information.png")


    # # ------------- HTML generating section ------------------------------
    # data = pd.read_excel('./Data/html_data_Sales_and_Stock.xlsx')
    #
    # if data.empty:
    #     print('No data for print')
    # else:
    #     print('Layout Generating')
    #     layout.generate_layout(gpm_name)

    # to = gpm.getGPMEmail(gpm_name)
    #
    # if (to == ['nawajesh@skf.transcombd.com', '']):
    #     to = ['rejaul.islam@transcombd.com', '']
    #     cc = ['', '']
    #     bcc = ['', '']
    #     print('Report Sending to = ', to)

    to = ['biswascma@yahoo.com', 'yakub@transcombd.com', 'zubair.transcom@gmail.com']
    cc = ['', '']
    bcc = ['rejaul.islam@transcombd.com', 'rafiul.ramjan@transcombd.com']

    msgRoot = MIMEMultipart('related')
    me = 'erp-bi.service@transcombd.com'

    # to = to
    # cc = ['biswascma@yahoo.com', 'yakub@transcombd.com', 'zubair.transcom@gmail.com']
    # bcc = ['rejaul.islam@transcombd.com', 'aftab.uddin@transcombd.com', 'fazle.rabby@transcombd.com']

    recipient = to + cc + bcc

    date = datetime.today()
    today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")

    # # ------------ Group email -------------------------
    subject = "Brand Wise Sales and Stock Report " + today
    email_server_host = 'mail.transcombd.com'
    port = 25

    msgRoot['From'] = me
    msgRoot['To'] = ', '.join(to)
    msgRoot['Cc'] = ', '.join(cc)
    msgRoot['Bcc'] = ', '.join(bcc)
    msgRoot['Subject'] = subject

    # msgRoot['to'] = recipient
    # msgRoot['from'] = me
    # msgRoot['subject'] = subject

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText("""
                            """ + layout.generate_layout(gpm_name) + """ 
                        """, 'html')

    msgAlternative.attach(msgText)

    # --- Read Banner Images
    fp = open(d.get_directory() + '/images/banner_ai.png', 'rb')
    banner_ai = MIMEImage(fp.read())
    fp.close()
    banner_ai.add_header('Content-ID', '<banner_ai>')
    msgRoot.attach(banner_ai)

    # --- Read Dashboard KPI Images
    fp = open(d.get_directory() + '/images/aging_stock_information.png', 'rb')
    aging = MIMEImage(fp.read())
    fp.close()
    aging.add_header('Content-ID', '<aging>')
    msgRoot.attach(aging)

    # --- Read Dashboard KPI Images
    fp = open(d.get_directory() + '/images/dashboard.png', 'rb')
    dash = MIMEImage(fp.read())
    fp.close()
    dash.add_header('Content-ID', '<dash>')
    msgRoot.attach(dash)

    # --- Read Cumulative Target & Sales Images
    fp = open(d.get_directory() + '/images/Cumulative_Day_Wise_Target_vs_Sales.png', 'rb')
    cm = MIMEImage(fp.read())
    fp.close()
    cm.add_header('Content-ID', '<cm>')
    msgRoot.attach(cm)

    # --- Read Cumulative Target & Sales Images
    fp = open(d.get_directory() + '/images/executive_wise_target_vs_sold_quantity.png', 'rb')
    executive = MIMEImage(fp.read())
    fp.close()
    executive.add_header('Content-ID', '<executive>')
    msgRoot.attach(executive)

    # --- Read Cumulative Target & Sales Images
    fp = open(d.get_directory() + '/images/brand_wise_target_vs_sold_quantity.png', 'rb')
    brand = MIMEImage(fp.read())
    fp.close()
    brand.add_header('Content-ID', '<brand>')
    msgRoot.attach(brand)

    # # 1. Add GPM branch wise aging Stock dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/branch_wise_aging_stock_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 2. Add GPM branch wise stock status dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/branch_wise_stock_status_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 3. Add GPM item wise yesterday sales dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/item_wise_yesterday_sales_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 4. Add GPM last three month no sales dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/NoSales_last_three_month_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 5. Add GPM No Stock last three month dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/NoStock_last_three_month_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 6. Add GPM yesterday no sales dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/yesterday_no_sales_copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)
    #
    # # 7. Add GPM yesterday no sales dataset
    # part = MIMEBase('application', "octet-stream")
    # file_location = d.get_directory() + '/Data/branch_wise_detailed_data_Sales_and_Stock-Copy.xlsx'
    # filename = os.path.basename(file_location)
    # attachment = open(file_location, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msgRoot.attach(part)

    # #----------- Finally send mail and close server connection -----
    server = smtplib.SMTP(email_server_host, port)
    server.ehlo()
    print('\n-----------------')
    print('Sending Mail')
    server.sendmail(me, recipient, msgRoot.as_string())
    print('Mail Send')
    print('-------------------')
    server.close()

    # # Html_file = open("testinghtml.html", "w")
    # # Html_file.write(layout.generate_layout(gpm_name))
    # # Html_file.close()
