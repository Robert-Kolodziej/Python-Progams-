#RandomGuess.py

import random
def main():
    print("Welcome to the randome number game")
    winner = False
    lownum = int(input("Enter the smaller number: "))
    highnum = int(input("Enter the higher number: "))
    randNum = random.randint(lownum, highnum)
    counter = 0
    while winner == False:
        userguess = int(input("Enter your guess: "))
        counter = counter + 1
        if userguess>randNum:
            print("Too large!")
        elif userguess<randNum:
            print("Too small!")
        else:
            winner = True
    print("Congratulations! You got it in" , counter, "tries")
main()

    
