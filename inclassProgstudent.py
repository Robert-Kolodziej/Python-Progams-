from student import Student

def main():
    # create a new student
    newStudent = Student("Jimmy" , 5)
    newStudent2 = Student("Bobby" , 5)
    
    newStudent.setScore(1,100)
    newStudent.setScore(2,50)
    
    newStudent2.setScore(1,100)
    newStudent2.setScore(2,98)
    newStudent2.setScore(3,99)
    newStudent2.setScore(4,97)
    newStudent2.setScore(5,96)
    
    average = newStudent.getAverage()
    highest = newStudent.getHighScore()
    average2 = newStudent2.getAverage()
    highest2 = newStudent2.getHighScore()
    
    print(newStudent)
    print("The average is: ", average)
    print("The highest grade is: ", highest)
    print(newStudent2)
    print("The average is: ", average2)
    print("The highest grade is: ", highest2)

    theName = input("Enter the name of the student: ")
    numScores = int(input("Enter number of grades for " + theName)
    student3 = Student(theName, numScore)

    for i in range(numScore):
        grade = float(input("Enter grade" + str(i+1))
        student3.setScore(i+1, grade)

    print(student3)
main()
