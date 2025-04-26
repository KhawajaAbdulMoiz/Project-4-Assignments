# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.


def remainder_cal():
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))

    quotient: int = num1 // num2 
    remainder: int = num1 % num2  
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
remainder_cal()

