# openFileDialog.py

#import so that we can use dialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
def main():
    filename = askopenfilename()
    wordFile = open(filename, 'r')

    countWords = 0
    countLetters = 0

    for line in wordFile:
        line = line.strip()
        print(line)
        countWords = countWords + 1
        countLetters = countLetters + len(line)
    print("There are", countWords, "words in the file")
    print("There are", countLetters, "letters in the file")
    
    outfilename = asksaveasfilename()
    outFile = open(outfilename, 'w')
    print("There are", countWords, "words in the file", file=outFile)
    print("There are", countLetters, "letters in the file", file = outFile)
    wordFile.close()
main()
