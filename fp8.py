import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

def create_database():
    conn = sqlite3.connect("userinfo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            contact_method TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def submit_data():
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_method_var.get()

    if not all([name, birthday, email, phone, address, contact_method]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email format.")
        return

    conn = sqlite3.connect("userinfo.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_method_var.set(contact_options[0])

    messagebox.showinfo("Success", "Customer information submitted!")

create_database()
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("400x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD)").pack()
birthday_entry = tk.Entry(root, width=50)
birthday_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

tk.Label(root, text="Preferred Contact Method").pack()
contact_options = ["Email", "Phone", "Mail"]
contact_method_var = tk.StringVar()
contact_method_var.set(contact_options[0])
contact_dropdown = ttk.Combobox(root, textvariable=contact_method_var, values=contact_options, state="readonly")
contact_dropdown.pack()

submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.pack(pady=10)

root.mainloop()
