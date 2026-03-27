from tkinter import *
import tkinter as tk

root = Tk()
root.title("Test GUI")
root.geometry("600x600")

def button_blicked():
    print("Button clicked!")

def main_menu():
    label = Label(root,text="Test GUI LABEL", bg="red", fg="white", font=("Helvetica", 40), width=50, height=3)
    label.pack(padx=20, pady=5, anchor="center")

    first_button = tk.Button(root, text="First Button", command=button_blicked, width=25, height=2, font=("Arial", 12), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    second_button = tk.Button(root, text="Second Button", command=button_blicked, width=25, height=2, font=("Arial", 12), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    third_button = tk.Button(root, text="Third Button", command=button_blicked, width=25, height=2, font=("Arial", 12), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    fourth_button = tk.Button(root, text="Fourth Button", command=button_blicked, width=25, height=2, font=("Arial", 12), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")

    # 25 pixels away
    first_button.pack(padx=20, pady=5, anchor="center",)
    second_button.pack(padx=20, pady=5, anchor="center")
    third_button.pack(padx=20, pady=5, anchor="center")
    fourth_button.pack(padx=20, pady=5, anchor="center")


main_menu()

root.mainloop()