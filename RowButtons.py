import tkinter as tk
from tkinter import messagebox

def button_click(row, column):
    messagebox.showinfo("Button clicked", f"Button {buttons[row][column]['text']} was clicked")

root = tk.Tk()
root.geometry("500x500")
root.resizable(False, False)

rows = 1
columns = 3

for i in range(rows):
    root.grid_columnconfigure(i, weight=1, minsize=150)
    root.grid_rowconfigure(i, weight=1, minsize=150)

button_names = []
for i in range(rows):
    button_names.append([f"Button {i * columns + j + 1}" for j in range(columns)])

buttons = []
for i in range(rows):
    button_row = []
    for j in range(columns):
        button = tk.Button(root, text=button_names[i][j], command=lambda r=i, c=j: button_click(r, c), width=10, height=2, font=("Arial", 12), justify='center')
        button.grid(row=i, column=j, padx=20, pady=20, sticky='nsew')
        button_row.append(button)
    buttons.append(button_row)

if rows * columns < 9:
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

root.mainloop()
