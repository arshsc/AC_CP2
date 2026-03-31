# import helper functions
from helper import *

# define main function
def main():
    # setup gradebook
    gradebook = GradeBook()
    gradebook.load_from_csv()

    # call intro
    intro()

    # menu
    while True:
        print("\nMAIN MENU")
        print("[1] Add New Student")
        print("[2] Add Grade to Student")
        print("[3] View Student Record")
        print("[4] View All Students")
        print("[5] Class Summary")
        print("[6] Exit")
        choice = input("Enter your choice (1-6): ")

        # user chouce
        if choice == "1":
            add_new_student(gradebook)
        elif choice == "2":
            add_grade_to_student(gradebook)
        elif choice == "3":
            view_student_record(gradebook)
        elif choice == "4":
            view_all_students(gradebook)
        elif choice == "5":
            class_summary(gradebook)
        elif choice == "6":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Try again.")

# call main function
main()