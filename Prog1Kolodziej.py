# Name: Bobby Kolodziej

# File Prog1Kolodziej.py

# Purpose: This is a program that converts celcius temperatures to Fahrenheit temperatures.

# Input: The input value in this program is the temperature in Celcius

# Output: The ouput variable in this program is the temperature in Fahrenheit

# Certification of Authenticity:
    # I certify that this lab is entirely my own work

def main():
    print("This program converts Celcius to Fahrenheit")
    # Repeat 5 times before quitting
    for i in range(5):
        # input the temp in Celcius
        celcius = float(input("Enter the temperature in Celcius: "))
        # calculate the value of Fahrenheit
        fahrenheit = (9/5) * celcius + 32
        # output the results
        print("The temperature is", fahrenheit, "degrees Fahrenheit")

main()
    
