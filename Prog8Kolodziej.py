##Bobby Kolodziej
##
##File: Prog8Kolodziej.py
##
##Purpose: This program gives a list of options and the user picks one
##      and this program reads another file and makes a rectangle
##
##Input: The user inputs the width of the rectangle and the height of the rectangle
##      and the fillstyle of the rectangle
##
##Output: The program outputs the rectangle with the info that is input by the user
##
##Certification of authority:
##I certify that this lab is entirely my own work. But I communicated with the programming lab.

from rectangleKolodziej import Rectangle

def main():
    ##Printing the choices
    userChoice = 'X'
    print("Welcome to the rectangle builder")
    print("W: Assign the width")
    print("H: Assign the height")
    print("F: Assign the fillstyle")
    print("A: Calculate the area")
    print("P: Calculate the perimeter")
    print("T: Text Description of the rectangle")
    print("D: Draw the rectangle")
    print("Q: Quit")

    newRectangle = Rectangle(10, 5, "*")

    userChoice = input("Enter your choice: ")

    ##Interpreting the user choice

    while userChoice != 'Q' or 'q' :
        if userChoice == 'W' or userChoice =='w':
            newWidth = int(input("Enter the new width: "))
            if newWidth>0:
                newRectangle.setWidth(newWidth)
                userChoice = input("Enter your choice: ")
            else:
                print("Invalid width try again")
                newWidth = int(input("Enter the new width: "))

        elif userChoice == 'H'or userChoice =='h':
            newHeight = int(input("Enter the new height: "))
            if newHeight > 0:
                newRectangle.setHeight(newHeight)
                userChoice = input("Enter your choice: ")
            else:
                print("Invalid height try again")
                userChoice = input("Enter your choice: ")

        elif userChoice == 'F' or userChoice == 'f':
            newFillstyle = input("Enter the new fillstyle: ")
            newRectangle.setFillstyle(newFillstyle)
            userChoice = input("Enter your choice: ")

        elif userChoice == 'A' or userChoice == 'a':
            newRectangle.calcArea()
            userChoice = input("Enter your choice: ")

        elif userChoice =='P' or userChoice == 'p':
            newRectangle.calcPerimeter()
            userChoice = input("Enter your choice: ")

        elif userChoice == 'T' or userChoice =='t':
            newRectangle.text()
            userChoice = input("Enter your choice: ")

        elif userChoice == 'D' or userChoice == 'd':
            newRectangle.drawRectangle()
            userChoice = input("Enter your choice: ")

        elif userChoice == 'Q' or userChoice =='q':
            print("Goodbye")
            

        else:
            print("Invalid Choice try again")
            userChoice = input("Enter your choice: ")
    

main()
            


            
            
            

    
    


