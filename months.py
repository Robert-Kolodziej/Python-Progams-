# months program
def main():
     datestr=input("Enter as mm/dd/yyyy: ")
     #datestr.split("/")
     monthstr,daystr,yearstr=datestr.split("/")
     month=int(monthstr)
     months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
     month=months[month-1]
     datestr=month + " " + daystr + ", " + yearstr
     print("The date is: ", datestr)
main()
