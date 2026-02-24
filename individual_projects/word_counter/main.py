# AC 2nd Word Counter

# libaries
from file_handling import *

# variables
default_file_path = "individual_projects/word_counter/docs/document.txt"
file_path = ""

# functions
def menu():
    print("\n--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice in ["1", "2", "3"]:
        if file_path == "":
            user = input("\nEnter the exact file path for your document (press Enter for default): ").strip()

            if user == "":
                file_path = default_file_path
            else:
                file_path = user

    if choice == "1":
        update_document(file_path)

    elif choice == "2":
        view_document(file_path)

    elif choice == "3":
        add_content(file_path)

    elif choice == "4":
        print("\nExiting...")
        break

    else:
        print("\nInvalid choice.")