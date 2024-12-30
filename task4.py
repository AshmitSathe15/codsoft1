import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.name} ({self.phone})"

class ContactBookApp:
    def __init__(self, root):
        self.contacts = []

        root.title("Contact Book")
        root.geometry("600x700")  # Increased dimensions for better space utilization
        root.configure(bg="#f0f8ff")  # Changed to AliceBlue

        header = tk.Label(root, text="Contact Book", font=("Helvetica", 20, "bold"), bg="#4682b4", fg="white")  # SteelBlue
        header.pack(fill=tk.X, pady=15)

        self.listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, height=20, selectbackground="#b0c4de")  # LightSteelBlue
        self.listbox.pack(pady=10)

        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg="#87cefa", fg="white", font=("Helvetica", 10), width=20).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="View Details", command=self.view_details, bg="#32cd32", fg="white", font=("Helvetica", 10), width=20).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Search Contact", command=self.search_contact, bg="#ffeb3b", fg="black", font=("Helvetica", 10), width=20).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Update Contact", command=self.update_contact, bg="#00ced1", fg="white", font=("Helvetica", 10), width=20).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, bg="#ff6347", fg="white", font=("Helvetica", 10), width=20).grid(row=2, columnspan=2, pady=5)

        footer = tk.Label(root, text="Manage Your Contacts Easily", font=("Helvetica", 10), bg="#4682b4", fg="white")
        footer.pack(fill=tk.X, pady=10)

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        self.contacts.append(Contact(name, phone, email, address))
        self.update_listbox()

    def view_details(self):
        try:
            index = self.listbox.curselection()[0]
            contact = self.contacts[index]
            details = f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}"
            messagebox.showinfo("Contact Details", details)
        except IndexError:
            messagebox.showerror("Error", "No contact selected.")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        if not query:
            return
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            result_str = "\n".join([f"{contact.name} - {contact.phone}" for contact in results])
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        try:
            index = self.listbox.curselection()[0]
            contact = self.contacts[index]
            contact.name = simpledialog.askstring("Update", "Enter New Name:", initialvalue=contact.name) or contact.name
            contact.phone = simpledialog.askstring("Update", "Enter New Phone Number:", initialvalue=contact.phone) or contact.phone
            contact.email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=contact.email) or contact.email
            contact.address = simpledialog.askstring("Update", "Enter New Address:", initialvalue=contact.address) or contact.address
            self.update_listbox()
        except IndexError:
            messagebox.showerror("Error", "No contact selected.")

    def delete_contact(self):
        try:
            index = self.listbox.curselection()[0]
            contact = self.contacts[index]
            confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete {contact.name}?")
            if confirm:
                del self.contacts[index]
                self.update_listbox()
        except IndexError:
            messagebox.showerror("Error", "No contact selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
