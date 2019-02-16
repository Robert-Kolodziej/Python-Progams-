##Bobby Kolodziej
##
##File: Prog6Kolodziej.py
##
##Purpose: The purpose of this program is to calculate the cost of movies on pay per view with the service charge, taxes, and initial
##          cost of movies from a user.
##
##Input: The input for this program is the name of the user, the user ID number, the rating, the number of movies, the length of the movies 
##
##Output: The output for this program is all of the infomation that is input by the user with the price calculated.
##
##Certification of authority:
##I certify that this lab is entirely my own work. But I communicated with Sean Kohler and the programming lab

#Main
#Main will ask the user for their name, ID number, and the number of movies ordered
#Parameters:
#   1. User name
#   2. User ID number
#   3. The number of movies ordered
#
#Returns: nothing is returned. 


def main():
    movieCost = 0
    serviceCharge = 0
    totalDue = 0
    taxDue = 0
    totalDuewithTax = 0
    numMovies = 0
    totalmoviecost = 0
    #Greeting for the user
    print("Welcome to the pay per view movie program which calculates the cost of your movies")
    customerID = int(input("Enter a number between 25000 and 99999: "))

    while customerID < 25000 or customerID > 99999:
        print("This is an invalid ID number, Please try again")
        customerID = int(input("Enter a number between 25000 and 99999: "))
   

    name = input("Enter your name: ")
    numMovies = int(input("Enter the number of movies ordered: "))

    totalmoviecost = chooseMovies(numMovies)
    serviceCharge = calcServiceCharge(numMovies, totalmoviecost)
    totalDuewithTax = calcTotalDue(totalmoviecost,serviceCharge)
    outputResults(name, customerID, numMovies,totalmoviecost,serviceCharge,totalDuewithTax)


#chooseMovies
#chooseMovies asks the user for the nunmber of movies ordered along with the rating of each movie which is used to determine the cost of the movie
#Parameters:
#   1. number of movies
#
#Returns: the cost of the movies 

def chooseMovies(numberMovies):
    totalmoviecost = 0

    

    while numberMovies <= 0:
        print("This is an invalid number of movies. Please try again")
        numberMovies = int(input("Enter the number of movies ordered: "))

    for movies in range(numberMovies):
        movieLength = int(input("Enter the length of the movie between 1 and 240: "))
        
        while movieLength < 1 or movieLength > 240:
            print("This is not a valid movie length. Please try again")
            movieLength = int(input("Enter the length of the movies between 1 and 240: "))
            
        movieRating = input("Enter the rating of the movie with either G, P, R, X, or O: ")
        
        while not (movieRating == 'G' or movieRating == 'P' or movieRating == 'R' or movieRating == 'X' or movieRating == 'O'):
            print("This is not a valid rating. Please try again")
            movieRating = input("Enter the rating of the movie with either G, P, R, X, or O: ")
                

        if movieRating == 'G':
            movieCost = movieLength * (.039)
        if movieRating == 'P':
            movieCost = movieLength * (.054)
        if movieRating == 'R':
            movieCost = movieLength * (.068)
        if movieRating == 'X':
            movieCost = movieLength * (.273)
        if movieRating == 'O':
            movieCost = movieLength * (.04)

        totalmoviecost = movieCost + totalmoviecost 
    

    return totalmoviecost


#calcServiceCharge
#calcServiceCharge calculates the service chare for the movies based on the number of movies ordered
#Parameters:
#   1. The number of movies
#   2. The total cost of the movies
#
#Returns: The service charge

def calcServiceCharge(numberofMovies,movieCost):

   
    if numberofMovies >= 1 and numberofMovies <= 3:
        serviceCharge = movieCost * (.18)
    elif numberofMovies >= 4 and numberofMovies <= 7:
        serviceCharge = movieCost * (.15)
    elif numberofMovies >= 8 and numberofMovies <= 11:
        serviceCharge = movieCost * (.11)
    else:
        serviceCharge = movieCost * (.05)
        
    return serviceCharge


#calcTotalDue
#calcTotalDue calculates the total cost due for the movies
#Parameters:
#   1. Cost of the movies
#   2. Service charge
#
#Returns: the total with tax.

def calcTotalDue(costmovie,theservicecharge):
   
    totalDue = costmovie + theservicecharge
    taxDue = totalDue * (.07)
    totalDuewithTax = totalDue + taxDue

    return totalDuewithTax


#outputResults
#outputResults prints all of the information that is accumulated in the program to the screen
#Parameters:
#   1. Customer name
#   2. Custome ID
#   3. Number of movies purchased
#   4. Total Cost
#   5. Service Charge
#   6. Total Amount Due
#
#Returns: All of the information listed in the parameters.

def outputResults(custname, custID, movienumber,costofmovies,servCharge,totalDue):
    print("Customer: ", custname)
    print(custID)
    print("Bought" , movienumber, "movies")
    print("The total cost of the movies is: $" , round(costofmovies, 2))
    print("The service charge for the movies is: $", round(servCharge,2))
    print("The total amount due for all the movies is: $", round(totalDue,2))

main()



