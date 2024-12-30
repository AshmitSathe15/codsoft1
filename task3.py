import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return
        
        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if digits_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#e0f7fa")

header = tk.Label(root, text="Password Generator", bg="#006064", fg="white", font=("Helvetica", 20, "bold"))
header.pack(fill=tk.X, pady=15)

length_frame = tk.Frame(root, bg="#e0f7fa")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Enter Password Length:", bg="#e0f7fa", font=("Helvetica", 12))
length_label.pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, font=("Helvetica", 12), width=10, justify="center")
length_entry.pack(side=tk.LEFT, padx=10)

options_frame = tk.Frame(root, bg="#e0f7fa")
options_frame.pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(options_frame, text="Include Uppercase (A-Z)", variable=uppercase_var, bg="#e0f7fa", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(options_frame, text="Include Lowercase (a-z)", variable=lowercase_var, bg="#e0f7fa", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Checkbutton(options_frame, text="Include Digits (0-9)", variable=digits_var, bg="#e0f7fa", font=("Helvetica", 10)).grid(row=0, column=1, sticky="w", padx=10, pady=5)
tk.Checkbutton(options_frame, text="Include Special (!@#$)", variable=special_var, bg="#e0f7fa", font=("Helvetica", 10)).grid(row=1, column=1, sticky="w", padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#00796b", fg="white", font=("Helvetica", 12), width=20)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="Generated Password: ", bg="#e0f7fa", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

footer = tk.Label(root, text="Secure & Random Passwords", bg="#006064", fg="white", font=("Helvetica", 10))
footer.pack(fill=tk.X, pady=10)

root.mainloop()
