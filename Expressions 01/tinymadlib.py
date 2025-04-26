# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def madlib():
    adj : str = str(input("Enter an Adjective : "))
    noun : str = str(input("Enter a Noun : "))
    verb : str = str(input("Enter a Verb : "))
    print(f"The {adj} {noun} outsmarted everyone and {verb} away like a legend")

madlib()