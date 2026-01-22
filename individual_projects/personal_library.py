# AC 2nd Personal Library


# list with tuples
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
    # display options
    choice = input("\n\nType the number for the action you would like to perform\n\n1. View Movies\n\n2. Add a Movie\n\n3. Remove a Movie\n\n4. Search for a Movie\n\n5. Exit Movie Library\n\n")
    return choice

# view
def view(movies_list):
    print("\n")
    # display all movies if movies are there
    if movies_list:
        for movie, director in movies_list:
            print(f"\n{movie} directed by {director}")
    # if no movies are in list
    elif not movies_list:
            print("\nThere are no movies in the library. Please add a movie or exit.")

# add
def add(movies_list):
    # ask for movie name
    movie = input("\n\nTitle: ")
    # ask for director name
    director = input("\nDirected by: ")

    # append the movie and director
    movies_list.append((movie, director))

    # inform the user it was added
    print(f"\nSuccessfully Added: {movie} directed by {director}")

# remove
def remove(movies_list):
    # to number each movie
    count = 0

    print("\n")
    # print each movie with number
    for movie, director in movies_list:
            count += 1
            print(f"\n{count}. {movie} directed by {director}")

    while True:
        # to make sure there are movies in the list
        if movies_list:
            movie_remove = input("\n\nEnter the number of the movie you would like to remove: ").strip()

            # check to make sure it is a valid input
            if movie_remove.isdigit() == False:
                print("\n\nInvalid choice, please retry.\n")
            elif movie_remove.isdigit() == True:
                movie_remove = int(movie_remove)
                
                # to account for index number
                if len(movies_list) >= movie_remove:
                    movie_remove -= 1

                    # movie being removed
                    for movie,director in movies_list:
                        movie = movies_list[movie_remove][0]
                        director = movies_list[movie_remove][1]
                    
                    # inform the user it is removed now
                    print(f"\n\nYou have removed {movie} by {director}")
                    movies_list.pop(movie_remove)
                    break
                
                # if the input is invalid
                elif len(movies_list) < movie_remove:
                    print("\n\nInvalid choice, please retry.")
                    
        # if there are no movies in the list
        elif not movies_list:
            print("\nThere are no movies in the library. Please add a movie or exit.")
            break

# search
def search(movies_list):
    while True:
        # search by movie or director
        search_by = input("\n\nWhat would you like to search by?\n\n1. Movie\n\n2. Director\n\n")

        # search by movie
        if search_by == "1":
            searching = input("\n\nWhat is the movie's name: ").strip().lower()
            found = False
            # if movie is found
            for movie, director in movies_list:
                if searching in movie.lower():
                    print(f"\n{movie} directed by {director}")
                    found = True
            # if no movie is found
            if not found:
                print("\nNo matching movies found.")
                
            break
        
        # search by director
        elif search_by == "2":
            searching = input("\n\nWhat is the director's name: ").strip().lower()
            found = False
            # if movie is found
            for movie, director in movies_list:
                if searching in director.lower():
                    print(f"\n{movie} directed by {director}")
                    found = True
            # if no director is found
            if not found:
                print("\nNo matching directors found.")

            break
        # if no other choice is valid
        else:
            print("\n\nInvalid choice, please retry.")


# main code
def main(movies_list):
    # introduction
    print("\nYour Movie Library with Directors")
    # to keep running
    while True:
        # call the main menu function
        choice = main_menu().strip()
        # call the view function
        if choice == "1":
            view(movies_list)
        # call the add function
        elif choice == "2":
            add(movies_list)
        # call the remove function
        elif choice == "3":
            remove(movies_list)
        # call the search function
        elif choice == "4":
            search(movies_list)
        # exit the program
        elif choice == "5":
            print("\nExiting...\n")
            break
        # if no other choice is valid
        else:
            print("\n\nInvalid choice, please retry.")


# calling main code function
main(movies_list)