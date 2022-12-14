from cgitb import reset
from tokenize import group
from PIL import Image, ImageDraw, ImageFont
import datetime
from escpos import image
import json

from escpos.printer import Usb
from escpos import *


p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)

size_title = 80
size_middle = 30
size_main = 50
height = 874
width = 1240
no = 0
groups = 0
time = 10
reserve = []

path = "./NotoSansJP-Regular.otf"

font_title = ImageFont.truetype(path, size=size_title)
font_main = ImageFont.truetype(path, size=size_main)
font_middle = ImageFont.truetype(path, size=size_middle)

# for i in range(99999999):
while True:
    opend = open("./data.json", "r")
    loaded = json.load(opend)
    no = loaded["no"]
    groups = loaded["groups"]
    reserve = loaded["reserve"]

    mode = input()
    if(mode == "m"):
        groups -= 1
        del reserve[0]

    elif(mode == "p"):
        groups += 1
        no += 1
        now = datetime.datetime.now()
        after = now+datetime.timedelta(minutes=time*groups)

        reserve.append({"no": no, "groups": groups, "now": now.strftime('%Y年%m月%d日 %H:%M'), "reserve": after.strftime('%Y年%m月%d日 %H:%M')})
        img = Image.new("RGB", (width, height), (240, 210, 160, 90))
        draw = ImageDraw.Draw(img, "RGBA")
        draw.arc((0-410, height-410, 410, height+410), start=0, end=360, fill=(255, 0, 0, 90), width=10)
        draw.arc((100, -1000, 2100, 1000), start=0, end=360, fill=(255, 0, 0, 90), width=10)

        draw.text((width/2, size_title/2), "診察予約券", "green", font=font_title)
        draw.text((size_title, size_title*2), "No."+str(no), "black", font=font_main)
        draw.text((size_title + size_main*4, size_title*2), input("お名前を入力："), "black", font=font_main)
        draw.line((size_title, size_title*2+size_main*1.5, size_title+size_main*9, size_title*2+size_main*1.5), fill=(0, 0, 0), width=3)

        draw.text((width/2, height/2), "診察予定時間："+after.strftime('%Y年%m月%d日 %H:%M'), "black", font=font_main,anchor="mm")

        draw.line((width-size_main*9.5, height-size_main*5.2, width-size_main*9.5, height), fill=(200, 170, 240, 125), width=10)
        draw.line((width-size_main*9.5, height-size_main*5.2, width, height-size_main*5.2), fill=(200, 170, 240, 125), width=10)
        draw.text((width-size_main*9, height-size_main*5), "病院ですとも", "black", font_main)
        draw.text((width-size_main*9, height-size_main*3.5), "TEL:0438-30-4000\n〒292-0041\n千葉県木更津市清見台東2-11-1", "black", font=font_middle)
        img.save("test.jpg")
        img = Image.open("./test.jpg")
        img = img.resize((int(width/2), int(height/2)))
        img = img.rotate(90, expand=True)
        p.text(" 5J\n")
        p.image(img)
        p.cut()
    elif(mode == "g"):
        groups = int(input("how many waiting groups? : "))
        no+=1
        dt_groupsw = datetime.datetime.now()+datetime.timedelta(minutes=time*groups)
        img = Image.new("RGB", (width, height), (240, 210, 160, 90))
        draw = ImageDraw.Draw(img, "RGBA")
        draw.arc((0-410, height-410, 410, height+410), start=0, end=360, fill=(255, 0, 0, 90), width=10)
        draw.arc((100, -1000, 2100, 1000), start=0, end=360, fill=(255, 0, 0, 90), width=10)

        draw.text((width/2, size_title/2), "診察予約券", "green", font=font_title)
        draw.text((size_title, size_title*2), "No."+str(no), "black", font=font_main)
        draw.text((size_title + size_main*4, size_title*2), "岩橋涼子", "black", font=font_main)
        draw.line((size_title, size_title*2+size_main*1.5, size_title+size_main*9, size_title*2+size_main*1.5), fill=(0, 0, 0), width=3)

        draw.text((width/2, height/2), "診察予定時間："+dt_groupsw.strftime('%Y年%m月%d日 %H:%M'), "black", font=font_main,anchor="mm")

        draw.line((width-size_main*9.5, height-size_main*5.2, width-size_main*9.5, height), fill=(200, 170, 240, 125), width=10)
        draw.line((width-size_main*9.5, height-size_main*5.2, width, height-size_main*5.2), fill=(200, 170, 240, 125), width=10)
        draw.text((width-size_main*9, height-size_main*5), "病院ですとも", "black", font_main)
        draw.text((width-size_main*9, height-size_main*3.5), "TEL:0438-30-4000\n〒292-0041\n千葉県木更津市清見台東2-11-1", "black", font=font_middle)
        img.save("test.jpg")
        img = Image.open("./test.jpg")
        img = img.resize((int(width/2), int(height/2)))
        img = img.rotate(90,expand=True)
        p.text(" 5J\n")
        p.image(img)
        p.cut()
    elif(mode=="v"):
        for i in reserve:
            print(i)
    elif(mode=="q"):
        print("quit")
        exit()
    else:
        print("m(minus): 退出時にこれをする")
        print("p(plus and print): 人が来たときにこれをする")
    loaded["no"] = no
    loaded["groups"] = groups
    loaded["reserve"] = reserve
    with open("./data.json", "w") as f:
        json.dump(loaded, f)
