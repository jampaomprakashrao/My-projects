import tkinter as tk
from tkinter import messagebox

def greet():
    messagebox.showinfo("Greeting", "Hello, " + entry.get())

root = tk.Tk()
root.title("Greetings App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
