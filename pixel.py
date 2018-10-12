from PIL import Image, ImageColor
import math
im = Image.new('1', (500,500)) # create the Image of size 1 pixel 
x1 = 100
y1 = 200
x2 = 250
y2 = 400
dx = (x1-x2)
dy = (y2-y1)
if (math.fabs(dy) > math.fabs(dx)):
    znak = 1
else:
    znak = -1
    
if (dy<0):
    znaky = -1
else:
    znaky = 1
    
if (dx<0):
    znakx = -1
else:
    znakx = 1
f = 0
x = x1
y = y1
while(x != x2 or y != y2):
    if (znak == -1):
        f = f + dy*znaky
        if (f>0):
            f=f-dx*znakx
            y=y+znaky
        x -= znakx
       # print (x,y, end=" ")
        im.putpixel((x,y), ImageColor.getcolor('white', '1'))
    else:
        f = f + dx*znakx
        if (f>0):
            f=f-dy*znaky
            x=x-znakx
        y += znaky
        #print (x,y, end=" ")
        im.putpixel((x,y), ImageColor.getcolor('white', '1'))

im.save('simplePixel.png')