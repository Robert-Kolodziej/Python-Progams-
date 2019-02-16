#ReadWordsFromFile.py

#read words from a file and print them out

def main():
    filename = input ("Enter the file name, including suffix: ")
    wordFile = open(filename, 'r')
    countwords = 0
    countletters = 0
    ecount = 0
    fourletterwordcount = 0 

    for line in wordFile:
        line = line.strip()
        countwords = countwords+1
        countletters = len(line)+ countletters
        ecount = line.find("e")+ ecount
        if len(line) == 4:
            fourletterwordcount = fourletterwordcount + 1
        print(line)
    print("There are", countwords , "words in the file")
    print("There are", countletters, "letters in the file")
    print("there are", ecount, "e's in the file")
    print("There are", fourletterwordcount, "four letter words in the file")
main()
