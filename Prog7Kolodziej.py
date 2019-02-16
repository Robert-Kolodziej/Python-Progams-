##Bobby Kolodziej
##
##File: Prog7Kolodziej.py
##
##Purpose: The purpose of this program is to give the user options from a menu and each choice
##          on the menu will call a different method.
##
##Input: The user inputs their choice after reading the list of different choices.
##
##
##Output: The output for this program is the information from each different method that is run.
##
##Certification of authority:
##I certify that this lab is entirely my own work. But I communicated with Professor Schwartz and the Programming lab.

def main():

    print("Welcome to the menu program where you pick a choice")
    choice = '-1'
    while (choice != '0'):
        print()
        print('1: Handle Grades')
        print('2: More Evens or More Odds')
        print('3: How Many Times')
        print('0: Quit')

        choice = input("Enter your choice: ")

        if choice == '1':
            handleGrades()
        elif choice == '2':
            moreEvenOrmoreOdd()
        elif choice == '3':
            howManyTimes()
        elif choice == '0':
            print("Goodbye")
        else:
            print("Invalid choice try again")


## handleGrades
## handleGrades will ask the user for 10 grades one at a time, then three helper methods will determine the
## highest grade, the lowest grade, and the average of all the grades.
## Parameters
##  nothing is passed to this function from main
## Returns the lowest the highest and the average of the grades

def handleGrades():
    average = 0
    grades = []
    gradenum = 0

    while gradenum <= 10:
        grade = float(input("Enter a grade: "))
        grades.append(grade)
        gradenum = gradenum+1
    highest=calcHighest(grades)
    lowest=calcLowest(grades)
    average=calcAverage(grades)
    print("The highest grade is" , highest)
    print("The lowest grade is" , lowest)
    print("The average is" , round(average,2))

                    
## calcHighest
## calcHighest takes the values in the list and determines the highest grade in the list.
## Parameters
## 1. the list of grades gets passed to this function
# Returns the highest grade on the list.
                    
def calcHighest(gradelist):
    highest = 0
    for grade in (gradelist):
        if grade > highest:
            highest = grade
    return highest

                    
## calcLowest
## calcLowest takes the values in the list and determines the lowest grade in the list.
## Parameters
## 1. the list of grades is also passed to this function
## Returns the lowest grade on the list.

def calcLowest(gradelist):
    lowest = 10000
    for grade in (gradelist):
        if grade < lowest:
            lowest = grade
    return lowest


## calcAverage
## calcAverage takes all the grades and adds them all up and divides by the number of grades to determine the average.
## Parameters
## 1. the list of grades is passed to this function
## Returns the average of all the grades in the list

def calcAverage(gradelist):
    average = 0
    for grade in (gradelist):
        average = average + grade
    average = average/len(gradelist)
    return average


## moreEvenOrmoreOdd
## moreEvenOrmoreOdd will ask the user for up to 10 positive numbers and put them into a list. This will stop if a negative
## is typed into the input.
## Parameters
## 1. nothing is passed to this function
## Returns nothing in this method.
                    
def moreEvenOrmoreOdd():
    numbers = []
    numEven = 0
    numOdd = 0
    nums=0
    userinput = int(input("Enter a positive number, negative to quit: "))
    
    while nums < 10 and userinput > 0:
        numbers.append(userinput)
        userinput = int(input("Enter a positive number, negative to quit: "))
        nums=nums+1
        
    numEven = countNumEven(numbers)
    numOdd = countNumOdd(numbers)
    
    if numEven > numOdd:
        print("There are more even numbers in the list")
        for i in (numbers):
            if i%2 == 0:
                print(i, end=" ")
    elif numOdd > numEven:
        print("There are more odd numbers in the list")
        for i in (numbers):
            if i %2 != 0:
                print(i, end=" ")
    else:
        print("The evens and odds are the same")
        print(numbers)
    


## countNumEven
## countNumEven counts the number of even numbers in the list of numbers.
## Parameters
## 1. the list of numbers is passed to this method.
## Returns the number of even numbers
                    
def countNumEven(numberslist):
    numEven = 0
    for num in numberslist:
        if num %2 == 0:
            numEven = numEven + 1
    return numEven

        
## countNumOdd
## countNumOdd counts the number of odd numbers in the list of numbers.
## Parameters
## 1. the list of numbers is passed to this method.
## Returns the number of odd numbers

def countNumOdd (numberslist):
    numOdd = 0
    for num in numberslist:
        if num %2 !=0:
            numOdd = numOdd + 1
    return numOdd


## howManyTimes
## howManyTimes counts how many times a value occurs ina list of negative numbers
## Parameters
## 1. nothing is passed to this method

def howManyTimes():
    target = 0
    targetoccurances = 0
    numberslist = []
    nums = 0
    usernums = int(input("Enter a negative number, positive to quit: "))
    while nums < 10 and usernums < 0:
        numberslist.append(usernums)
        usernums = int(input("Enter a negative number, positive to quit: "))
        
    nums = nums + 1
    target = int(input("Enter the target number: "))
    for number in(numberslist):
        if number == target:
            targetoccurances = targetoccurances + 1
            
    printOut(numberslist,target,targetoccurances)

    
    


## printOut()
## printOut() prints all the information from the method howManyTimes
## Parameters
## 1. number list
## 2. the target number
## 3. the number of times the target occurs
## returns all these values printed to the screen. 
def printOut(numslist,targetnum,targettimes):
    print("The list is", numslist)
    print("The target number is" , targetnum)
    print("The target number occurs", targettimes, "times in the list")

main()
