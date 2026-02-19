# AC 2nd Text File Editing for Word Counter

from time import get_current_time

def update_document():
    if file_path == "":
        file_path = input("\nEnter the exact file path for your document: ").strip()
        if file_path == "":
            file_path = "individual_projects/word_counter/docs/document.txt"
        return file_path
    elif file_path:
        try:
            with open(file_path, "a") as file:
                current_time = get_current_time()
                file.write(f"\n\n Word Count: {word_count}\nLast Updated: {current_time}")
        except:
            print(f"The file '{file_path}' was not found.")

def view_document(file_path):
    try:
        print("\nDocument content: ")
        with open(file_path, "r") as file:
            for line in file:
                print(line, end='')
            print("\n")
    except:
        print(f"The file '{file_path}' was not found.")

def add_content(file_path):
    new_content = input("\nEnter new content (press Enter twice to finish):\n")
    try:
        with open(file_path, "a") as file:
            file.write("\n", new_content)
    except:
        print(f"The file '{file_path}' was not found.")



# main file
def main_menu():
    choice = input("\n--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4): ")
    return choice


def main():
    file_path = "individual_projects/word_counter/docs/document.txt"
    while True:
        choice = main_menu()
        if choice == "1":
            file_path = update_document()
        elif choice == "2":
            view_document(file_path)
        elif choice == "3":
            add_content(file_path)

main()