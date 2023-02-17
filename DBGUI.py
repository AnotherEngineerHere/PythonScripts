import tkinter as tk
import tkcalendar
import mysql.connector
import csv
import datetime
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
import sys
import json
import os

lock_file = 'appPython.lock'

if os.path.exists(lock_file):
    sys.exit("An instance of the application is already running.")

with open(lock_file, 'w') as f:
    f.write(str(os.getpid()))


today = date.today()

db = mysql.connector.connect(
    host="localhost",
    user="PIUSER",
    password="desarrolloMTE",
    database="pidb"
)
root = tk.Tk()
root.geometry("600x800")
root.title("Descarga de información de MySQL")

title_label = tk.Label(
    root, text="Descargar Información de la base de datos:", font=("Helvetica", 16))
title_label.pack(pady=50)

start_date_label = tk.Label(
    root, text="Fecha de inicio:", font=("Helvetica", 16))
start_date_label.pack()
start_date_entry = tkcalendar.DateEntry(
    root, maxdate=today, font=("Helvetica", 16), state="readonly")
start_date_entry.pack(pady=20)


end_date_label = tk.Label(root, text="Fecha de fin:", font=("Helvetica", 16))
end_date_label.pack()
end_date_entry = tkcalendar.DateEntry( root, maxdate=today, font=("Helvetica", 16), state="readonly")
end_date_entry.pack()

tabla_label = tk.Label(root, text="Tabla:", state="normal")
tabla_label.pack(pady=20)

tablas = ['OP_Registro', 'OP_RegistroTemporal']
tabla_var = tk.StringVar(root)
tabla_var.set(tablas[0])

tabla_frame = tk.Frame(root)
tabla_frame.pack(pady=20)

tabla_entry = tk.OptionMenu(tabla_frame, tabla_var, *tablas)
tabla_entry.pack(side="left")
tabla_entry.config(font=("Helvetica", 16))

filetype_label = tk.Label(root, text="Tipo de archivo:", state="normal")
filetype_label.pack(pady=20)

filetypes = ['CSV', 'JSON']
filetype_var = tk.StringVar(root)
filetype_var.set(filetypes[0])

filetype_frame = tk.Frame(root)
filetype_frame.pack(pady=20)

filetype_entry = tk.OptionMenu(filetype_frame, filetype_var, *filetypes)
filetype_entry.pack(side="left")
filetype_entry.config(font=("Helvetica", 16))

def onRun():
    messagebox.showinfo("Information", "Selecciona fecha de inicio y de fin")


onRun()


def converStartDate(date_string):
    date_format = "%d/%m/%y"
    parsed_date = datetime.datetime.strptime(date_string, date_format)
    new_date_format = "%Y/%m/%d 00:00:00"
    new_date_string = parsed_date.strftime(new_date_format)
    return new_date_string


def converEndDate(date_string):
    date_format = "%d/%m/%y"
    parsed_date = datetime.datetime.strptime(date_string, date_format)
    new_date_format = "%Y/%m/%d 23:59:59"
    new_date_string = parsed_date.strftime(new_date_format)
    return new_date_string


def convert_string_to_date(date_string, date_format):
    return datetime.datetime.strptime(date_string, date_format)


def check_dates():
    date_format = "%d/%m/%y"
    start_date = convert_string_to_date(start_date_entry.get(), date_format)
    end_date = convert_string_to_date(end_date_entry.get(), date_format)
    print(type(start_date))
    print(type(end_date))
    if start_date > end_date:
        messagebox.showerror(
            "Error", "La fecha de inicio no puede ser mayor que la fecha de fin")
        start_date_entry.set_date(None)


