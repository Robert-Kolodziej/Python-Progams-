"""
File: rectangleKolodziej.py

This module defines the rectangle class.
"""

class Rectangle:
    """This class represents drawing a rectangle."""

    def __init__(self, width, height, fillstyle):
        self.myWidth = width
        self.myHeight = height
        self.myFillstyle = fillstyle

    def getWidth(self):
        """Returns the width of the rectangle."""
        return width

    def getHeight(self):
        """Returns the height of the rectangle."""
        return height

    def getFillstyle(self):
        """Returns the fillstyle of the rectangle."""
        return fillstyle

    def setWidth(self, newWidth):
        """Sets the width of the rectangle."""
        self.myWidth = newWidth

    def setHeight(self, newHeight):
        """Sets the height of the rectangle."""
        self.myHeight = newHeight

    def setFillstyle(self, newFillstyle):
        """Sets the fillstyle f the rectangle. """
        self.myFillstyle = newFillstyle

    def calcArea(self):
        """Calculates the area of the rectangle."""
        area = 0
        area = self.myWidth * self.myHeight

        return area

    def calcPerimeter(self):
        """Calculates the perimeter of the rectangle."""
        perimeter = 0
        perimeter = self.myWidth*2 + self.myHeight*2

        return perimeter 

    def drawRectangle(self):
        """Prints out the rectangle to the screen. """
        for row in range(self.myHeight):
            for column in range (self.myWidth):
                print(self.myFillstyle, end="")
            print()
        

    def text(self):
        """Returns the text representation of the rectangle."""
        print("Width: " , self.myWidth)
        print("Height: ", self.myHeight)
        print("Fillstyle: ", self.myFillstyle)
        print("Perimeter:, ", self.calcPerimeter())
        print("Area: ", self.calcArea())
        
         
        
                
