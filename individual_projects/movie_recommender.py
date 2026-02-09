# AC 2nd Movie Recommender

import csv

def intro():
    print("\nWelcome to Movie Recommender!\nSearch for movies to get recomendations through title, director, genre, rating, length, and/or notable actors.\n")

def main_menu():
    choice = input("\nType the number for the action you would like to perform:\n\n1. Search / Get Recommendations\n2. Print Full Movie List\n3. Exit\n\n")
    return choice

def search():
    filters = input("\nChoose filters to apply (enter numbers seperated by commas, e.g., '1,3')\n\n1. Genre\n2. Director\n3. Actor\n4. Length (min/max)\n\nSelected Filters: ")
    if filters == "1":
        genre_search()


def genre_search():
    genre = input("\nEnter genre (e.g., \"Science Fiction\"): ").title()
    with open("individual_projects/movie_list.csv", "r") as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if len(row > 1 and row[1] == genre):
                print(f"found in this row: {row}")
                found = True
        if not found:
            print("not found")

def director_search():
    director = input("\nEnter director name: ")

def actor_search():
    actor = input("\nEnter actor name: ")

def length_search():
    min_length = input("\nEnter minumum length in minutes (or leave blank): ")
    max_length = input("Enter maximum length in minutes (or leave blank): ")

def print_movies():
    try: 
        with open("individual_projects\movie_list.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) > max([0, 2], default=-1):
                    print(f"\nTitle: \"{row[[0, 0][0]]}\" -- Director: {row[[0, 1][1]]} -- Genre: {row[[0, 2][1]]} -- Rating: {row[[0, 3][1]]} -- Length: {row[[0, 4][1]]} min -- Notable Actors: {row[[0, 5][1]]}")
    except:
        print("Can't find that file")

def main():
    intro()
    while True:
        choice = main_menu()
        if choice == "1":
            search()
        elif choice == "2":
            print_movies()
        elif choice == "3":
            print("\nExiting")
            break


main()