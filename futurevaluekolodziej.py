# file futurevalue.py
# A program that calculates the amount of money in a bank account after 10 years
# By Bobby Kolodziej 
def main():
    print("This program calculates the future")
    print("Value of a 10 year investment")
    # Input the initail principal
    principal = eval(input("Enter the initail principal: "))
    # Input the annual interest rate
    apr = eval(input("enter the annual interest rate: "))
    # Repeat 10 times 
    for i in range(10):
        # calculate the principal
        principal = principal * (1+apr)
        # output the value of principal at the end of 10 years
        print("The value in", i+1," years is:", principal)
main()
