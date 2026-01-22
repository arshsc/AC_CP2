# AC 2nd Random Password Generator

# variables
lowercases_required = False
uppercases_required = False
numbers_required = False
special_characters_required = False

password = []

# lists
#lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#numbers = []

# functions
def intro():
    print("Random Password Generator\n\nPlease type corresponding number for menu choices or if needed, \"Y\" for Yes or \"N\" for No.")

def main_menu():
    choice = input("\nType the number for the action you would like to perform\n\n1. Generate Passwords\n\n2. Exit\n\n").strip()
    return choice

def generate_password(lowercases_required, uppercases_required, numbers_required, special_characters_required):

    def requirement(option, option_required):
        while True:
            required = input(f"\nDoes the password need {option} letters (Y/N): ").strip().upper()

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
            
    while True:
        length = input("\nHow long does the password need to be: ").strip()
        if length.isdigit():
            return length
        elif length.isdigit() == False:
            print("\nInvalid choice, please retry.")
    
    requirement("lowercase", lowercases_required)
    requirement("uppercase", uppercases_required)
    requirement("number", numbers_required)
    requirement("special_character", special_characters_required)

def length(password, length):
    if length == True:
        password = ["X"] * 5
        return password


def main(lowercases_required, uppercases_required, numbers_required, special_characters_required, password, length):
    intro()

    while True:

        choice = main_menu()

        if choice == "1":
            generate_password(lowercases_required, uppercases_required, numbers_required, special_characters_required)
            length()
        elif choice == "2":
            print("\nExiting...")
        else:
            print("\nInvalid choice, please retry.")


main(lowercases_required, uppercases_required, numbers_required, special_characters_required, password, length)