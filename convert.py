# File convert.py
# A program to convert Celcius temperatures to Fahrenheit Temperatures
# by Bobby Kolodziej

def main():
    # input the temp in Celcius
    celcius = eval(input("Enter the temperature in Celcius"))

    # calculate the value of Fahrenheit
    fahrenheit = (9/5) * celcius + 32

    # output the results
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

main()
    
