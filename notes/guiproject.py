from tkinter import *
import tkinter as tk

root = Tk()
root.title("Test GUI")
root.geometry("2560x1440")
frame = tk.Frame(root, bg = '#8BDFF4')

class MainMenu:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = Label(root,text="Test GUI LABEL", fg="black", font=("Helvetica", 60), width=40, height=4)
        label.pack(padx=20, pady=8, anchor="center")

        first_button = tk.Button(root, text="First Button", width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
        second_button = tk.Button(root, text="Second Button", width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
        third_button = tk.Button(root, text="Third Button", width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
        fourth_button = tk.Button(root, text="Fourth Button", width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")

        # 25 pixels away
        first_button.pack(padx=20, pady=10, anchor="center",)
        second_button.pack(padx=20, pady=10, anchor="center")
        third_button.pack(padx=20, pady=10, anchor="center")
        fourth_button.pack(padx=20, pady=10, anchor="center")

class FirstPage: 
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu): # Add other page classes here
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        """Raises the requested frame to the top."""
        frame = self.frames[cont]
        frame.tkraise() # Brings this frame to the front

if __name__ == "__main__":
    app = FirstPage()


"""def first_button_click():
    frame.destroy()
    label = Label(root,text="Clicked the First Button", fg="black", font=("Helvetica", 60), width=40, height=4)
    label.pack(padx=20, pady=8, anchor="center")

    go_back = tk.Button(root, text="Go Back", command=main_menu, width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")

    # 25 pixels away
    go_back.pack(padx=20, pady=10, anchor="center",)"""

root.mainloop()

