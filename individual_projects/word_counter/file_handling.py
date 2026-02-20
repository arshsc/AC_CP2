# AC 2nd Text File Editing for Word Counter

from time_handling import get_current_time

def get_file_path():
    if file_path == "":
        new_file_path = input("\nEnter the exact file path for your document: ").strip()
        if new_file_path == "":
            file_path = 'individual_projects/word_counter/docs/document2.txt'
        return file_path
    
def update_document(file_path):
    try:
        with open(file_path, "a") as file:
            current_time = get_current_time()
            text = file.read()
            words = text.split()
            word_count = len(words)
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