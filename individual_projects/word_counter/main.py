# AC 2nd Word Counter

from file_handling import *

# main file
def main_menu():
    choice = input("\n--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4): ")
    return choice


def main():
    file_path = ''
    while True:
        choice = main_menu()
        if choice == "1":
            if file_path == "":
                file_path = input("\nEnter the exact file path for your document: ").strip()
                if file_path == "":
                    file_path = 'individual_projects/word_counter/docs/document2.txt'
                elif file_path:
                    file_path = file_path
            elif file_path:
                update_document(file_path)

            update_document(file_path)
        elif choice == "2":
            view_document(file_path)
        elif choice == "3":
            add_content(file_path)

main()



