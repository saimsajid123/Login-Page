import customtkinter as ct
from customtkinter import *
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

root=ct.CTk()
root.geometry("1366x768")

def login():
    print("Test")
    

frame=ct.CTkFrame(master=root)
frame.pack(padx=10,pady=10,fill="both",expand=True)

lable=ct.CTkLabel(master=frame,text="Log in",font=("Arial",18))
lable.pack(padx=10,pady=12)

entry1=ct.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(padx=12,pady=10)
entry2=ct.CTkEntry(master=frame,placeholder_text="Password",show="*")
entry2.pack(padx=12,pady=10)

button=ct.CTkButton(master=frame,text="Login",font=("Arial",18),command=login)
button.pack(padx=12,pady=10)

checkbox=ct.CTkCheckBox(master=frame,text="remember me")
checkbox.pack(padx=12,pady=10)

root.mainloop()