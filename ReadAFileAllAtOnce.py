#ReadAFileAllAtOnce.py
#Read a file all at once

def main():
    filename = input("Enter the file name, including the suffix: ")
    wordFile = open(filename, "r")
    contents = wordFile.read()
    print (contents)
    wordFile.close()
    
main()
