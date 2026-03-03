# AC 2nd Fractal Pattern Generator

# import needed libraries and functions
import turtle
from helper import *

# main function to run the program
def main():
    # intro
    intro()
    # while true loop to keep program running
    while True:
        # get recursion
        recursion = get_recursion()
        # get color
        color = get_color()
        # setup the turtle
        t = setup_turtle(color)
        
        # inform user it is starting to generate the triangle
        print("\nGenerating Sierpinski Triangle...")

        # make turtle go instant
        turtle.tracer(0,0)
        # draw the triangle with specified turtle, length, and recursion
        draw(t, 250, recursion)

        # to exit, press enter
        exit = input("\nPress 'Enter' to Exit the program. ")
        if exit == "":
            print("\nExiting...")
            turtle.bye()
            break

# call the main function
main()