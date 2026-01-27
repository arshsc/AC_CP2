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

# password as list
password = []


# functions
# intro to explain how to use the program
def intro():
    print("Random Password Generator\n\nPlease type corresponding number for menu choices or if needed, \"Y\" for Yes or \"N\" for No.")

# displays main menu and return the user's choice
def main_menu():
    choice = input("\n\nType the number for the action you would like to perform\n\n1. Generate Passwords\n\n2. Exit\n\n").strip()
    return choice

# get all needed requirements for password, true for yes, false for no
def requirement(prompt, option_required):
    while True:
        required = input(f"\n{prompt}").strip().upper()

        if required == "Y" or required == "N":
            if required == "Y":
                option_required = True
                return option_required
            elif required == "N":
                option_required = False
                return option_required
        else:
            print("\nInvalid choice, please retry.")

# chooses a random character from allowed types until it finds a character that is allowed
def get_random_character(lower, upper, numbers, special):
    while True:
        choice = random.randint(1, 4)

        if choice == 1 and lower:
            return random.choice(string.ascii_lowercase)
        elif choice == 2 and upper:
            return random.choice(string.ascii_uppercase)
        elif choice == 3 and numbers:
            return random.choice(string.digits)
        elif choice == 4 and special:
            return random.choice(string.punctuation)


# assemble the password using the helper function
def password_create(password, length, lower, upper, numbers, special):
    # to avoid appending to old passwords
    password.clear()

    for i in range(length):
        password.append(get_random_character(lower, upper, numbers, special))

    return password

# main calling all functions inside of it and updating variables outside of it
def main(password, length, lowercases_required=False, uppercases_required=False, numbers_required=False, special_characters_required=False):

    # call the intro
    intro()

    while True:
        # call the main menu
        choice = main_menu()

        # 1 to generate passwords
        if choice == "1":
            while True:
                length = input("\nHow long does the password need to be: ").strip()
                if length.isdigit():
                    length = int(length)
                    break
                else:
                    print("\nInvalid choice, please retry.")

            # call all requirement functions to get needed requirements
            lowercases_required = requirement("Does the password need lowercase letters (Y/N): ", lowercases_required)
            uppercases_required = requirement("Does the password need uppercase letters (Y/N): ", uppercases_required)
            numbers_required = requirement("Does the password need numbers (Y/N): ", numbers_required)
            special_characters_required = requirement("Does the password need special characters (Y/N): ", special_characters_required)

            # if password is empty
            if not (lowercases_required or uppercases_required or numbers_required or special_characters_required):
                print("\nAt least one character type must be selected.")
                continue
            
            # display all generated passwords
            print("\nGenerated Passwords:")
            for i in range(4):
                password = password_create(password, length, lowercases_required, uppercases_required, numbers_required, special_characters_required)
                print(f"\n{i+1}. {''.join(password)}")

        # exit the program
        elif choice == "2":
            print("\nExiting...")
            break
        
        # if input was invalid
        else:
            print("\nInvalid choice, please retry.")


# call the main function
main(password, length, lowercases_required, uppercases_required, numbers_required, special_characters_required)
