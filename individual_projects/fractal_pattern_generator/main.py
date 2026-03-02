# AC 2nd Fractal Pattern Generator

# fix pychace happening
# fix 1 recursion able to happen
# make readme
# add comments

import turtle
import sys
from helper import *
sys.dont_write_bytecode = True

def main():
    intro()
    while True:
        recursion = get_recursion()
        color = get_color()
        t = setup_turtle(color)

        print("\nGenerating Sierpinski Triangle...")

        turtle.tracer(0,0)
        draw(t, 250, recursion)

        exit = input("\nPress 'Enter' to Exit the program. ")
        if exit == "":
            print("\nExiting...")
            turtle.bye()
            break

main()