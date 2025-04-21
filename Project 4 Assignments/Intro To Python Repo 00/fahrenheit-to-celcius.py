def fahrenheit(temp):
    result = (temp - 32)*5.0/9.0
    print(f"Temperature: {temp}F = {result}C")
temperature = int(input("Enter temperature in Fahrenheit: "))
fahrenheit(temperature)