##Bobby Kolodziej
##
##file Prog10Kolodziej.py
##
##Input: The input for this program comes from the file being read and also the input
##      from the user. 
##
##Output: The output is the information from the file printed to the screen in a list.
##
## Certification of authority
## I certify that this lab is entirely my own work. But I comunicated with the programming lab. 

from itemKolodziej import ItemKolodziej

##File being read: inputItem.txt

def getList():
    inputFile = input("Enter the file name for the input file: ")
    theFile = open(inputFile, 'r')
    numItems = theFile.readline()
    count = 1
    itemList=[]
    for item in numItems:
        quantity = theFile.readline().strip()
        name = theFile.readline().strip()
        price = theFile.readline().strip()
        count+= 1
        newItem = ItemKolodziej(quantity, name, price)
        itemList.append(newItem)
    return itemList

## Add an item
def addItem(itemsList):
    quant = int(input("Enter the quantity of the new item: "))
    itemName = input("Enter the item name: ")
    itemPrice = float(input("Enter the price of the item: "))
    new = ItemKolodziej(quant, itemName, itemPrice)
    itemsList.append(new)
    return itemsList

## Print the list
def printList(listofItems):
    if listofItems == []:
        print("The list is empty")
    else:
        print("Quantity" + "\t" + "Name" + "\t" + "\t" + "Unit Price")
        for i in range(len(listofItems)):
            print(listofItems[i])

## Search for an item
def searchItem(theitemList):
    itemSearch = input("Enter the name of the item you are looking for: ")
    for item in theitemList:
        if item.getName() == itemSearch:
            print("Yes," , itemSearch, "is in the list, you have", str(item.getQuantity()), "at a price of $", str(item.getPrice()))
            return 

        else:
            print("This item is not in the list")

## Count Item
def countItems(listItems):
    count = 0
    for items in listItems:
        itemQuant = items.getQuantity()
        count+= itemQuant
    print("There are", count, "items in the list")

## Total cost
def totalCost(totalItems):
    costofallItems = 0
    for item in totalItems:
        totalQuant = item.getQuantity()
        totalPrice = item.getPrice()
        costofallItems = totalQuant * totalPrice
    print("The total price of the list is: $" , costofallItems)

## Is the list empty?
def emptyList(fullList):
    listofItems = fullList
    if listofItems == []:
        print("The list is empty")
    else:
        print("No, the list is not empty")
        printList(fullList)

## Clear the list
def clearList(itemList):
    listofItems = itemList
    listofItems = []
    return listofItems

                      
def main():
    print("Provide information about an item")
    items = getList()
    userChoice = "-1"

    while userChoice != "0":
    
        print("\n")
        print("1. Add an item to the list")
        print("2. Delete an item from the list")
        print("3. Print the items in the list")
        print("4. Search for user specific item in the list")
        print("5. Count the total number of items in the list")
        print("6. Total the cost of the items in the list")
        print("7. Determine if the list is empty")
        print("8. Clear the list")
        print("0. Quit" + "\n")

        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            addItem(items)
        elif userChoice == "2":
            print("Did not do the challenge")
        elif userChoice == "3":
            printList(items)
        elif userChoice == "4":
            searchItem(items)
        elif userChoice == "5":
            countItems(items)
        elif userChoice == "6":
            totalCost(items)
        elif userChoice == "7":
            emptyList(items)
        elif userChoice == "8":
            items = clearList(items)
        elif userChoice == "0":
            print("Goodbye")
        else:
            print("Invalid Choice. Try again")

main()    
