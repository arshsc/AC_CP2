import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.minsize(250,250)
root.maxsize(1500,1500)
root.geometry("300x300+100+100")
root.configure(background="green")
start = tk.Label(root, text="This is my first GUI program!", font=("Times New Roman", 40, "bold")).grid(row=0, column=0, columnspan=2)
#start.config(fg="purple", background="green")

tk.Label(root, text="This is a label.").grid(row=0, column=0)

# making a counter

root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

btn= tk.Button(root, text="ADD", command=add).grid(row=5, column=0)


btn2= tk.Button(root, text="SUB", command=sub).grid(row=5, column=1)


lbl = tk.Label(root, text="0")
lbl.grid(row=5, column=0, columnspan=2)

close = tk.Button(root, text="Bye", command=root.destroy)


root.mainloop()