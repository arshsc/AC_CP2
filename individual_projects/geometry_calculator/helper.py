# import needed libraries
import csv

# list of all valid shapes for easy reference
valid_shapes = ["Circle", "Rectangle", "Square", "Triangle"]

# file paths
circle_file = "individual_projects/geometry_calculator/docs/circles.csv"
rectangle_file = "individual_projects/geometry_calculator/docs/rectangles.csv"
square_file = "individual_projects/geometry_calculator/docs/squares.csv"
triangle_file = "individual_projects/geometry_calculator/docs/triangles.csv"

# classes
# circle class
class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def get_area(self):
        return 3.141592653 * self.radius ** 2

    def get_circumference(self):
        return 2 * 3.141592653 * self.radius

    def display(self):
        return f"Circle | Radius: {self.radius} | Area: {self.get_area():.2f} | Circumference: {self.get_circumference():.2f}"

    @staticmethod
    def formulas():
        return "Area = π * radius^2 | Circumference = 2 * π * radius"

    def to_dict(self):
        return {"radius": self.radius, "area": self.get_area(), "circumference": self.get_circumference()}

# rectagnle class
class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        return f"Rectangle | Length: {self.length} | Width: {self.width} | Area: {self.get_area():.2f} | Perimeter: {self.get_perimeter():.2f}"

    @staticmethod
    def formulas():
        return "Area = length * width | Perimeter = 2 * (length + width)"

    def to_dict(self):
        return {"length": self.length, "width": self.width, "area": self.get_area(), "perimeter": self.get_perimeter()}

# square class
class Square:
    def __init__(self, side):
        self.side = float(side)

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

    def display(self):
        return f"Square | Side: {self.side} | Area: {self.get_area():.2f} | Perimeter: {self.get_perimeter():.2f}"

    @staticmethod
    def formulas():
        return "Area = side^2 | Perimeter = 4 * side"

    def to_dict(self):
        return {"side": self.side, "area": self.get_area(), "perimeter": self.get_perimeter()}

# triangle class
class Triangle:
    def __init__(self, side1, side2, side3, height=None):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
        self.height = float(height) if height else None

    def get_area(self):
        if self.height:
            return (self.side1 * self.height) / 2
        else:
            return None

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def display(self):
        return f"Triangle | Sides: ({self.side1}, {self.side2}, {self.side3}) | Height: {self.height} | Area: {self.get_area():.2f} | Perimeter: {self.get_perimeter():.2f}"

    @staticmethod
    def formulas():
        return "Area = 1/2(base * height) | Perimeter = side1 + side2 + side3"

    def to_dict(self):
        return {"side1": self.side1, "side2": self.side2, "side3": self.side3, "height": self.height, "area": self.get_area(), "perimeter": self.get_perimeter()}


