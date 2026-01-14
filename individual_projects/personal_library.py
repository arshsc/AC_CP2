# AC 2nd Personal Library


# list
movies_list = [
    ("Jurassic Park", "Steven Spielberg"),
    ("The Shining", "Stanley Kubrick"),
    ("The Dark Knight", "Christopher Nolan"),
    ("Back to the Future", "Robert Zemeckis"),
    ("Iron Man", "Jon Favreau"),
]

# functions
# main menu
def main_menu():
    choice = input("\n\nType the number for the action you would like to perform\n\n1. View\n\n2. Add\n\n3. Remove\n\n4. Search\n\n5. Exit\n\n")
    return choice

# view
def view(movies_list):
    print("\n")
    for movie, director in movies_list:
        print(f"\n'{movie}' directed by {director}")
    print("\n")

# add
def add(movies_list):
    movie = input("\nTitle: ")
    director = input("\nDirected by: ")

    movies_list.append((movie, director))

    print(f"\nSucessfully Added\n\n'{movie}' by {director}")

# search

# remove

# main code

def main(movies_list):
    while True:
        choice = main_menu().strip()

        if choice == "1":
            view(movies_list)
        
        elif choice == "2":
            add(movies_list)


main(movies_list)