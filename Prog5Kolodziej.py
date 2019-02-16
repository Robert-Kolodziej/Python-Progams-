##Bobby Kolodziej
##
##File: Prog5Kolodziej.py
##
##Story one came from: https://www.woojr.com/summer-mad-libs/funny-mad-libs/
##
##Story two came from: https://www.woojr.com/winter-mad-libs/winter-mad-libs-kids/
##
##Purpose: This is a program that reads a file of inputs for the user. Takes the inputs and replaces
##          numbers from another file with the words that are input by the user.
##
##Input: The input for this program is what each blank needs from the file that is being read in by this program.
##
##Output: The output from this program will be the full story with all the blanks filled in from the input from the user.
##
##Certification of authority:
##I certify that this lab is entirely my own work but I commuicated with Professor Schwartz and Sean Kohler.

def main():
    print("Welcome to the mad libs program")
    #Input file: inputstory1.txt or inputstory2.txt
    #Replace file: replace1.txt or replace2.txt

    #Asking the user for the file names and opeing the files for reading
    inputFile = input("Enter the file name for the input file, including the suffix: ")
    replacementFile = input("Enter the file name for the replacement file, including the suffix: ")
    inFile = open(inputFile, 'r')
    story = inFile.read()
    replaceFile = open(replacementFile, 'r')

    #Repeating a line split for each line in the program
    for line in replaceFile:
        list = line.split()
        print("Please enter a(n):")
        userinput= input(list[1])
        for line in story:
            story = story.replace(list[0], userinput)
            
    #printing the story with the blanks filled in
    print(story)
    outputFile = input("Enter the file name for the output file, including the suffix: ")
    outFile = open(outputFile, 'w')
    print(story, file = outFile)
    inFile.close()
    replaceFile.close()

main()
