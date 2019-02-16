#ReadMultipleNumbersPerLine.py

def main():
    theFile = open("input4.txt", 'r')
    sum = 0

    #find out how many numbers are in the file
    line = theFile.readline()
    numInputs = int(line)

    #read in a line of numbers
    for i in range (numInputs):
        line = theFile.readline()
        #convert it into a list
        list = line.split()
        size = len(list)
        print("There are", size, "numbers in this line: ", list)

        #add the numbers in this list to the sum
        for x in range(size):
            number = int(list[x])
            sum = sum + number

    print("The sum is", sum)

    #output to a file
    outName = input("Give me an output file name with suffix: ")
    outFile = open(outName, 'w')
    print("The sum is", sum, file = outFile)
    
    theFile.close()

main()
