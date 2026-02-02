# AC 2nd Simple Morse Code Translator

# lists
english = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", "...-", ".--", "-..-", "-.--", "--..")

def main_menu():
    choice = input("\n1. Translate from Morse code to English\n\n2. Translate from English to Morse Code\n\n3. Exit\n\n")
    return choice

def morse_code_english():
    pass

def english_morse_code():
    message = input("What is the code you need translated")

def main():
    choice = main_menu()

    if choice == "1":
        morse_code_english()
    elif choice == "2":
        english_morse_code()

