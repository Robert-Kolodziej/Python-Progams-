# File: happyFace.py

#import graphics window
from graphics import *

#create the graphics window
win = GraphWin("My Graphics Window", 500,500)

#draw the face
center = Point(250,250)
circ = Circle(center,150)
circ.setFill("yellow")
circ.draw(win)

#draw eyes

center = Point(100,150)
circ2 = Circle(center,15)
circ2.setFill("black")
circ2.move(90,40)
circ2.draw(win)

circ3 = circ2.clone()
circ3.move(120, 0)
circ3.draw(win)

center = Point(100,150)
circEye = Circle(center, 4)
circEye.setFill("white")
circEye.move(90,40)
circEye.draw(win)

circEye2 = circEye.clone()
circEye2.move(120,0)
circEye2.draw(win)

#draw mouth

center = Point(250,300)
circMouth = Circle(center, 40)
circMouth.setFill("black")
circMouth.draw(win)

#draw nose


