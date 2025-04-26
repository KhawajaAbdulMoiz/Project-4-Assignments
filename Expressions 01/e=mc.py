# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

C : int = 299792458  # Speed of light 

def cal():
    mass: float = float(input("Enter mass in kg: "))
    energy: float = mass * (C ** 2)
    print(str(energy) + " joules of energy!")
cal()