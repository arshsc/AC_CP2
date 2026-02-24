# AC 2nd Word Counter Main

# libaries
from file_handling import *

# variables
default_file_path = "individual_projects/word_counter/docs/document.txt"
file_path = ""

# functions
# menu
def menu():
    print("\n--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit")

# put in while true loop to keep running
while True:
    # call menu function
    menu()
    # ask for choice
    choice = input("Enter your choice (1-4): ")

    # before they do anything, get file path or resort to default file path
    if choice in ["1", "2", "3"]:
        if file_path == "":
            user = input("\nEnter the exact file path for your document (press Enter for default): ").strip()

            if user == "":
                file_path = default_file_path
            else:
                file_path = user
    # choice 1
    if choice == "1":
        update_document(file_path)

    # choice 2
    elif choice == "2":
        view_document(file_path)

    # choice 3
    elif choice == "3":
        add_content(file_path)

    # choice 4
    elif choice == "4":
        print("\nExiting...")
        break
    
    # if no choice is valid
    else:
        print("\nInvalid choice.")