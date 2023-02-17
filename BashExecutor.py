import tkinter as tk
import subprocess
import os

def execute():
    selected_file = listbox.get(listbox.curselection())
    script_path = os.path.join("/home/pi/scripts/", selected_file)
    subprocess.run(["bash", script_path])

root = tk.Tk()
root.title("Bash File Executor")

listbox = tk.Listbox(root)
listbox.pack(side="left", fill="both", expand=True)

# Insert filenames into the listbox
with open("filenames.txt", "r") as file:
    filenames = file.read().splitlines()
    for filename in filenames:
        listbox.insert("end", filename)

# Make the listbox read-only
listbox["selectmode"] = "browse"
listbox["exportselection"] = False

execute_button = tk.Button(root, text="Execute", command=execute)
execute_button.pack(side="right")

root.mainloop()
