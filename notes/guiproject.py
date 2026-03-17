from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test GUI")
root.geometry("600x600")

label = Label(root,text="Test GUI LABEL", bg="red", fg="white", font=("Helvetica", 20))
label.pack()




root.mainloop()