def download_data():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    start_datetime = datetime.datetime.strptime(start_date, '%d/%m/%y')
    start_time = datetime.datetime.combine(start_datetime, datetime.time.min)
    end_datetime = datetime.datetime.strptime(end_date, '%d/%m/%y')
    end_time = datetime.datetime.combine(end_datetime, datetime.time.max)
    tabla = tabla_var.get()
    cursor = db.cursor()

    start_date_string = converStartDate(start_date)
    end_date_string = converEndDate(end_date)

    query = "SELECT TRAMA FROM %s WHERE FECHAHORAOCURRENCIA BETWEEN '%s' AND '%s' ORDER BY ID DESC;" % (
        tabla, start_date_string, end_date_string)
    cursor.execute(query)
    result = cursor.fetchall()
    if end_time > start_time:
        if (tabla == "OP_Registro"):
            filename = "Enviados"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", initialfile=filename)
            if file_path:
                with open(file_path, mode='w', newline="") as file:
                    writer = csv.writer(file)

                    # replace "col2", "col3", ... with actual column names
                    writer.writerow([""])
                    for row in result:
                        writer.writerow(row)

                messagebox.showinfo(
                    "Información", "Archivo descargado exitosamente")
                print("is OK")
        else:
            filename = "Recibidos"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", initialfile=filename)
            if file_path:
                with open(file_path, mode='w', newline="") as file:
                    writer = csv.writer(file)
                    # replace "col2", "col3", ... with actual column names
                    writer.writerow(
                        ["id", "fechahoraenvio", "fechahoraocurrencia", "trama"])
                    for row in result:
                        writer.writerow(row)

                messagebox.showinfo(
                    "Información", "Archivo descargado exitosamente")
                print("is OK")
    else:
        messagebox.showerror("Error", "Fechas Incorrectas")
        start_date_entry.set_date(today)
        end_date_entry.set_date(today)
        print("not OK")


def download_dataJSON():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    start_datetime = datetime.datetime.strptime(start_date, '%d/%m/%y')
    start_time = datetime.datetime.combine(start_datetime, datetime.time.min)
    end_datetime = datetime.datetime.strptime(end_date, '%d/%m/%y')
    end_time = datetime.datetime.combine(end_datetime, datetime.time.max)
    tabla = tabla_var.get()
    cursor = db.cursor()

    start_date_string = converStartDate(start_date)
    end_date_string = converEndDate(end_date)

    query = "SELECT TRAMA FROM %s WHERE FECHAHORAOCURRENCIA BETWEEN '%s' AND '%s' ORDER BY ID DESC;" % (
        tabla, start_date_string, end_date_string)
    cursor.execute(query)
    rows = cursor.fetchall()
    if end_time > start_time:
        if (tabla == "OP_Registro"):
            filename = "Enviados"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json", initialfile=filename)
            if file_path:
                query = "SELECT TRAMA FROM %s WHERE FECHAHORAOCURRENCIA BETWEEN '%s' AND '%s' ORDER BY ID DESC;" % (tabla, start_date_string, end_date_string)
            cursor.execute(query)
            rows = cursor.fetchall()

            result = []
            for row in rows:
                trama = row[0]
                trama_dict = json.loads(trama)
                result.append(trama_dict)

            with open(file_path, mode='w') as file:
                json.dump(result, file, indent=4)
        elif(table == "OP_RegistroTemporal"):
         filename = "Recibidos"
         file_path = filedialog.asksaveasfilename(defaultextension=".json", initialfile=filename)
        if file_path:
                query = "SELECT TRAMA FROM %s WHERE FECHAHORAOCURRENCIA BETWEEN '%s' AND '%s' ORDER BY ID DESC;"
                query = query % (tabla, start_date_string, end_date_string)
                cursor.execute(query)
                rows = cursor.fetchall()
                output = []
                for row in rows:
                    output.append(row[0])
                with open(file_path, "w") as file:
                    json.dump(output, file)
        messagebox.showinfo("Información", "Arhivo descargado exitosamente")
    else:
        messagebox.showerror("Error", "Fechas Incorrectas")
    start_date_entry.set_date(today)
    end_date_entry.set_date(today)


def filetype_changed(*args):
    tabla = filetype_var.get()
    # Execute the code to update the download button based on the new file type value
    if tabla == "CSV":
        download_button.config(command=download_data)
    elif tabla == "JSON":
        download_button.config(command=download_dataJSON)

# Add the listener to the filetype_var variable
filetype_var.trace("w", filetype_changed)

# Define the download button with a default command
download_button = tk.Button(root, text="Descargar", font=("Helvetica", 16), command=None, state="normal")
download_button.pack(pady=20)
root.resizable(False, False)
root.mainloop()

# Clean up the lock file when the application exits
os.remove(lock_file)
