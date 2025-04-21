def calculate_perimeter(side1,side2,side3):
    result = side1+side2+side3
    print(f"The perimeter of the triangle is {result}")

first_side = float(input(f"Enter Length of Side 1 : "))
second_side = float(input(f"Enter Length of Side 2 : "))
third_side = float(input(f"Enter Length of Side 3 : "))
calculate_perimeter(first_side,second_side,third_side)