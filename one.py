<<<<<<< HEAD
from PIL import  Image,ImageDraw,ImageFont,ImageFilter
import time
def addNum(nub,filepath):
    img = Image.open(filepath)
    width,height = img.size
    fontSize =int(height/20)
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('C:\\windows\\Fonts\\Arial.ttf',fontSize);  #图片位置，及添加数字大小 
    draw.text((width-80,0),str(nub),(256,0,0),font=ttFont)     #确定显示的 位置，数字，颜色，字体
    img.save('D:/360/qq_addNub.jpg')
    img.show()
    time.sleep(3)
    img1=img.filter(ImageFilter.GaussianBlur)   #模糊化
    img1.show()
   # img1.save('D:/360/blur.jpg')
