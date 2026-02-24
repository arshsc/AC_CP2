# file_handler.py

from time_handling import get_current_time


def read_document(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except:
        print("\nFile does not exist.")


def clean_text(text):
    lines = text.split("\n")
    cleaned = []

    for line in lines:
        if "Word Count:" not in line and "Last Updated:" not in line:
            cleaned.append(line)

    return "\n".join(cleaned)


def count_words(text):
    words = text.split()
    return len(words)


def update_document(file_path):
    text = read_document(file_path)

    clean = clean_text(text)
    word_count = count_words(clean)
    time = get_current_time()

    with open(file_path, "w") as file:
        file.write(clean)
        file.write("\n\nWord Count: " + str(word_count))
        file.write("\nLast Updated: " + time)

    print(f"\nDocument updated. Word count: {word_count}")


def view_document(file_path):
    text = read_document(file_path)
    print("\nDocument content:")
    print(text)


def add_content(file_path):
    print("\nEnter new content (press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    new_text = "\n".join(lines)

    with open(file_path, "a") as file:
        file.write("\n" + new_text)

    print("Content added successfully.")