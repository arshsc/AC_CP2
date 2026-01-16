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
    choice = input("\n\nType the number for the action you would like to perform\n\n1. View Movies\n\n2. Add a Movie\n\n3. Remove a Movie\n\n4. Search for a Movie\n\n5. Exit Movie Library\n\n")
    return choice

# view
def view(movies_list):
    print("\n")
    for movie, director in movies_list:
        print(f"\n{movie} directed by {director}")

# add
def add(movies_list):
    movie = input("\n\nTitle: ")
    director = input("\nDirected by: ")

    movies_list.append((movie, director))

    print(f"\nSucessfully Added\n\n{movie} directed by {director}")

# remove FIX
def remove(movies_list):
    count = 0

    print("\n")

    for movie, director in movies_list:
            count += 1
            print(f"\n{count}. {movie} directed by {director}")

    while True:
        movie_remove = input("\nEnter the number of the movie you would like to remove: ").strip()

        if movie_remove.isdigit() == False:
            print("\n\nInvalid choice, please retry.\n")
        elif movie_remove.isdigit() == True:
            movie_remove = int(movie_remove)
            movie_remove -= 1
            movie = movies_list[movie_remove][movie_remove]
            movie_remove -= 1
            director = movies_list[movie_remove][movie_remove]
            print(f"\n\nYou have removed {movie} by {director}")
            movies_list.pop(movie_remove)
            break

# search FIX
def search():
    while True:
        search_by = input("\n\nWhat would you like to search by?\n\n1. Movie\n\n2. Director\n\n")

        if search_by == "1":
            searching = input("\n\nWhat is the movie's name: ")
            return searching
        elif search_by == "2":
            searching = input("\n\nWhat is the director's name: ")
            return searching
        
        else:
            print("\n\nInvalid choice, please retry.")

# main code
def main(movies_list):
    print("\nYour Movie Library with Directors")

    while True:
        choice = main_menu().strip()

        if choice == "1":
            view(movies_list)
        
        elif choice == "2":
            add(movies_list)
        
        elif choice == "3":
            remove(movies_list)
        
        elif choice == "4":
            searching = search(movies_list)
            print(searching)

            if searching in movies_list:
                for movie, director in movies_list:
                    if movie == searching or director == searching:
                        print(f"\n{movie} by {director}")


        elif choice == "5":
            print("\nExiting...\n")
            break
        
        else:
            print("\n\nInvalid choice, please retry.")


main(movies_list)