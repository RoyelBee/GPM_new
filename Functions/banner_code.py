from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime
import pandas as pd
import path as dir
import Functions.db_connection as dbc

def banner(name):
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


    df_designation = pd.read_sql_query(""" select Name, Designation from GPMBRAND
                    where Name like ?
                    group by Name,Designation """, dbc.connection, params={name})

    date_time = pd.read_sql_query(
            """ select convert(varchar, max(datetime),6) as [date],
            FORMAT(CAST(max(datetime) AS datetime), 'hh:mm tt') as [time]
            
            from OESalesDetails
            where LEFT(TRANSDATE, 8) = convert(varchar(8), getdate(), 112) """, dbc.connection)

    up_date = str(date_time["date"][0])

    up_time = date_time['time'][0]
    # print(type(up_date), type(up_time))

    #
    # im = Image.open(dir.get_directory() + '/Images/Person.png')
    # im = im.resize((120, 120));
    # bigsize = (im.size[0] * 10, im.size[1] * 10)
    # mask = Image.new('L', bigsize, 0)
    # draw = ImageDraw.Draw(mask)
    # draw.ellipse((0, 0) + bigsize, fill=255)
    # mask = mask.resize(im.size, Image.ANTIALIAS)
    # im.putalpha(mask)
    # background = Image.open(dir.get_directory() + '/Images/new_ai.png')
    # background.paste(im, (820, 70), im)
    # background.save(dir.get_directory() + '/images/overlap.png')



    img = Image.open(dir.get_directory() + "/Images/new_ai.png")
    update_time = ImageDraw.Draw(img)
    timestore = ImageDraw.Draw(img)
    tag = ImageDraw.Draw(img)
    branch = ImageDraw.Draw(img)
    font = ImageFont.truetype(dir.get_directory() + "/images/Stencil_Regular.ttf", 40, encoding="unic")
    name_font = ImageFont.truetype(dir.get_directory() + "/images/Lobster-Regular.ttf", 30, encoding="unic")
    font1 = ImageFont.truetype(dir.get_directory() + "/images/ROCK.ttf", 30, encoding="unic")
    font2 = ImageFont.truetype(dir.get_directory() + "/images/ROCK.ttf", 18, encoding="unic")
    font3 = ImageFont.truetype(dir.get_directory() + "/images/ROCK.ttf", 12, encoding="unic")
    report_name = 'GPM '
    # n = gpm_name
    # tag.text((25, 8), 'SK+F', (255, 255, 255), font=font)
    branch.text((24, 150), report_name + "Sales and Stock Report (" + day+")", (255, 209, 0), font=font1)
    # name.text((25, 180), n , (255, 255, 255), font=name_font)
    # timestore.text((25, 200), time + "\n" + day, (255, 255, 255), font=font2)
    timestore.text((25, 200), name, (244, 118,1), font=font2)
    timestore.text((25, 220), "Group Product Manager", (255,255,255), font=font2)

    timestore.text((815, 10), "Last Data Update Time\n" + str(up_date) + ' , ' + up_time,  (255, 255, 255),  font=font3)
    # timestore.text((705, 180), "Name", (255, 255, 255), font=font2)
    # timestore.text((705, 180), "Designation", (255, 255, 255), font=font2)

    img.save(dir.get_directory() + "/images/banner_ai.png")
    # img.show()
    print("1. Banner Created \n ")
