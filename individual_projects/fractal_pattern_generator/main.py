# AC 2nd Fractal Pattern Generator

# import needed libraries and functions
import turtle
from individual_projects.geometry_calculator.helper import *

# main function to run the program
def main():
    # intro
    intro() # type: ignore
    # while true loop to keep program running
    while True:
        # get recursion
        recursion = get_recursion() # type: ignore # type: ignore
        # get color
        color = get_color() # type: ignore # type: ignore
        # setup the turtle
        t = setup_turtle(color) # type: ignore
        
        # inform user it is starting to generate the triangle
        print("\nGenerating Sierpinski Triangle...")

        # make turtle go instant
        turtle.tracer(0,0)
        # draw the triangle with specified turtle, length, and recursion
        draw(t, 250, recursion) # type: ignore

        # to exit, press enter
        exit = input("\nPress 'Enter' to Exit the program. ")
        if exit == "":
            print("\nExiting...")
            turtle.bye()
            break

# call the main function
main()