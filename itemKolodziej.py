"""
File: itemKolodziej.py

This class creates an item and asks for the pice and quantity of the items.

"""
class ItemKolodziej:
    """This class represents items"""

    def __init__(self, quantity, name, price):
        self.myQuantity = int(quantity)
        self.myName = name
        self.myUnitPrice = float(price)

    def setQuantity(self, newQuantity):
        """Sets the quantiry of the item"""
        self.myQuantity = newQuantity

    def setName(self, newName):
        """Sets the name of the item"""
        self.myName = newName

    def setPrice(self, newPrice):
        """sets the price of the item"""
        self.myUnitPrice = newPrice

    def getQuantity(self):
        """Returns the quantity of the items"""
        return self.myQuantity

    def getName(self):
        """Returns the name of the item"""
        return self.myName

    def getPrice(self):
        """Returns the price of the item"""
        return self.myUnitPrice

    def __str__(self):
        """Returns the string representation of the item"""
        ans= str(self.myQuantity) + "\t" +"\t" + str(self.myName) +"\t" +"\t" + "$" + str(self.myUnitPrice)

        return ans
