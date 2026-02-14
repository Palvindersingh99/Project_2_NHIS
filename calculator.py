import tkinter as tk

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=('Arial', 18),
    width=20,
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
input_field.pack()

# Buttons frame
btns_frame = tk.Frame(root)
btns_frame.pack()

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            btns_frame, text=text, width=6, height=2,
            command=equal, bg="lightgreen"
        )
    elif text == 'C':
        btn = tk.Button(
            btns_frame, text=text, width=6, height=2,
            command=clear, bg="lightcoral"
        )
    else:
        btn = tk.Button(
            btns_frame, text=text, width=6, height=2,
            command=lambda t=text: press(t)
        )

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
