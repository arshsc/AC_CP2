# import helper functions
from helper import *

# main
def main_personal_portfolio():
    # setup the app
    app = tk.Tk()
    # setup the app title
    app.title("Arsh Chowdhary - Personal Portfolio")
    # setup resolution
    app.geometry("600x1000")

    # call class 
    start_page = StartPage(app)
    # pack the frame
    start_page.pack(fill="both", expand=True)

    # setup app mainloop
    app.mainloop()

# call the main function
main_personal_portfolio()