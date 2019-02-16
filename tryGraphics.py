#fun with gtraphics
#tryGraphics.py

#import the graphics package
from graphics import *

#we need a graphics window to start
win = GraphWin("My Graphics Window", 400,400)

#make a point or two
p = Point(50,60)
p2 = Point(140,100)
x = p.getX()
y = p.getY()
print(x,y)

p.draw(win)
p2.draw(win)


#draw a circle
center = Point(100,100)
circ = Circle(center,30)
circ.setFill("red")
circ.setOutline("green")
circ.setWidth(5)
circ.draw(win)

#label the circle
label = Text(center, "red circle")
label.draw(win)

#draw an X
startpoint = Point(20,30)
endpoint = Point(180,165)
startpoint2 = Point(20,165)
endpoint2 = Point(180,30)
    
line = Line(startpoint,endpoint)
line2 = Line(startpoint2,endpoint2)
line.setWidth(5)
line2.setWidth(5)
line.draw(win)
line2.draw(win)

#draw rectangle around the X
rect = Rectangle(startpoint, endpoint)
rect.setWidth(5)
rect.setOutline("blue")
rect.draw(win)

#draw an oval
ovalP1 = Point(300,100)
ovalP2 = Point(380,50)
oval= Oval(ovalP1,ovalP2)
oval.move(-40,0)
oval.setWidth(5)
oval.setOutline("gold")
oval.setFill("purple")
oval.draw(win)

#draw second oval
#oval2 = oval  Noooooooooo!!!!!
oval2 = oval.clone()
oval2.move(0,60)
oval2.draw(win)


