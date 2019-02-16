#crazyCircles.py

from graphics import *

win = GraphWin("Crazy Circles", 500,500)
center = Point(250,250)
label = Text(center, "click near the center of the screen")
label.draw(win)
p1 = win.getMouse()


circ1 = Circle(p1, 200)
circ1.setFill("red")
circ1.draw(win)
circ2 = Circle(p1,170)
circ2.setFill("orange")
circ2.draw(win)
circ3 = Circle(p1,140)
circ3.setFill("yellow")
circ3.draw(win)
circ4 = Circle(p1,110)
circ4.setFill("green")
circ4.draw(win)
circ5 = Circle(p1,80)
circ5.setFill("blue")
circ5.draw(win)
circ6 = Circle(p1,50)
circ6.setFill("Purple")
circ6.draw(win)
circ7 = Circle(p1,20)
circ7.setFill("pink")
circ7.draw(win)
circ8 = Circle(p1,5)
circ8.setFill("black")
circ8.draw(win)

