# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def cal_inches(feet):
    INCHES : int = 12
    result : int = feet*INCHES
    print(f"There are {result} inches in {feet} feet")

feet = int(input("Enter Feet : "))
cal_inches(feet)