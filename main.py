from PIL import Image, ImageDraw, ImageFont
import datetime

size_title = 80
size_middle = 30
size_main = 50
height = 874
width = 1240
no = 0
groups = int(input())
resevation = datetime.datetime.now()+datetime.timedelta(minutes=15*groups)
path = "./NotoSansJP-Regular.otf"
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)
font_title = ImageFont.truetype(path, size=size_title)
font_main = ImageFont.truetype(path, size=size_main)
font_middle = ImageFont.truetype(path, size=size_middle)
draw.text((width/2, 0+size_title/2), "診察予約券", "orange", font=font_title, anchor="mm")
draw.text((size_title, size_title*2), "No."+str(no), "black", font=font_main)
draw.text((size_title + size_main*4, size_title*2), "岩橋涼子", "black", font=font_main)
draw.line((size_title, size_title*2+size_main*1.5, size_title+size_main*9, size_title*2+size_main*1.5), fill=(0, 0, 0), width=3)

draw.text((width/2, height/2), "診察予定時間："+resevation.strftime("%m月%d日 %H時%M分"), "black", font=font_main, anchor="mm")

draw.line((width-size_main*9.5, height-size_main*5.2, width-size_main*9.5, height), fill=100, width=10)
draw.line((width-size_main*9.5, height-size_main*5.2, width, height-size_main*5.2), fill=100, width=10)
draw.text((width-size_main*9, height-size_main*5), "病院ですとも", "black", font_main)
draw.text((width-size_main*9, height-size_main*3.5), "TEL:0438-30-4000\n〒292-0041\n千葉県木更津市清見台東2-11-1", "black", font=font_middle)
img.save("test.jpg")
