##Bobby Kolodziej
##
##file Prog9bKolodziej.py
##
##Input: The input for this program comes from the file being read
##
##Output: The output is the information from the file printed to the screen in a list.
##
## Certification of authority
## I certify that this lab is entirely my own work but I communicated with Charlie Schmitz and sean Kohler.

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
def printList(listofItems):
    print("Quantity" + "\t" + "Name" + "\t" + "\t" + "Unit Price")
    for i in range(len(listofItems)):
        print(listofItems[i])
    
def main():
    print("Provide information about an item")
    items = getList()    
    printList(items)

main()    
