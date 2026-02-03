# AC 2nd Movie Recommender

import csv

def intro():
    print("\nWelcome to Movie Recommender!\nSearch for movies to get recomendations through title, director, genre, rating, length, and/or notable actors.\n")

def main_menu():
    choice = input("\nType the number for the action you would like to perform:\n\n1. Search / Get Recommendations\n2. Print Full Movie List\n3. Exit\n\n")
    return choice

def search():
    filters = input("\nChoose filters to apply (enter numbers seperated by commas, e.g., '1,3')\n\n1. Genre\n2. Director\n3. Actor\n4. Length (min/max)\n\nSelected Filters: ")

    def genre_search():
        genre = input("\nEnter genre (e.g., \"Science Fiction\"): ")

    def director_search():
        director = input("\nEnter director name: ")

    def actor_search():
        actor = input("\nEnter actor name: ")

    def length_search():
        min_length = input("\nEnter minumum length in minutes (or leave blank): ")
        max_length = input("Enter maximum length in minutes (or leave blank): ")

def print_movies():
    try:
        with open("individual_projects\movie_list.csv", mode= "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            movies = []
            for line in reader:
                movies.append(
                    {
                        header[0]: line[0],
                        header[1]: line[1],
                        header[2]: line[2],
                        header[3]: line[3],
                        header[4]: line[4],
                        header[5]: line[5],
                    }
                )
    except:
        print("Can't find CSV")
    else:
        for movie in movies:
            print(f"{header[0]}: {movie}")

def main():
    intro()
    while True:
        choice = main_menu()
        if choice == "1":
            break
        if choice == "2":
            print_movies()


main()