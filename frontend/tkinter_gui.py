import tkinter
import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    sqliteConnection = sqlite3.connect('./backend/database.db')
    cursor = sqliteConnection.cursor()
    credential_fetch = "SELECT username, password FROM Admin_Users"
    cursor.execute(credential_fetch)
    results = cursor.fetchall()
    
    for row in results:
        username = row[0]
        password = row[1]
        print(username, password)
        
        if entry1.get() == username and entry2.get() == password:
            print("Login Successful") #i love jake he is so fit omg give me his number

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me?")
checkbox.pack(pady=12, padx=10)

root.mainloop()