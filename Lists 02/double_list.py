# Write a program that doubles each element in a list of numbers

def double():
    numbers: int = [1, 2, 3, 4]
    for i in range(len(numbers)):
        number : int = numbers[i]
        numbers[i] = number*2
    print(numbers)

double()