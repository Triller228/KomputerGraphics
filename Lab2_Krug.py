from PIL import Image, ImageColor,ImageDraw
im = Image.new("RGB", (500, 500))
draw = ImageDraw.Draw(im)
x0 = 250
y0 = 250
R = 25
draw.line([x0,y0,x0+2,y0+2], (0, 0, 255))


def Circle1(x0,y0,rad):
    im.putpixel((x0,y0+R), (255,250,250))
    im.putpixel((x0,y0-R), (255,250,250))
    im.putpixel((x0+R,y0), (255,250,250))
    im.putpixel((x0-R,y0), (255,250,250))
def Circle2(x0,y0,x,y):
    im.putpixel((x0+x,y0+y), (255,255,255))
    im.putpixel((x0-x,y0+y), (255,255,255))
    im.putpixel((x0+x,y0-y), (255,255,255))
    im.putpixel((x0-x,y0-y), (255,255,255))
    im.putpixel((x0+y,y0+x), (255,255,255))
    im.putpixel((x0-y,y0+x), (255,255,255))
    im.putpixel((x0+y,y0-x), (255,255,255))
    im.putpixel((x0-y,y0-x), (255,255,255))


Circle1(x0,y0,R)
x = 0 
y = R
f = lambda x,y: pow(x,2) + pow(y,2) - pow(R,2)
while(x <= y):
    if(f(x+1,y-0.5) > 0):
        y = y - 1
    x = x + 1
    Circle2(x0,y0,x,y)
    print('x ','y ', x,y)

draw.line([x0-x,y0-y,x0+x,y0+y], (0, 0, 255))



im.save('simplePixel.png')