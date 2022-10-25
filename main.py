from PIL import Image, ImageDraw, ImageFont

size_title = 180
size_main = 150
height = 1080
width = 1920
path = "./onryou.TTF"
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)
font_title = ImageFont.truetype(path, size=size_title)
font_main = ImageFont.truetype(path, size=size_main)
draw.text((0, 0), "5Jお化け屋敷・診察予約券", "black", font=font_title)
draw.text((width/2, height/2), "時間", "black", font=font_main, anchor="mm")
img.save("test.jpg")
