from helper import *


intro()
while True:
    choice = menu()
    if choice == "1":
        create_new_shape()
    elif choice == "2":
        view_all_shapes()
    elif choice == "3":
        select_shape()
    elif choice == "4":
        compare_shapes()
    elif choice == "5":
        sort_shapes()
    elif choice == "6":
        formula_guide(valid_shapes)
    elif choice == "7":
        print("\nExiting...")
        break
    else:
        print("\nInvalid Choice")