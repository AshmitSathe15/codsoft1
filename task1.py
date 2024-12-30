import tkinter as tk
from tkinter import messagebox
import json


class Task:
    def __init__(self, name, description="", completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"{self.name} - {'Completed' if self.completed else 'Pending'}"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")
        self.tasks = []

        self.load_tasks()

        self.title_label = tk.Label(
            root, text="To-Do List", font=("Helvetica", 16), bg="#f0f0f0"
        )
        self.title_label.pack(pady=10)

        self.listbox = tk.Listbox(
            root,
            width=50,
            height=10,
            bg="#fff",
            font=("Helvetica", 12),
            selectbackground="#a6a6a6",
        )
        self.listbox.pack(padx=20, pady=10)

        self.entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame,
            text="Add Task",
            command=self.add_task,
            width=12,
            bg="#6c757d",
            fg="#fff",
            font=("Helvetica", 10),
        )
        self.add_button.grid(row=0, column=0, padx=5)

        self.mark_button = tk.Button(
            self.button_frame,
            text="Mark Completed",
            command=self.mark_completed,
            width=12,
            bg="#28a745",
            fg="#fff",
            font=("Helvetica", 10),
        )
        self.mark_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            command=self.delete_task,
            width=12,
            bg="#dc3545",
            fg="#fff",
            font=("Helvetica", 10),
        )
        self.delete_button.grid(row=0, column=2, padx=5)

        self.save_button = tk.Button(
            root,
            text="Save Tasks",
            command=self.save_tasks,
            width=30,
            bg="#007bff",
            fg="#fff",
            font=("Helvetica", 10),
        )
        self.save_button.pack(pady=10)

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            self.listbox.insert(tk.END, f"{task.name} - {status}")

    def add_task(self):
        task_name = self.entry.get()
        if task_name:
            task = Task(task_name)
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task name.")

    def mark_completed(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            task.mark_completed()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning(
                "Selection Error", "Please select a task to mark as completed."
            )

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning(
                "Selection Error", "Please select a task to delete."
            )

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)
        messagebox.showinfo("Save", "Tasks have been saved!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in tasks_data]
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
