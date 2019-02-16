##Bobby Kolodziej
##
##File: Prog3Kolodziej.py
##
##Purpose: A program to calculate the total charge to a customer for downloading movies.
##
##Input: The input for this program are the buyer's last name, the buyer's first name,
##       the number of movies downlaoded, and the cost per downloaded movie.
##
##Output: the output for this program will be the total cost the buyer has to pay for all the movies
##        including tax for each movie.
##
##Certification of authority:
##I certify that this lab is entirely my own work, but I discussed with Zach Fredeman.

def main():
    print("This program calculates the total cost for downloaded movies")
    
    #Prompting the user for input values.
    lastname = input("Please enter the buyer's last name: ")
    firstname = input("Please enter the buyer's first name: ")
    numMovies = int(input("Please enter the number of movies downloaded: "))
    costMovie = float(input("Please enter the cost for the movies: "))

    #Calculating the base charge 
    baseCharge= numMovies * costMovie

    #Calculating the service charge.
    if numMovies <= 2:
        serviceCharge = baseCharge * .21
    elif numMovies  > 2 and numMovies < 5:
        serviceCharge = baseCharge * .17
    else:
        serviceCharge = baseCharge * .12

    netPayment = serviceCharge + baseCharge

    #Calculate the tax amount.
    if netPayment <= 4.50:
        tax = netPayment *.0
    elif netPayment > 4.50 and netPayment <= 6.00:
        tax = netPayment *.03
    elif netPayment > 6.00 and netPayment <= 8.75:
        tax = netPayment* .07
    else:
        tax = .08 * netPayment
    totalCharge = tax + netPayment

    print(firstname, lastname)
    print("Bought", numMovies, "movies")
    print("At a price of $" , costMovie)
    print("With a service charge of $" , serviceCharge)
    print("Taxes totaling $" , tax)
    print("With a total cost of $" , totalCharge)
    
main()
 
        
