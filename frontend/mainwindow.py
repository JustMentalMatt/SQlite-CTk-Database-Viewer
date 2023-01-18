import customtkinter
import sqlite3

def mainWindow():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("1280x720")


    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    tableText = customtkinter.CTkLabel(master=frame, text="Browse Tables:", font=("Roboto", 24))
    tableText.pack(side="left", pady=0, padx=10)
    
    grid = customtkinter.CTkFrame(master=frame)
    grid.pack(pady=300, padx=60, fill="both", expand=False)
        
    

    def optionmenu_callback(choice):
        print("optionmenu dropdown clicked:", choice)

    combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["Admin_Users", "Guest_Users"],
                                       command=optionmenu_callback)
    combobox.pack(padx=20, pady=10)
    combobox.set("TABLES")  # set initial value
    
    root.title("Database Viewer")
    root.resizable(False,False)
    root.mainloop()
    
mainWindow()