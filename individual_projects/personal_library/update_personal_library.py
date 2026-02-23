# AC 2nd Personal Library

# libraries
import csv


# list to store movies
movies_list = []


# ask what file to use or use default if blank
file_path = input("Enter library file path or press Enter for default: ").strip()
if file_path == "":
    file_path = "individual_projects/library.csv"


# functions
# load the library
def load_library():
    # clear movie list first
    movies_list.clear()
    # open the file and append it to movies list
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie = {"Title": row["Title"], "Director": row["Director"], "Year": row["Year"], "Genre": row["Genre"]}
                movies_list.append(movie)

    except:
        print(f"\nFile '{file_path}' not found. Starting with empty library.")

# save library
def save_library():
    # write to the file to update it
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Director", "Year", "Genre"])
            writer.writeheader()
            writer.writerows(movies_list)
        print(f"\nLibrary saved successfully to '{file_path}'.")

    except:
        print("\nError saving the library.")


# main menu
def main_menu():
    choice = input("\n\nType the number for the action you would like to perform\n\n1. Show Simple List\n2. Show Detailed List\n3. Add a Movie\n4. Update a Movie\n5. Delete a Movie\n6. Save Library\n7. Reload Library from File\n8. Exit\n\nChoice: ")
    return choice

# simple view of movies
def view_simple(movies_list):
    print("\n")
    if movies_list:
        # go through each movie to print title and director
        for count, movie in enumerate(movies_list, start=1):
            print(f"{count}. {movie['Title']} directed by {movie['Director']}")
    else:
        print("There are no movies in the library.")

# detailed view of movies
def view_detailed(movies_list):
    print("\n")
    if movies_list:
        # go through each movie and print title, director, year, and genre
        for count, movie in enumerate(movies_list, start=1):
            print(f"\n{count}. Title: {movie['Title']}\n   Director: {movie['Director']}\n   Year: {movie['Year']}\n   Genre: {movie['Genre']}")
    else:
        print("There are no movies in the library.")

# add movie
def add(movies_list):
    # ask for the movie info
    print("\nEnter movie details:")
    title = input("Title: ").strip()
    director = input("Director: ").strip()

    # to validate year as nubmer
    while True:
        year = input("Year: ").strip()
        if year.isdigit() or year == "":
            break
        print("Please enter a valid number for year.")

    genre = input("Genre: ").strip()

    # need valid inputs
    if not title or not director or not genre:
        print("\nInvalid input. Title, Director, and Genre are required.")
        return

    # append to movie list
    movies_list.append({"Title": title, "Director": director, "Year": year, "Genre": genre})
    print(f"\nSuccessfully Added: {title}")

# update movie
def update(movies_list):
    # check if there are movies to update
    if not movies_list:
        print("\nNo movies to update.")
        return

    # view all movies and ask which one they want to update
    view_simple(movies_list)
    choice = input("\nEnter the number of the movie to update: ").strip()

    # validate input
    if not choice.isdigit():
        print("\nInvalid choice.")
        return

    # turn number into index and make sure it is valid 
    index = int(choice) - 1
    if index < 0 or index >= len(movies_list):
        print("\nInvalid choice.")
        return

    # get correct movie
    movie = movies_list[index]
    print("\nLeave blank to keep current value.")

    # ask for each category what they want to change it to
    title = input(f"Title ({movie['Title']}): ").strip()
    director = input(f"Director ({movie['Director']}): ").strip()

    # make sure year is a number
    while True:
        year = input(f"Year ({movie['Year']}): ").strip()
        if year.isdigit() or year == "":
            break
        print("Please enter a valid number for year.")

    genre = input(f"Genre ({movie['Genre']}): ").strip()

    # if empty, keep the same
    if title != "":
        movie["Title"] = title
    if director != "":
        movie["Director"] = director
    if year != "":
        movie["Year"] = year
    if genre != "":
        movie["Genre"] = genre

    print("\nMovie updated successfully.")

# remove
def remove(movies_list):
    # check if there are movies to delete
    if not movies_list:
        print("\nNo movies to delete.")
        return

    # view all movies and ask which one they want to delete
    view_simple(movies_list)
    choice = input("\nEnter the number of the movie to delete: ").strip()

    # validate input
    if not choice.isdigit():
        print("\nInvalid choice.")
        return

    # get correct index and make sure it is valid
    index = int(choice) - 1
    if index < 0 or index >= len(movies_list):
        print("\nInvalid choice.")
        return
    
    # remove the movie with correct index
    removed = movies_list.pop(index)
    print(f"\nRemoved {removed['Title']}")

# main
def main(movies_list):
    # intro
    print("\nYour Movie Library!")
    # load the library
    load_library()

    # to keep running until exit
    while True:
        choice = main_menu().strip()

        # view simple
        if choice == "1":
            view_simple(movies_list)

        # view detailed
        elif choice == "2":
            view_detailed(movies_list)

        # add movie
        elif choice == "3":
            add(movies_list)

        # update movie
        elif choice == "4":
            update(movies_list)

        # remove a movie
        elif choice == "5":
            remove(movies_list)

        # save library
        elif choice == "6":
            save_library()

        # load library
        elif choice == "7":
            load_library()
            print("\nLibrary reloaded.")

        # exit, ask if they want to save before
        elif choice == "8":
            save_choice = input("\nSave before exiting? (y/n): ").lower()
            if save_choice == "y":
                save_library()
            print("\nExiting...\n")
            break
        
        # invalid choice
        else:
            print("\nInvalid choice, please retry.")



# call the main function
main(movies_list)
