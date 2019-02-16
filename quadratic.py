#File quadratic.py
#By Bobby Kolodziej
#test data (a=1, b=4, c=4) and (a=1, b=0, c=-9) 
import math 
def main():
    #input the values for a,b,c
    a=int(input("give a value for a "))
    b=int(input("give a value for b "))
    c=int(input("give a value for c "))
    discroot=math.sqrt(b**2-4*a*c)
    root1=(-b+discroot)/(2*a)
    root2=(-b-discroot)/(2*a)
    print ("The value for Root1 is: ", root1)
    print ("The value for Root2 is: ", root2)
    
main()
