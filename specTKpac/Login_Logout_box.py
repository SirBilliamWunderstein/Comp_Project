import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

conn = sqlite3.connect("accounts.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)")
conn.commit()

def create_account_window(parent_canvas):
    frame = tk.Frame(parent_canvas, bd=2, relief="raised", bg="lightgray")
    window_id = parent_canvas.create_window(0, 0, window=frame, anchor="ne")

    def fix_position(event=None):
        parent_canvas.coords(window_id, parent_canvas.winfo_width() - 5, 5)

    parent_canvas.bind("<Configure>", fix_position)

    def login():
        username = simpledialog.askstring("Login", "Enter Account Name:")
        if not username:
            return
        password = simpledialog.askstring("Login", "Enter Account Password:", show="*")
        if not password:
            return
        try:
            cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", f"Account '{username}' created.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Account already exists")

    def logout():
        username = simpledialog.askstring("Logout", "Enter Account Name to delete:")
        if not username:
            return
        cur.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", f"Account '{username}' deleted.")
        else:
            messagebox.showerror("Error", "Account not found")

    tk.Button(frame, text="Logout", fg="red", activebackground="red", command=logout).pack(pady=5, padx=10)
    tk.Button(frame, text="Login", fg="green", activebackground="green", command=login).pack(pady=5, padx=10)

    return frame
