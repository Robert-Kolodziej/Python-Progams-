##File: Prog9a.py
##
##Bobby Kolodziej
## Certification of authority
## I certify that this lab is entirely my own work but i communicated with Charlie Schmitz

from itemKolodziej import ItemKolodziej

def getList():
    numItems = int(input("Enter the number of items in the list: "))
    count = 1
    itemList=[]
    for item in range(numItems):
        quantity = int(input("Enter the quantity of your item " + str(count) +": "))
        name = input("Enter the name of item "+ str(count) + ": ")
        price = float(input("Enter the price of the item " + str(count) +": "))
        count+= 1
        newItem = ItemKolodziej(quantity, name, price)
        itemList.append(newItem)
    return itemList
def printList(listofItems):
    for i in range(len(listofItems)):
        print(listofItems[i])
    
def main():
    print("Provide information about an item")
    items = getList()    
    printList(items)

main()        
