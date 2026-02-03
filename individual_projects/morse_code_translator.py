# AC 2nd Simple Morse Code Translator


# lists

# english letters
english = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

# morse code
morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")


# functions

# intro
def intro():
    print("\nWelcome to the Morse Code Translator!")

# main menu 
def main_menu():
    choice = input("\n\nChoose an option:\n\n1. Translate from Morse code to English\n\n2. Translate from English to Morse Code\n\n3. Exit\n\n")
    return choice

# morse code to english
def morse_code_english():
    while True:
        message = input("\nWhat is the code you need translated (Morse code symbols only)?\n\n")
        # split the message
        symbols = message.split(" ")

        # no invalid symbols
        invalid_symbols = False 
        
        # go through each symbol in symbols and check if they are valid or not
        for symbol in symbols:
            if symbol != "" and symbol not in morse_code:
                invalid_symbols = True

        # if there is a invalid symbol
        if invalid_symbols:
            print("\n\nInvalid Morse code, please enter your message again using valid Morse code.\n")
        else:
            break
    
    # empty string to add letters too
    result = ""
    # go through each symbol in symbols, keep spaces between the words, find each symbols corresponding letter and add it to result.
    for symbol in symbols:
        if symbol == "":
            result += " "
        else:
            letter = morse_code.index(symbol)
            result += english[letter]

    # print out the final message
    print(f"\nYour message says:\n\n\n{result}")


# english to morse code
def english_morse_code():
    while True:
        message = input("\nWhat is the message you need translated (letters only)?\n\n").lower()
        # no invalid characters
        invalid_chars = False

        # go through each character in message and check if it is valid
        for char in message:
            if char != " " and char not in english:
                invalid_chars = True

        # if there is an invalid character
        if invalid_chars:
            print("\n\nInvalid character detected, please use only letters a-z and spaces.\n")
        else:
            break

    # empty string to add Morse code symbols to
    result = ""
    # go through each character in message
    for char in message:
        if char == " ":
            result += " "  # keep spaces between words
        else:
            letter = english.index(char)
            result += morse_code[letter] + " "

    # print out the final Morse code message
    print(f"\nYour message in Morse code is:\n\n\n{result}")

# main
def main():
    # call intro to introduce the program
    intro()
    while True:
        # get users choice
        choice = main_menu()

        # morse code to english
        if choice == "1":
            morse_code_english()
        # english to morse code
        elif choice == "2":
            english_morse_code()
        # exit
        elif choice == "3":
            print("\nExiting...")
            break
        # if 1 or 2 is not selected
        else:
            print("\n\nInvalid choice, please retry.")

# call main
main()