
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("500x520")
root.resizable(False, False)

# Functions

def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def backspace():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])

def calculate():
    try:
        exp = display.get()
        exp = exp.replace("×", "*")
        exp = exp.replace("÷", "/")
        ans = eval(exp)

        display.delete(0, tk.END)
        display.insert(0, ans)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Menu

menu = tk.Menu(root)
root.config(menu=menu)

m1 = tk.Menu(menu, tearoff=0)
m1.add_command(label="Clear", command=clear)
m1.add_separator()
m1.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="Options", menu=m1)

# Display

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10, ipady=10)

# Button Frame

frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True, padx=10, pady=10)

buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"]
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):

        b = buttons[i][j]

        if b == "=":
            cmd = calculate
        elif b == "C":
            cmd = clear
        elif b == "⌫":
            cmd = backspace
        else:
            cmd = lambda x=b: click(x)

        tk.Button(
            frame1,
            text=b,
            font=("Arial", 16),
            command=cmd
        ).grid(
            row=i,
            column=j,
            sticky="nsew",
            padx=4,
            pady=4
        )

# Make buttons expand

for i in range(5):
    frame1.grid_rowconfigure(i, weight=1)

for j in range(4):
    frame1.grid_columnconfigure(j, weight=1)

root.mainloop()