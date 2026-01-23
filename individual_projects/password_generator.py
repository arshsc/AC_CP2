# AC 2nd Random Password Generator


# libraries
import random
import string


# variables
length = 0
lowercases_required = False
uppercases_required = False
numbers_required = False
special_characters_required = False

password = []


# functions
def intro():
    print("Random Password Generator\n\nPlease type corresponding number for menu choices or if needed, \"Y\" for Yes or \"N\" for No.")

def main_menu():
    choice = input("\nType the number for the action you would like to perform\n\n1. Generate Passwords\n\n2. Exit\n\n").strip()
    return choice

def requirement(prompt, option_required):
    while True:
        required = input(f"\n{prompt}").strip().upper()

        if required == "Y" or "N":
            if required == "Y":
                option_required = True
                return option_required
            elif required == "N":
                option_required = False
                return option_required
            break
        else:
            print("\nInvalid choice, please retry.")

def password_length(password, length):
    for i in range(length):
        random_number = random.randint(65, 90)
        random_letter = chr(random_number)
        password.append(random_letter)
    return password


def main(password, length, lowercases_required = False, uppercases_required = False, numbers_required = False, special_characters_required = False):


    intro()

    while True:
        print(password)
        print(length, lowercases_required, uppercases_required, numbers_required, special_characters_required)

        choice = main_menu()

        if choice == "1":
            while True:
                length = input("\nHow long does the password need to be: ").strip()
                if length.isdigit():
                    length = int(length)
                    break
                elif length.isdigit() == False:
                    print("\nInvalid choice, please retry.")
            lowercases_required = requirement("Does the password need lowercase letters (Y/N): ", lowercases_required)
            uppercases_required = requirement("Does the password need uppercase letters (Y/N): ", uppercases_required)
            numbers_required = requirement("Does the password need numbers (Y/N): ", numbers_required)
            special_characters_required = requirement("Does the password need special characters (Y/N): ", special_characters_required)

            password = password_length(password, length)

        elif choice == "2":
            print("\nExiting...")

        else:
            print("\nInvalid choice, please retry.")



main(password, length, lowercases_required, uppercases_required, numbers_required, special_characters_required)