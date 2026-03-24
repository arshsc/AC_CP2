import csv


valid_shapes = ["Circle", "Rectangle", "Square", "Triangle"]


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(radius):
        pi = 3.141592653
        area_circle = pi * (radius * radius)
        return area_circle

    def get_circumference(radius):
        pi = 3.141592653
        circumference = 2*(pi * radius)
        return circumference
    
    def to_dict(self):
        return self.__dict__

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area_rectangle(length, width):
        area_rectangle = length * width
        return area_rectangle
    
    def get_perimeter_rectangle(length, width):
        perimeter_rectangle = length + length + width + width
        return perimeter_rectangle

    # sub square class here

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area_triangle(base, height):
        area_triangle = (base * height)/2
        return area_triangle
    
    def get_perimeter_triangle(base, height):
        pass



def intro():
    print("\nGEOMETRY CALCULATOR\n\nWelcome to the Shape Calculator")

def menu():
    print("\nMAIN MENU\n")
    print(f"Current Shapes: shapes_created created\n")
    print(f"SHAPE LIBRARY:\nshapes_created")
    print("\nACTIONS:\n[1] Create New Shape\n[2] View All Shapes\n[3] Select Shape\n[4] Compare Shops\n[5] Sort Shapes\n[6] Formula Guide\n[7] Quit")
    choice = input("\nEnter your choice (1-7): ")
    return choice

def create_new_shape(valid_shapes):
    print("\nCREATE NEW SHAPE\n")
    while True:

        print("Available Shapes:\n[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
        shape_type = input("\nEnter shape type (1-4): ").strip().upper()

        if shape_type not in valid_shapes:
            print("\nInvalid Shape")
        else:
            print(f"\nCreating a {shape_type}...")

            if shape_type == "Circle":
                while True:
                    radius = input("Enter radius (positive number): ")
                    if radius.isdigit() == False:
                        print("\nInvalid Entry")

                    elif radius.isdigit() == True:
                        with open("individual_projects\geometry_calculator\docs\circles.csv", "a", newline='') as file:
                            writer = csv.DictWriter()
                        print("\nCircle created successfully!")
                        print(f"\nCIRCLE DETAILS:\nShape: {shape_type} #\nRadius: {radius} units\nArea:")

def formula_guide(valid_shapes):
    while True:
        print("\nWhich shape do you want to see formulas for:\n[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
        shape_type = input("\nEnter your choice (1-4): ").strip().upper()

        if shape_type not in ["1", "2", "3", "4"]:
            print("\nInvalid Shape")
        elif shape_type == "Exit":
            break
        else:
            if shape_type == "1":
                print("\nFormulas for a Circle:")
                print("\nArea = pi * radius^2")
                print("Circumference = 2(pi * radius) OR pi * diameter")
                print("Diameter = radius + radius")

            elif shape_type in ["2", "3"]:
                print(f"\nFormulas for a Rectangle / Square:")
                print("\nArea = length * width")
                print("Perimeter = length + lenghth + width + width")

            elif shape_type == "4":
                print(f"\nFormulas for a Triangle:")
                print("\nArea = 1/2(base * height)")
                print("Perimeter = side a + side b + side c")

            another_shape = input("\nWould you like to look at another shapes formula (Y/N): ").strip().lower()

            if another_shape not in ["yes", "no", "y", "n"]:
                print("\nInvalid Entry")
            else:
                if another_shape == ["yes", "y"]:
                    continue
                elif another_shape == ["no", "n"]:
                    break
intro()
while True:
    choice = menu()
    
    if choice == "1":
        create_new_shape(valid_shapes)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        formula_guide(valid_shapes)
    elif choice == "7":
        print("\nExiting...")
        break
    else:
        print("\nInvalid Choice")