# load each of the csv files
def load_csv(filename):
    try:
        with open(filename, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

# load the csv files before anything
circles = load_csv(circle_file)
rectangles = load_csv(rectangle_file)
squares = load_csv(square_file)
triangles = load_csv(triangle_file)


# save csv function to write back to the file after edits
def save_csv(filename, fieldnames, data):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# function to count total shapes and each shape type for menu display
def count_shapes():
    counts = {
        "Circle": len(circles),
        "Rectangle": len(rectangles),
        "Square": len(squares),
        "Triangle": len(triangles)
    }
    total = sum(counts.values())
    return total, counts


# intro
def intro():
    print("\n=====================================\n\nGEOMETRY CALCULATOR\n\n=====================================\n\nWelcome to the Shape Calculator\n\n=====================================")

# main menu
def menu():
    total_shapes, counts = count_shapes()
    print("\nMAIN MENU\n\n=====================================")
    print(f"\nCurrent Shapes: {total_shapes} created")
    print(f"\nShape Library: \nCircles: {counts['Circle']}\nRectangles: {counts['Rectangle']}\nSquares: {counts['Square']}\nTriangles: {counts['Triangle']}")
    print("\nACTIONS:\n[1] Create New Shape\n[2] View All Shapes\n[3] Select Shape\n[4] Compare Shapes\n[5] Sort Shapes\n[6] Formula Guide\n[7] Quit")
    choice = input("\nEnter your choice (1-7): ")
    return choice


# create new shape
def create_new_shape():
    print("\nCREATE NEW SHAPE\n")
    print("Available Shapes:\n[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
    choice = input("Enter shape type (1-4): ").strip()

    # create circle, then append to csv and list
    if choice == "1":
        while True:
            try:
                radius = float(input("Enter radius: "))
                if radius <= 0:
                    print("Must be positive!")
                    continue
                break
            except:
                print("Invalid Input")
        circle = Circle(radius)
        with open(circle_file, "a", newline="") as file:
            fieldnames = ["radius", "area", "circumference"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(circle.to_dict())
        circles.append(circle.to_dict())
        print(circle.display())

    # create rectangle, then append to csv and list
    elif choice == "2":
        while True:
            try:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                if length <= 0 or width <= 0:
                    print("Must be positive!")
                    continue
                break
            except:
                print("Invalid Input")
        rect = Rectangle(length, width)
        with open(rectangle_file, "a", newline="") as file:
            fieldnames = ["length", "width", "area", "perimeter"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(rect.to_dict())
        rectangles.append(rect.to_dict())
        print(rect.display())

    # create square, then append to csv and list
    elif choice == "3":
        while True:
            try:
                side = float(input("Enter side length: "))
                if side <= 0:
                    print("Must be positive!")
                    continue
                break
            except:
                print("Invalid Input")
        sq = Square(side)
        with open(square_file, "a", newline="") as file:
            fieldnames = ["side", "area", "perimeter"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(sq.to_dict())
        squares.append(sq.to_dict())
        print(sq.display())

    # create triangle, then append to csv and list
    elif choice == "4":
        while True:
            try:
                s1 = float(input("Enter side 1: "))
                s2 = float(input("Enter side 2: "))
                s3 = float(input("Enter side 3: "))
                height = float(input("Enter height: "))
                if s1 <= 0 or s2 <= 0 or s3 <= 0 or height <= 0:
                    print("All values must be positive!")
                    continue
                break
            except:
                print("Invalid Input")
        tri = Triangle(s1, s2, s3, height)
        with open(triangle_file, "a", newline="") as file:
            fieldnames = ["side1", "side2", "side3", "height", "area", "perimeter"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(tri.to_dict())
        triangles.append(tri.to_dict())
        print(tri.display())

    else:
        print("Invalid Input")


# view all shapes
def view_all_shapes():
    print("\nALL SHAPES\n")
    shape_number = 1

    for row in circles:
        object = Circle(row["radius"])
        print(f"{shape_number}. {object.display()}")
        shape_number += 1

    for row in rectangles:
        object = Rectangle(row["length"], row["width"])
        print(f"{shape_number}. {object.display()}")
        shape_number += 1

    for row in squares:
        object = Square(row["side"])
        print(f"{shape_number}. {object.display()}")
        shape_number += 1

    for row in triangles:
        object = Triangle(row["side1"], row["side2"], row["side3"], row["height"])
        print(f"{shape_number}. {object.display()}")
        shape_number += 1

    if shape_number == 1:
        print("No shapes found.")


# select shape
def select_shape():
    print("\nSELECT SHAPE\n")
    print("[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
    choice = input("Choose shape type: ").strip()

    # determine which shape list and file to use based on choice, also get the keys needed  and csv writing
    if choice == "1":
        shapes = circles
        filename = circle_file
        fieldnames = ["radius", "area", "circumference"]
        keys = ["radius"]  # only the constructor needs radius
    elif choice == "2":
        shapes = rectangles
        filename = rectangle_file
        fieldnames = ["length", "width", "area", "perimeter"]
        keys = ["length", "width"]
    elif choice == "3":
        shapes = squares
        filename = square_file
        fieldnames = ["side", "area", "perimeter"]
        keys = ["side"]
    elif choice == "4":
        shapes = triangles
        filename = triangle_file
        fieldnames = ["side1", "side2", "side3", "height", "area", "perimeter"]
        keys = ["side1", "side2", "side3", "height"]
    else:
        print("Invalid Input")
        return

    if not shapes:
        print("No shapes to select.")
        return

    # display all shapes with their index
    print("\nAvailable Shapes:")
    for i, s in enumerate(shapes, start=1):
        print(f"{i}. {s}")

    # select a shape
    try:
        index = int(input("Select shape number: ")) - 1
        if index < 0 or index >= len(shapes):
            print("Invalid selection!")
            return
    except:
        print("Invalid Input")
        return

    selected = shapes[index]

    # edit only the measurement values
    print("\nEnter new values (leave blank to keep current value):")
    for key in keys:
        new_val = input(f"{key} ({selected[key]}): ").strip()
        if new_val != "":
            selected[key] = float(new_val)

    # recreate the shape with updated values then update the dict and write back to csv
    if choice == "1":
        object = Circle(selected["radius"])
    elif choice == "2":
        object = Rectangle(selected["length"], selected["width"])
    elif choice == "3":
        object = Square(selected["side"])
    elif choice == "4":
        object = Triangle(
            selected["side1"], selected["side2"], selected["side3"], selected["height"]
        )

    # update the dict with new values
    shapes[index] = object.to_dict()

    # write back to CSV
    save_csv(filename, fieldnames, shapes)

    print("\nShape updated successfully!")

# compare shapes
def compare_shapes():
    print("\nCOMPARE SHAPES\n")
    print("[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
    choice = input("Choose shape type: ").strip()

    # map choice to shapes and comparison field
    shape_map = {
        "1": (circles, "circumference", "Circle"),
        "2": (rectangles, "perimeter", "Rectangle"),
        "3": (squares, "perimeter", "Square"),
        "4": (triangles, "perimeter", "Triangle")
    }

    if choice not in shape_map:
        print("Invalid Input")
        return

    shapes, compare_field, shape_name = shape_map[choice]

    if len(shapes) < 2:
        print(f"Need at least 2 {shape_name.lower()}s to compare.")
        return

    # show available shapes with numbers
    print(f"\nAvailable {shape_name}s:")
    for i, s in enumerate(shapes, start=1):
        print(f"{i}. {s}")

    # ask user to select two shapes
    try:
        i1 = int(input("Select first shape #: ")) - 1
        i2 = int(input("Select second shape #: ")) - 1
        if i1 < 0 or i2 < 0 or i1 >= len(shapes) or i2 >= len(shapes):
            print("Invalid selection!")
            return
    except:
        print("Invalid input!")
        return

    s1 = shapes[i1]
    s2 = shapes[i2]

    # convert the values we need to floats
    area1, area2 = float(s1["area"]), float(s2["area"])
    val1, val2 = float(s1[compare_field]), float(s2[compare_field])

    # Compare area
    print("\n--- AREA COMPARISON ---")
    if area1 > area2:
        print("Shape 1 has a larger area.")
    elif area2 > area1:
        print("Shape 2 has a larger area.")
    else:
        print("Both shapes have equal area.")

    # Compare perimeter / circumference
    print(f"\n--- {compare_field.upper()} COMPARISON ---")
    if val1 > val2:
        print("Shape 1 has a larger value.")
    elif val2 > val1:
        print("Shape 2 has a larger value.")
    else:
        print("Both shapes are equal.")

    print("\nComparison complete!")


# sort shapes
def sort_shapes():
    print("\nSORT SHAPES\n")
    print("[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
    choice = input("Choose shape type: ").strip()

    # sort circles
    if choice == "1":
        shapes = circles
        filename = circle_file
        fieldnames = ["radius", "area", "circumference"]
        sort_options = {"1": "area", "2": "circumference"}
    # sort rectangles
    elif choice == "2":
        shapes = rectangles
        filename = rectangle_file
        fieldnames = ["length", "width", "area", "perimeter"]
        sort_options = {"1": "area", "2": "perimeter"}
    # sort squares
    elif choice == "3":
        shapes = squares
        filename = square_file
        fieldnames = ["side", "area", "perimeter"]
        sort_options = {"1": "area", "2": "perimeter"}
    # sort triangles
    elif choice == "4":
        shapes = triangles
        filename = triangle_file
        fieldnames = ["side1", "side2", "side3", "height", "area", "perimeter"]
        sort_options = {"1": "area", "2": "perimeter"}
    else:
        print("Invalid Input")
        return

    if not shapes:
        print("No shapes to sort.")
        return

    print("\nSort by:\n[1] Area\n[2] Perimeter/Circumference")
    sort_choice = input("Enter choice: ").strip()
    if sort_choice not in sort_options:
        print("Invalid Input")
        return

    sort_key = sort_options[sort_choice]
    shapes.sort(key=lambda x: float(x[sort_key]))
    save_csv(filename, fieldnames, shapes)
    print(f"\nShapes sorted by {sort_key} successfully!")


# formulas
def formula_guide(valid_shapes):
    while True:
        print("\nWhich shape do you want to see formulas for:\n[1] Circle\n[2] Rectangle\n[3] Square\n[4] Triangle")
        shape_type = input("\nEnter your choice (1-4): ").strip()
        if shape_type not in ["1", "2", "3", "4"]:
            print("\nInvalid Shape")
        else:
            if shape_type == "1":
                print(Circle.formulas())
            elif shape_type == "2":
                print(Rectangle.formulas())
            elif shape_type == "3":
                print(Square.formulas())
            elif shape_type == "4":
                print(Triangle.formulas())
        another_shape = input("\nLook at another formula? (Y/N): ").strip().lower()
        if another_shape not in ["yes", "y"]:
            break