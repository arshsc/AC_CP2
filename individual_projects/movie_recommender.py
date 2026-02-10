# AC 2nd Movie Reccomender

# import need libraries
import csv

# functions
# intro
def intro():
    print("\nWelcome to Movie Recommender!\n\nSearch for movies by genre, director, actor, and/or length.\n")

# main menu
def main_menu():
    return input("\nType the number for the action you would like to perform:\n\n1. Search / Get Recommendations\n2. Print Full Movie List\n3. Exit\n\n")

# search
def search():
    while True:
        # ask for filters, strip it, then validate the input
        filters = input("\nChoose filters to apply (enter numbers separated by commas, e.g., '1,3')\n\n1. Genre\n2. Director\n3. Actor\n4. Length (min/max)\n\nSelected Filters: ").split(",")
        filters = [f.strip() for f in filters]

        valid_options = {"1", "2", "3", "4"}
        if all(f in valid_options for f in filters):
            break
        else:
            print("\nInvalid filter selection. Please enter numbers from 1 to 4 separated by commas.")

    # set all filters to none / 0
    genre = director = actor = None
    min_len = max_len = 0

    # ask for genre
    if "1" in filters:
        genre = input("Enter genre: ").strip().lower()

    # ask for director
    if "2" in filters:
        director = input("Enter director name: ").strip().lower()
    
    # ask for actor
    if "3" in filters:
        actor = input("Enter actor name: ").strip().lower()
    
    if "4" in filters:
        while True:
            # ask for min length then validate
            min_input = input("Enter minimum length (or leave blank): ").strip()
            if min_input == "" or min_input.isdigit():
                min_len = int(min_input) if min_input.isdigit() else 0
                break
            else:
                print("\nInvalid input. Please enter a number or leave blank.")
        while True:
            # ask for max length then validate
            max_input = input("Enter maximum length (or leave blank): ").strip()
            if max_input == "" or max_input.isdigit():
                max_len = int(max_input) if max_input.isdigit() else 0
                break
            else:
                print("\nInvalid input. Please enter a number or leave blank.")

    # if movie wasnt found
    found = False
    # file needs to be open to work, then it looks through the file to find each of the filters
    try:
        with open("individual_projects/movie_list.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) < 6:
                    continue
                if match_movie(row, genre, director, actor, min_len, max_len):
                    print_movie(row)
                    found = True
    # if movie list doesnt work
    except:
        print("\nMovie list file not found.")

    # if it isnt found
    if not found:
        print("\nNo movies match those filters.")

# checks if a movie row matches all the filters
def match_movie(row, genre, director, actor, min_len, max_len):
    row_genres = [g.strip().lower() for g in row[2].split(",")]
    row_actors = [a.strip().lower() for a in row[5].split(",")]

    if genre and not any(genre in g for g in row_genres):
        return False
    if director and director not in row[1].strip().lower():
        return False
    if actor and not any(actor in a for a in row_actors):
        return False

    try:
        length = int(row[4])
    except:
        return False

    if min_len != 0 and length < min_len:
        return False
    if max_len != 0 and length > max_len:
        return False

    return True

# to print a movie in consistent format
def print_movie(row):
    print(f'\nTitle: "{row[0]}" -- Director: {row[1]} -- Genre: {row[2]} -- Rating: {row[3]} -- Length: {row[4]} min -- Notable Actors: {row[5]}')

# print the movies
def print_movies():
    try:
        with open("individual_projects/movie_list.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) < 6:
                    continue
                print_movie(row)
    except:
        print("Can't find that file")

# main function
def main():
    # call the intro
    intro()
    # while true to keep it running
    while True:
        # choice from main menu
        choice = main_menu()
        # search function
        if choice == "1":
            search()
        
        # print all movies
        elif choice == "2":
            print_movies()

        # exit the program
        elif choice == "3":
            print("\nExiting...")
            break
            
        # if no input is valid
        else:
            print("\nInvalid choice. Please try again.")

# call main function
main()
