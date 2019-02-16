#ReadCertainNumberofValues.py

#Read first number, then read that many numbers 

def main():
    maxval = 0
    theFile = open("input3.txt", 'r')
    line = theFile.readline()
    numinputs = int(line)
    for i in range(numinputs):
        line = theFile.readline()
        number = int(line)
        if number > maxval:
            maxval = number 
    print ("The maximum value is", maxval)
main()
