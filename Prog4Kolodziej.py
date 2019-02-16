##Bobby Kolodziej
##
##File: Prog4Kolodziej.py
##
##Purpose: The purpose of this program is to play a random gambling game with dice 
##
##Input: The input for this program is the ammount of money the player wants to play with.
##
##Output: The output for this program will be the pot, the value on die 1, the value on die 2, the sum of the both dice, and the play number. 
##
##Certification of authority:
##I certify that this lab is entirely my own work.

def main():
    #Greeting for the player 
    pot=int(input("Please enter the amount of money you would like to play with: "))
    play= 0
    maxvalue=0

    #Playing the game
    while pot > 0:
        import random 
        die1value= random.randint(1,6)
        die2value= random.randint(1,6)
        sum=die1value + die2value
        if sum == 7:
            pot=pot+4
        else:
            pot=pot-1
        play=play+1
        print("The first die value was", die1value, ", the second die value was", die2value, ", you have $", pot, "in your pot", ", you are on play number", play)
    print("Game over: You ran out of money")
    print("It took you", play, "plays to run out of money")
    
main()
