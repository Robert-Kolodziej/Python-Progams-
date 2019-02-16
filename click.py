#File: click.py

from graphics import *

def main():
    

    #get clicks from the user and tell her where she clicked
    radius = 5
    clicks = int(input("How many clicks do you want: "))
    win = GraphWin("Click Me", 300,300)
    center = Point(150,150)
    label = Text(center, "Click randomly times around the screen")
    label.draw(win)
    for i in range (clicks):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())
        circ = Circle(p,radius)
        circ.setFill("red")
        radius+=5
        circ.draw(win)
    label = Text(p, "Thats all of your clicks")
    label.draw(win)
    
main()
