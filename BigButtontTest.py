import tkinter as tk
import subprocess
import os

def on_button_press():
    print("Button pressed!")

def on_exit_press():
    root.destroy()

def run_python_script():
    subprocess.Popen(["python3", "C:/Users/juana/Documentos/DBGUI.py"])

def run_bash_script():
    output = subprocess.run(["bash", "path/to/script.sh"], capture_output=True, text=True)
    output_text.configure(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output.stdout)
    output_text.configure(state='disabled')

root = tk.Tk()
root.state('normal')

button = tk.Button(root, text="Press me!", font=("Helvetica", 15), command=on_button_press)
button.pack(pady=10)

button2 = tk.Button(root, text="Button 2", font=("Helvetica", 15), command=on_button_press)
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", font=("Helvetica", 15), command=on_button_press)
button3.pack(pady=10)

button4 = tk.Button(root, text="Button 4", font=("Helvetica", 15), command=on_button_press)
button4.pack(pady=10)

python_button = tk.Button(root, text="Run Python Script", font=("Helvetica", 15), command=run_python_script)
python_button.pack(pady=10)

bash_button = tk.Button(root, text="Run Bash Script", font=("Helvetica", 15), command=run_bash_script)
bash_button.pack(pady=10)

output_text = tk.Text(root, font=("Helvetica", 15), height=10, width=50, state='disabled')
output_text.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 15), command=on_exit_press)
exit_button.pack(pady=10)

root.mainloop()
