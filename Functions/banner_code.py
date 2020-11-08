from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime
import pandas as pd
import path as dir
import pyodbc as db

con = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

def banner():
    date = datetime.today()
    day = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")
    date = datetime.today()
    x = dd.datetime.now()
    day = str(date.day) + '-' + str(x.strftime("%b")) + '-' + str(date.year)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")

    conn = db.connect('DRIVER={SQL Server};'
                          'SERVER=137.116.139.217;'
                          'DATABASE=ARCHIVESKF;'
                          'UID=sa;'
                          'PWD=erp@123;')

    date_time = pd.read_sql_query(
        """select max(datetime) as uptime from OESalesDetails
        where LEFT(TRANSDATE, 8) = convert(varchar(8), getdate(), 112)""", conn)

    datetime_list = date_time['uptime'].to_list()
    temp_var = datetime_list[0]
    con_to_str = str(temp_var)
    hour = str(con_to_str[11:13])
    min = str(con_to_str[14:16])

    def convertTime(hour, min):
        h, m = (int(hour), int(min))

        postfix = ' AM'

        if h > 12:
            postfix = ' PM'
            h -= 12
        return '{}:{:02d}{}'.format(h or 12, m, postfix)

    img = Image.open(dir.get_directory() + "/images/new_ai.png")
    update_time = ImageDraw.Draw(img)
    timestore = ImageDraw.Draw(img)
    tag = ImageDraw.Draw(img)
    branch = ImageDraw.Draw(img)
    font = ImageFont.truetype(dir.get_directory() + "/images/Stencil_Regular.ttf", 40, encoding="unic")
    name_font = ImageFont.truetype(dir.get_directory() + "/images/Lobster-Regular.ttf", 30, encoding="unic")
    font1 = ImageFont.truetype(dir.get_directory() + "/images/ROCK.ttf", 30, encoding="unic")
    font2 = ImageFont.truetype(dir.get_directory() + "/images/ROCK.ttf", 18, encoding="unic")
    report_name = 'GPM '
    # n = gpm_name
    tag.text((25, 8), 'SK+F', (255, 255, 255), font=font)
    branch.text((25, 150), report_name + "Sales and Stock Report", (255, 209, 0), font=font1)
    # name.text((25, 180), n , (255, 255, 255), font=name_font)
    timestore.text((25, 200),time + "\n" + day, (255, 255, 255), font=font2)
    timestore.text((705, 200), "Last Update Time: " + str(convertTime(hour, min)), (33,246,7), font=font2)
    img.save(dir.get_directory() + "/images/banner_ai.png")
    # img.show()
    print("Banner Created")