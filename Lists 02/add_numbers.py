# Write a function that takes a list of numbers and returns the sum of those numbers.

def add(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

list : int = [5,8,5,2,4]
result = add(list)
print(f"The sum of the numbers : {result}")