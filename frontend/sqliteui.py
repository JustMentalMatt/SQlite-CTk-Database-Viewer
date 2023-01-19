import sqlite3
import customtkinter
import tkinter
from tkinter import ttk
from customtkinter import *
# from mainwindow import sqlUI


def admin_usersTable():
    conn = sqlite3.connect('./backend/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Admin_Users")
    rows = c.fetchall()
    t = ttk.Treeview(sqlUI)
    t["columns"] = ("one", "two", "three", "four", "five")
    t.heading("#0", text="ID")
    t.column("#0", minwidth=50, width=50, stretch=YES)
    t.heading("one", text="Name")
    t.column("one", minwidth=150, width=150, stretch=YES)
    t.heading("two", text="Email")
    t.column("two", minwidth=200, width=200, stretch=YES)
    t.heading("three", text="Join Date")
    t.column("three", minwidth=150, width=150, stretch=YES)
    t.heading("four", text="Username")
    t.column("four", minwidth=150, width=150, stretch=YES)
    t.heading("five", text="Password")
    t.column("five", minwidth=150, width=150, stretch=YES)

    for row in rows:
        t.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    t.grid(column=0, columnspan=5, row=0, rowspan=2, padx=5, ipadx=10, ipady=10, sticky="NS")
    
admin_usersTable()
