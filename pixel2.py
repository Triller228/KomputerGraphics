from PIL import Image, ImageColor
import math
im = Image.new('1', (500,500)) # create the Image of size 1 pixel 
e = 0
x1 = 100
y1 = 200
x2 = 250
y2 = 400
print ("x1>x2")
if(x1>x2):
    x1,x2 = x2,x1
    y1,y2 = y2,y1
    
dx = math.fabs(x2-x1)
dy = math.fabs(y2-y1)
if ((x2-x1)==0):
    k = 0
else:
    k = dy/dx
print("k==", k)
x,y = x1,y1

if (k<1 and k!=0):
    e1 = e*dx
    while (x2>x and y2>y):
        x +=1
        e1 = e1 + dy
        if (e1 > 0.5*dx):
            if(y2<y1):
                y-=1
            else:
                y +=1
            print (x,y,e1, end="::")
            im.putpixel((x,y), ImageColor.getcolor('white', '1'))
            e1 -=dx
        else:
            im.putpixel((x,y), ImageColor.getcolor('white', '1'))
            print (x,y,e1, end="::")
elif (k>1):
    e1 = e*dy
    while (x<x2 and y<y2):
        x +=1
        e1 = e1 + dx
        if (e1 > 0.5*dy):
            if(y2<y1):
                y-=1
            else:
                y +=1
            print (x,y,e1, end=";")
            im.putpixel((x,y), ImageColor.getcolor('white', '1'))
            e1 -=dy
        else:
            im.putpixel((x,y), ImageColor.getcolor('white', '1'))
            print (x,y,e1, end=";")
else:
    while (x1!=x2 or y1!=y2):
        if(x1==x2):
            if(y1>y2):
                y1,y2=y2,y1
            im.putpixel((x1,y1), ImageColor.getcolor('white', '1'))
            y1 +=1
        elif(y1==y2):
            if(x1>x2):
                x1,x2=x2,x1
            im.putpixel((x1,y1), ImageColor.getcolor('white', '1'))
            x1 +=1
        else:
            x1 +=1
            if(y2<y1):
                y1-=1
            else:
                y1 +=1
            im.putpixel((x1,y1), ImageColor.getcolor('white', '1'))
im.save('simplePixel.png')