import tkinter as tk
import math

# Function to handle button clicks
def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text in ["sin", "cos", "tan", "sqrt", "log"]:
        try:
            if button_text == "sin":
                result = str(math.sin(math.radians(float(current))))
            elif button_text == "cos":
                result = str(math.cos(math.radians(float(current))))
            elif button_text == "tan":
                result = str(math.tan(math.radians(float(current))))
            elif button_text == "sqrt":
                result = str(math.sqrt(float(current)))
            elif button_text == "log":
                result = str(math.log10(float(current)))

            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)


# Main window
root = tk.Tk()
root.title("Scientific Calculator")

# Center the window
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
root.configure(bg="#1E0CC1")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, relief="flat", justify="right", bg="#3C3C3C", fg="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sin", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("cos", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("tan", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("sqrt", 4, 4),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("log", 5, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=6, height=2, font=("Arial", 14, "bold"),
                       bg="#D72121", fg="white", relief="flat", activebackground="#D8E338",
                       command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make grid expand equally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
