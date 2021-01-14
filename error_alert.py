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
# import Functions.read_gpm_info as gpm
import path as d


def send_error_msg(name):
    # if (to == ['nawajesh@skf.transcombd.com', '']):
    #     to = ['rejaul.islam@transcombd.com', '']
    #     cc = ['', '']
    #     bcc = ['', '']
    #     print('Report Sending to = ', to)

    msgRoot = MIMEMultipart('related')
    me = 'erp-bi.service@transcombd.com'

    to = ['rejaul.islam@transcombd.com', '']
    cc = ['', '']
    bcc = ['', '']

    recipient = to + cc + bcc

    date = datetime.today()
    today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")

    # # ------------ Group email --------------------
    subject = "Failed GPM SKF" + today
    email_server_host = 'mail.transcombd.com'
    port = 25

    msgRoot['From'] = me
    msgRoot['To'] = ', '.join(to)
    msgRoot['Cc'] = ', '.join(cc)
    msgRoot['Bcc'] = ', '.join(bcc)
    msgRoot['Subject'] = subject

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText("""
                                     <h2>Failed to Generate [ """ + name + """ ] Branch Report </h2>
                                      
                                    """, 'html')
    msgAlternative.attach(msgText)

    # # ----------- Finally send mail and close server connection -----
    server = smtplib.SMTP(email_server_host, port)
    server.ehlo()
    print('\n-----------------')
    print('Sending Error Mail')
    server.sendmail(me, recipient, msgRoot.as_string())
    print('Mail Send')
    print('-------------------')
    server.close()
