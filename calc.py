import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")

# Main window
root = tk.Tk()
root.title("Calculator")
root.config(bg="#f2f1ed")   
root.resizable(0, 0)

# Display
entry = tk.Entry(
    root,
    font=('Segoe UI', 20),
    bg="#ffffff",
    fg="#1e1e1e",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, pady=12, padx=10)

# Top buttons
tk.Button(
    root, text="C",
    font=('Segoe UI', 14),
    bg="#d9534f",  
    fg="white",
    bd=0,
    width=10,
    height=2,
    command=clear
).grid(row=1, column=0, columnspan=2, pady=6)

tk.Button(
    root, text="<-",
    font=('Segoe UI', 14),
    bg="#d9534f",
    fg="white",
    bd=0,
    width=10,
    height=2,
    command=backspace
).grid(row=1, column=2, columnspan=2, pady=6)

# Calculator buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row, col = 2, 0
for b in buttons:
    tk.Button(
        root,
        text=b,
        font=('Segoe UI', 14),
        bg="#d0d0d0" if b not in {'+','-','*','/','='} else "#4a90e2",
        fg="#1e1e1e",
        bd=0,
        width=5,
        height=2,
        activebackground="#bdbdbd",
        command=(calc if b == '=' else lambda x=b: press(x))
    ).grid(row=row, column=col, padx=6, pady=6)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
