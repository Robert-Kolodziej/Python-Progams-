# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
        print("Thisprogram illustrates a chaotic functuion")
        x = eval(input("Enter a number between 0 and 1: "))
        for i in range(10):
            x = 3.9 * x * (1 - x)
            print(i+1,x)

main()
