# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.


def get_list():
    updated_list = []
    while True:
        value = input("Enter a value (press Enter to stop): ")
        if value=="":
            break
        updated_list.append(value)
    print("The updated list is", updated_list)

get_list()
