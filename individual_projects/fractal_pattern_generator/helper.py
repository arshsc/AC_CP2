# AC 2nd Factal Pattern Generator Helper

# import needed libraries
import turtle

# intro function
def intro():
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinksi Triangle fractal using recursion.")

# function to get recursion depth from user
def get_recursion():
    # while true loop to get valid recursion depth from user
    while True:
        recursion = input("\nEnter recursion Depth (1-5): ").strip()
        # make sure it is a valid entry, if it is, convert to int and add 1 to it (since 1 is the base case) and break out of loop, otherwise print invalid entry
        if recursion in ["1", "2", "3", "4", "5"]:
            recursion = int(recursion)
            recursion += 1
            break
        else:
            print("\nInvalid Entry.")
    return recursion

# function to get color from user
def get_color():
    # list of colors to check if user input is valid
    colors = ["white", "black", "blue", "red", "green", "yellow", "orange", "purple", "pink", "brown", "grey", "lightgrey", "darkgrey", "darkblue", "lightblue", "darkgreen", "lightgreen", "darkred", "lightred", "cyan", "magenta", "maroon", "olive", "navy", "lime", "teal", "aqua", "turquoise", "beige", "lavender", "mint", "salmon", "tan"]

    # while true loop to get valid color from user
    while True:
        color = input("\nEnter triangle color (e.g., red, blue, green): ").strip().lower().replace(" ", "")
        # check if color is in list of colors, if it is, break out of loop, otherwise print invalid color
        if color in colors:
            break
        else:
            print("\nInvalid Color.")
    return color

# function to draw the Sierpinski Triangle with specified turtle, length, and recursion depth
def draw(t, length, recursion):
    # base case: if recursion is 1, return
    if recursion == 1:
        return 1
    # recursive case: if recursion is greater than 1, draw the triangle and call the function recursively on each of the three smaller triangles
    else:
        for i in range(3):
            for i in range(3):
                t.forward(length/2)
                draw(t, length/2, recursion-1)
                t.forward(length/2)
                t.left(120)
            draw(t, length/2, recursion-1)

# function to setup the turtle with specified color and return the turtle object
def setup_turtle(color):
    t = turtle.Turtle()
    t.teleport(0,0)
    t.pensize(3)
    t.color(color)
    t.hideturtle()
    return t