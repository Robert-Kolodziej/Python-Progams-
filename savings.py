"""
File: savingsaccount.py
This module defines the SavingsAccount class.
"""

class SavingsAccount:
    """This class represents a savings account with the owner's
        name,PIN, and balance. """
    RATE = 0.02     # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        self.myName = name
        self.myPin = pin
        self.myBalance = balance


    def __str__(self):
        """Returns the string rep."""
        ans = "Name: " + self.myName + "\n"
        ans = ans + "Pin: " + self.myPin +"\n"
        ans = ans + "Balance: " + self.myBalance

        return ans
    
    def getBalance(self):
        """Returns the current balance."""
        return self.myBalance

    def getName(self):
        """Returns the current name."""
        return self.myName

    def getPin(self):
        """Returns the current pin."""
        return self.myPin

    def setName(self, newName):
        """Sets the name for the account."""
        

    def setBalance(self, newAmount):
        """Sets the balance for the account."""

    def setPin(self, newCode):
        """Sets the PIN for the account."""

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""

    def withdraw(self, amount):
        """If the amount is valid, subtract it
        from the balance and returns None;
        otherwise, returns an error message."""
    

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
