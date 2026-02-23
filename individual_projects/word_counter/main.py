# AC 2nd Word Counter

from file_handling import *
from datetime import datetime

def get_current_time():
    current_datetime = datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")

file_content = ""

file_path = input("Enter library file path or press Enter for default: ").strip()
if file_path == "":
    file_path = "individual_projects/word_counter/docs/document.txt"

def file_path_to_string():
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except:
        print(f"Error: The file '{file_path} was not found.")

def update_document():
    try:
        with open(file_path, "a") as file:
            current_time = get_current_time()
            text = file.read()
            words = text.split()
            word_count = len(words)
            file.write(f"\n\n Word Count: {word_count}\nLast Updated: {current_time}")
    except:
        print(f"The file '{file_path}' was not found.")



# main file
def main_menu():
    choice = input("\n--- Document Word Count Updater ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4): ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            update_document()

main()



