import customtkinter
import sqlite3

def mainWindow():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("1280x720")
    root.title("Database Viewer")
    root.resizable(False,False)
    
                                            # --------- Frames --------- #:
    
    # Title Box:
    titleboxFrame = customtkinter.CTkFrame(master=root)
    titleboxFrame.grid(column=0, columnspan=2, row=0, rowspan=1, ipadx=5, ipady=5, padx=20, pady=20, sticky="nsew")
    tb_title = customtkinter.CTkLabel(master=titleboxFrame, text="SQLite Database Viewer", font=("Roboto", 24, "underline",))
    tb_title.grid(column=0, row=0, ipadx=10, ipady=10, sticky="nsew")
    tb_text = customtkinter.CTkLabel(master=titleboxFrame, text=" Database Viewer V1    ~    Author: Ma 💕", font=("Roboto", 12))
    tb_text.grid(column=0, columnspan=2, row=1, ipadx=10, sticky="w")
    
    # User Info Box:
    usrinfoFrame = customtkinter.CTkFrame(master=root)
    usrinfoFrame.grid(column=0, columnspan=2, row=2, rowspan=1, ipadx=5, ipady=5, padx=20, pady=10, sticky="nsew")
    usrName = customtkinter.CTkLabel(master=usrinfoFrame, text="¬ Logged in as: ", font=("Roboto", 14))
    usrName.grid(column=0, row=0, ipadx=10, ipady=10, sticky="SW")
    usrAuth = customtkinter.CTkLabel(master=usrinfoFrame, text="¬ Auth Level:  ", font=("Roboto", 14))
    usrAuth.grid(column=0, row=2, ipadx=10, sticky="SW")
    
    # Button Box:
    btnboxFrame = customtkinter.CTkFrame(master=root)
    btnboxFrame.grid(column=0, columnspan=2, row=0, rowspan=10, ipadx=20, ipady=20, padx=20, pady=20, sticky="nsew")
    

#########################################################################################################################


    # tableText = customtkinter.CTkLabel(master=btnboxFrame, text="Browse Tables:", font=("Roboto", 24))
    # tableText.grid(column=0, row=0, pady=(20, 0), sticky="nsew")
    
    # def optionmenu_callback(choice):
    #     print("optionmenu dropdown clicked:", choice)

    # combobox = customtkinter.CTkOptionMenu(master=frame, values=["Admin_Users", "Guest_Users"], command=optionmenu_callback) 
                                          
                                                                         
    # combobox.grid(row=1, column=1)
    # combobox.set("TABLES")  # set initial value
    
    
    root.mainloop()
    
mainWindow()