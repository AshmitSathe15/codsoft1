import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.configure(bg="#e6f2ff")

header = tk.Label(root, text="Simple Calculator", bg="#004d99", fg="white", font=("Helvetica", 16, "bold"))
header.pack(fill=tk.X, pady=10)

tk.Label(root, text="Enter First Number:", bg="#e6f2ff", font=("Helvetica", 10)).pack(pady=5)
entry1 = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="#004d99")
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:", bg="#e6f2ff", font=("Helvetica", 10)).pack(pady=5)
entry2 = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="#004d99")
entry2.pack(pady=5)

tk.Label(root, text="Choose Operation:", bg="#e6f2ff", font=("Helvetica", 10)).pack(pady=5)
operation_var = tk.StringVar(value="+")
operations_frame = tk.Frame(root, bg="#e6f2ff")
operations_frame.pack(pady=5)

tk.Radiobutton(operations_frame, text="Addition (+)", variable=operation_var, value="+", bg="#e6f2ff", font=("Helvetica", 9)).grid(row=0, column=0, padx=10)
tk.Radiobutton(operations_frame, text="Subtraction (-)", variable=operation_var, value="-", bg="#e6f2ff", font=("Helvetica", 9)).grid(row=0, column=1, padx=10)
tk.Radiobutton(operations_frame, text="Multiplication (*)", variable=operation_var, value="*", bg="#e6f2ff", font=("Helvetica", 9)).grid(row=1, column=0, padx=10)
tk.Radiobutton(operations_frame, text="Division (/)", variable=operation_var, value="/", bg="#e6f2ff", font=("Helvetica", 9)).grid(row=1, column=1, padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#004d99", fg="white", font=("Helvetica", 12), width=20)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", bg="#e6f2ff", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
