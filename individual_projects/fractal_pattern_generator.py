# AC 2nd Fractal Pattern Generator

import turtle

def intro():
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinksi Triangle fractal using recursion.")

def options():
    while True:
        recursion = input("\nEnter recursion Depth (1-5): ").strip()
        if recursion in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("\nInvalid Entry.")
    while True:
        color = input("\nEnter triangle color (e.g., red, blue, green): ").strip().lower()
        if color in ["red", "orange", "yellow", "green", "blue", "pink", "purple", "indigo", "violet", "brown", "gray", "black"]:
            break
        else:
            print("\nInvalid Entry")
    return recursion, color

def main():
    intro()
    recursion, color = options()
    t.color(color)


def sierpinski_triangle(t, line_len):
    if line_len == 1:
        return 1
    else:
        t.forward(line_len)
        t.left(120)
        t.forward(line_len)
        t.left(120)
        t.forward(line_len)
        line_len -= 1
        sierpinski_triangle(t, line_len)


t = turtle.Turtle()
sierpinski_triangle(t, 3)
turtle.done()

