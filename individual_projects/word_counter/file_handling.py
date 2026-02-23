"""# AC 2nd Text File Editing for Word Counter

from time_handling import get_current_time
    
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


def view_document():
    try:
        print("\nDocument content: ")
        with open(file_path, "r") as file:
            for line in file:
                print(line, end='')
            print("\n")
    except:
        print(f"The file '{file_path}' was not found.")


def add_content():
    new_content = input("\nEnter new content (press Enter twice to finish):\n")
    try:
        with open(file_path, "a") as file:
            file.write("\n", new_content)
    except:
        print(f"The file '{file_path}' was not found.")"""