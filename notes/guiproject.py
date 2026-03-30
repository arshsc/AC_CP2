from tkinter import *
import tkinter as tk

root = Tk()
root.title("Test GUI")
root.geometry("2560x1440")

def button_blicked():
    print("Button clicked!")

def main_menu():
    label = Label(root,text="Test GUI LABEL", fg="black", font=("Helvetica", 60), width=40, height=4)
    label.pack(padx=20, pady=8, anchor="center")

    first_button = tk.Button(root, text="First Button", command=button_blicked, width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    second_button = tk.Button(root, text="Second Button", command=button_blicked, width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    third_button = tk.Button(root, text="Third Button", command=button_blicked, width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")
    fourth_button = tk.Button(root, text="Fourth Button", command=button_blicked, width=50, height=4, font=("Helvetica", 15), bd=5, bg="white", activebackground="grey", activeforeground="white", overrelief="solid")

    # 25 pixels away
    first_button.pack(padx=20, pady=10, anchor="center",)
    second_button.pack(padx=20, pady=10, anchor="center")
    third_button.pack(padx=20, pady=10, anchor="center")
    fourth_button.pack(padx=20, pady=10, anchor="center")

main_menu()

root.mainloop()