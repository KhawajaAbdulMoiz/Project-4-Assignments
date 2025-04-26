# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.


def celsius():
    temp : float = float(input("Enter Temprature in Fahrenheit : "))
    result :float = (temp - 32) * 5.0/9.0
    print(f"Temperature: {temp}F = {result} Celsius")

celsius()