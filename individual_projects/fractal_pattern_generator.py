# AC 2nd Fractal Pattern Generator

import turtle

def intro():
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinksi Triangle fractal using recursion.")


def get_recursion():
    while True:
        recursion = input("\nEnter recursion Depth (1-5): ").strip()
        if recursion in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("\nInvalid Entry.")
    return recursion

def get_color():
    while True:
        color = input("\nEnter triangle color (e.g., red, blue, green): ").strip().lower()
        if color in ["red", "orange", "yellow", "green", "blue", "pink", "purple", "indigo", "violet", "brown", "gray", "black"]:
            break
        else:
            print("\nInvalid Entry")
    return color

def draw(t, length, depth):
    if depth == 0:
        for i in range(0,3):
            t.forward(length)
            t.left(120)
    else:
        draw(t, length/2, depth-1)
        t.forward(length/2)
        draw(t, length/2, depth-1)
        t.back(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        draw(t, length/2, depth-1)
        t.left(60)
        t.back(length/2)
        t.right(60)

def setup_turtle(color):
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(15)
    t.color(color)

def main():
    intro()
    while True:
        recursion = get_recursion()
        recursion = int(recursion)
        recursion -= 1

        color = get_color()

        t = turtle.Turtle()
        t.pensize(3)
        t.color(color)
        t.hideturtle()

        print("\nGenerating Sierpinski Triangle...")
        draw(t, 250, recursion)
        exit = input("\nPress 'Enter' to Exit the program. ")
        if exit == "":
            print("\nExiting...")
            turtle.bye()
            break
        else:
            turtle.exitonclick()

main()
turtle.done()