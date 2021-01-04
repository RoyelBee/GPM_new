import datetime
import smtplib
from _datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import Functions.design_report_layout as layout
import path as d
import time
import Functions.read_gpm_info as gpm

msgRoot = MIMEMultipart('related')

me = 'erp-bi.service@transcombd.com'
to = ['', 'rejaul.islam@transcombd.com']
cc = ['', '']
bcc = ['', '']

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

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# # We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText("""
                            hello there 
                        """, 'html')

msgAlternative.attach(msgText)

# --- Read Banner Images
# fp = open(d.get_directory() + '/images/banner_ai.png', 'rb')
# banner_ai = MIMEImage(fp.read())
# fp.close()
# banner_ai.add_header('Content-ID', '<banner_ai>')
# msgRoot.attach(banner_ai)

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
