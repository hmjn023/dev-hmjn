from escpos.printer import Usb
from escpos import *

from PIL import Image

img = Image.open("./test.jpg")
img = img.rotate(90)

p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)
p.text("5j\n")
p.image(img)
p.cut()
