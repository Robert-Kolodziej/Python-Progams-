#Longestword.py


def findlongestword(sent):
    wordlist = sent.split()
    longestword = wordlist[0]
    for word in wordlist:
        if len(word)>len(longestword):
            longestword = word
    
    return longestword

def countfourletterwords(sent):
    wordlist = sent.split()
    numfourletterwords = 0
    for word in wordlist:
        if len(word)== 4:
            numfourletterwords = numfourletterwords + 1
    return numfourletterwords

def asterix(sent):
    wordlist = sent.split()
    numfourletterwords = 0
    for word in wordlist:
        if len(word)== 4:
            sensor = sent.replace(word, "****")
    return sensor

            
def main():
    
    sentence = input("Enter a sentence: ")
    longestword = findlongestword(sentence)
    fourletterwords = countfourletterwords(sentence)
    sensor = asterix(sentence)
    print("The longest word is", longestword)
    print("There are" , fourletterwords, "four letter words in the sentence")
    print(sensor)
main()
