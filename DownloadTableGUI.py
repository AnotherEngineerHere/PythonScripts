import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def download_table():
    table_name = table_entry.get()
    table = pd.read_html(table_name)[0]
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Comma Separated Values", "*.csv")])
    table.to_csv(save_path, index=False)
    status_label.config(text="Table successfully saved as " + save_path)

root = tk.Tk()
root.title("Table Downloader")

table_label = tk.Label(root, text="Table Name:")
table_label.grid(row=0, column=0, padx=10, pady=10)

table_entry = tk.Entry(root)
table_entry.grid(row=0, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download and Save", command=download_table)
download_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
