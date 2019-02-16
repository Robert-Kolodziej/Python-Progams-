from SavingsAccount import Savingsaccount

def main():
    print("Welcome to the First National Bank")
    newAccount = Savingsaccount("Bobby", "1234", 3000.00)
    print(newAccount)

    newAccount2 = ("Sean" , "4321")
    print(newAccount2)

    print("Deposit $300 into each account")
    newAccount.deposit(300)
    newAccount2.deposit(300)
    print(newAccount)
    print(newAccount2)

    print("Create a new account")
    theName = input("Enter the account holder's name: ")
    thePin = input("Enter the new PIN: ")
    theAmount = float(input("Enter the initial deposit amount: "))
    newAccount3 = Savingsaccount(theName, thePin, theAmount)
    print(newAccount3)
main()
    
