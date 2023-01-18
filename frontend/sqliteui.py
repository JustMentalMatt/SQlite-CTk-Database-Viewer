import sqlite3
import customtkinter
import tkinter
from tkinter import ttk
from customtkinter import *


def display_table():
    conn = sqlite3.connect('./backend/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Admin_Users")
    rows = c.fetchall()

    root = customtkinter.CTk()
    root.title("My Database Table")

    t = ttk.Treeview(root)
    t["columns"] = ("one", "two", "three", "four", "five")
    t.heading("#0", text="ID")
    t.column("#0", minwidth=0, width=50, stretch=NO)
    t.heading("one", text="Name")
    t.column("one", minwidth=0, width=100, stretch=NO)
    t.heading("two", text="Email")
    t.column("two", minwidth=0, width=100, stretch=NO)
    t.heading("three", text="Join Date")
    t.column("three", minwidth=0, width=100, stretch=NO)
    t.heading("four", text="Username")
    t.column("four", minwidth=0, width=100, stretch=NO)
    t.heading("five", text="Password")
    t.column("five", minwidth=0, width=100, stretch=NO)

    for row in rows:
        t.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    t.pack()
    root.mainloop()

    
    conn = sqlite3.connect('./backend/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Admin_Users")
    rows = c.fetchall()
    t = ttk.Treeview(sqlUIFrame)
    t["columns"] = ("one", "two", "three", "four", "five")
    t.heading("#0", text="ID")
    t.column("#0", minwidth=0, width=50, stretch=NO)
    t.heading("one", text="Name")
    t.column("one", minwidth=0, width=200, stretch=NO)
    t.heading("two", text="Email")
    t.column("two", minwidth=0, width=200, stretch=NO)
    t.heading("three", text="Join Date")
    t.column("three", minwidth=0, width=200, stretch=NO)
    t.heading("four", text="Username")
    t.column("four", minwidth=0, width=200, stretch=NO)
    t.heading("five", text="Password")
    t.column("five", minwidth=0, width=200, stretch=NO)

    for row in rows:
        t.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    t.grid(column=0, columnspan=5, row=0, rowspan=2, ipadx=10, ipady=10, sticky="SWEN")