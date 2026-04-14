from helper import *

def main_personal_portfolio():
    app = tk.Tk()
    app.title("Arsh Chowdhary - Personal Portfolio")
    app.geometry("600x1000")

    start_page = StartPage(app)
    start_page.pack(fill="both", expand=True)

    app.mainloop()

main_personal_portfolio()