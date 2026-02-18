import tkinter as tk
import math

# ===== MAIN WINDOW =====
root = tk.Tk()
root.title("Ultra Pro Calculator")
root.geometry("420x650")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# ===== ENTRY DISPLAY =====
entry = tk.Entry(root, font=("Segoe UI", 28), bg="#0f0f0f",
                 fg="white", bd=0, justify="right",
                 insertbackground="white")
entry.pack(fill="both", ipadx=8, ipady=25, padx=15, pady=20)

# ===== HISTORY DISPLAY =====
history = tk.Label(root, text="", anchor="e",
                   bg="#0f0f0f", fg="gray",
                   font=("Segoe UI", 12))
history.pack(fill="both", padx=20)

# ===== FUNCTIONS =====
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history.config(text=expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def scientific(func):
    try:
        value = float(entry.get())
        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "fact":
            result = math.factorial(int(value))

        history.config(text=f"{func}({value})")
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ===== BUTTON STYLE =====
def create_button(text, row, col, cmd, bg="#1f1f1f", fg="white"):
    btn = tk.Button(frame, text=text,
                    bg=bg, fg=fg,
                    font=("Segoe UI", 14),
                    bd=0, width=5, height=2,
                    activebackground="#333333",
                    activeforeground="white",
                    command=cmd)
    btn.grid(row=row, column=col, padx=8, pady=8)
    return btn

# ===== BUTTON FRAME =====
frame = tk.Frame(root, bg="#0f0f0f")
frame.pack()

# ===== BUTTONS =====
buttons = [
    ("C", lambda: clear(), "#ff3b30"),
    ("⌫", lambda: backspace(), "#ff9500"),
    ("(", lambda: click("("), "#2c2c2c"),
    (")", lambda: click(")"), "#2c2c2c"),
    ("/", lambda: click("/"), "#ff9500"),

    ("7", lambda: click("7")),
    ("8", lambda: click("8")),
    ("9", lambda: click("9")),
    ("*", lambda: click("*"), "#ff9500"),
    ("√", lambda: scientific("sqrt"), "#2c2c2c"),

    ("4", lambda: click("4")),
    ("5", lambda: click("5")),
    ("6", lambda: click("6")),
    ("-", lambda: click("-"), "#ff9500"),
    ("x!", lambda: scientific("fact"), "#2c2c2c"),

    ("1", lambda: click("1")),
    ("2", lambda: click("2")),
    ("3", lambda: click("3")),
    ("+", lambda: click("+"), "#ff9500"),
    ("log", lambda: scientific("log"), "#2c2c2c"),

    ("0", lambda: click("0")),
    (".", lambda: click(".")),
    ("=", lambda: calculate(), "#34c759"),
    ("sin", lambda: scientific("sin"), "#2c2c2c"),
    ("cos", lambda: scientific("cos"), "#2c2c2c"),

    ("tan", lambda: scientific("tan"), "#2c2c2c"),
    ("ln", lambda: scientific("ln"), "#2c2c2c"),
]

row = 0
col = 0

for item in buttons:
    if len(item) == 3:
        text, cmd, color = item
        create_button(text, row, col, cmd, bg=color)
    else:
        text, cmd = item
        create_button(text, row, col, cmd)

    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()
