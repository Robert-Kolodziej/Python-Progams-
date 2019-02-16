#ReadFromFileALineAtATime.py

#Read from a file a line at a time, adding up the numbers

def main():
    theFile = open("input2.txt", 'r')
    outFile = open("outputfile.txt", "w")                                                                                                                                                                                                                          
    sum = 0
    for line in theFile:
        number = int(line)
        print(number, file=outFile)
        sum = sum + number
    print ("The sum is", sum)

    #send some output to the output file
    print("The sum is", sum, file=outFile)
    theFile.close()
    outFile.close()
main()
