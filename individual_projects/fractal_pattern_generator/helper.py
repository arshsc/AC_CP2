import turtle

def intro():
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinksi Triangle fractal using recursion.")


def get_recursion():
    while True:
        recursion = input("\nEnter recursion Depth (1-5): ").strip()
        if recursion in ["1", "2", "3", "4", "5"]:
            recursion = int(recursion)
            recursion += 1
            break
        else:
            print("\nInvalid Entry.")
    return recursion

def get_color():
    colors = ["white", "black", "blue", "red", "green", "yellow", "orange", "purple", "pink", "brown", "grey", "lightgrey", "darkgrey", "darkblue", "lightblue", "darkgreen", "lightgreen", "darkred", "lightred", "cyan", "magenta", "maroon", "olive", "navy", "lime", "teal", "aqua", "turquoise", "beige", "lavender", "mint", "salmon", "tan"]

    while True:
        color = input("\nEnter triangle color (e.g., red, blue, green): ").strip().lower().replace(" ", "")
        if color in colors:
            break
        else:
            print("\nInvalid Color.")
    return color

def draw(t, length, recursion):
    if recursion == 1:
        return 1
    else:
        for i in range(3):
            for i in range(3):
                t.forward(length/2)
                draw(t, length/2, recursion-1)
                t.forward(length/2)
                t.left(120)
            draw(t, length/2, recursion-1)

def setup_turtle(color):
    t = turtle.Turtle()
    t.teleport(0,0)
    t.pensize(3)
    t.color(color)
    t.hideturtle()
    return t