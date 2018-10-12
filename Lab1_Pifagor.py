import math 
from tkinter import * 
root=Tk();
canv = Canvas(root, width = 1600, height = 1200, bg = "white")
canv.pack() 
x,y=650,650
side=120
alfa=math.pi/4
x5=x
y5=y
i = 0


def Pifagor(x, y, x5,y5,i, side, alfa, glubina):
    dx=side
    dy=side
    x1,y1=x+dx,y-dy
    x2,y2=x1-dy,y1-dx
    x3,y3=x-dy,y-dx
    x4,y4=x3+side*math.cos(alfa)*math.cos(alfa), y3-side*math.sin(alfa)*math.sin(alfa)
    canv.create_polygon(x, y, x1, y1, x2, y2, x3, y3, activefill = 'green')


    #canv.create_line((x+x1+x2+x3)/4,(y3+y+y2+y1)/4,(x2+x3+x4)/3,(y2+y3+y4)/3,fill = 'red')
    #canv.create_line((x+x1+x2+x3)/4,(y3+y+y2+y1)/4,x5,y5,fill = 'red')
    
    
    x5 = (x3+x2+x4)/3
    y5 = (y3+y2+y4)/3
     
    if glubina>1:
        glubina = glubina-1
        Pifagor(x4, y4,x5,y5,i, alfa, glubina)
        Pifagor(x3, y3,x5,y5,i, side*math.cos(alfa), alfa, glubina)
    

   
    

Pifagor(x, y,x5,y5,i, side,alfa,1)
root.mainloop()