import tkinter as tk
from tkinter import messagebox
from getpass import getpass
import os
from auth import hash_password,verify_master_password
from database import add_password,view_password,update_password,delete_password
from crypto import encrypt_password, decrypt_password
import hashlib

root= tk.Tk()
root.title("Password Manager - Login")
root.geometry("400x300")
root.resizable(False,False)

#which writes the master passwords in gui
def add_master_pass_gui():
    set_win = tk.Toplevel(root)
    set_win.title("Setup Master Password")

    tk.Label(set_win, text="Enter the master password").pack(pady=10)
    master = tk.Entry(set_win, show="*")
    master.pack()

    tk.Label(set_win, text="Confirm Password").pack(pady=10)
    confirm = tk.Entry(set_win, show="*")
    confirm.pack()

    def save():
        master_pass = master.get()
        confirm_pass = confirm.get()
        if master_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            hashed = hash_password(master_pass)
            with open("master.hash", "w") as file:
                file.write(hashed)
            messagebox.showinfo("Success", "Password set")
            set_win.destroy()

    tk.Button(set_win, text="Confirm", command=save).pack(pady=20)


#login to main part
def login():
    password= password_entry.get()
    password= hash_password(password)
    if verify_master_password(password):
        messagebox.showinfo("Access Granted !!")
        root.destroy()
        open_menu()
    
    else:
        messagebox.showerror("Error ! Access Denied.")


def open_menu():
    menu = tk.Tk()
    menu.title("--Menu Page--")
    menu.geometry("400x350")
    menu.resizable(False,False)

    tk.Label(menu, text="Welcome to Password Manager", font=("Arial" ,14)).pack(pady=15)

    #Database programs in GUI
    def add_password_gui():
        set_win = tk.Toplevel(menu)
        set_win.title("Add Password")
        set_win.geometry("400x300")
        set_win.resizable(False,False)

        tk.Label(set_win, text="Enter username").pack(pady=10)
        u_name = tk.Entry(set_win)
        u_name.pack()
        
        tk.Label(set_win, text="Enter email").pack(pady=10)
        email = tk.Entry(set_win)
        email.pack()

        tk.Label(set_win, text="Enter password").pack(pady=10)
        p_word = tk.Entry(set_win, show="*")
        p_word.pack()

        def save():
            entered_username = u_name.get()
            entered_email = email.get()
            entered_password = p_word.get()
            add_password(entered_username,entered_email,entered_password)
            messagebox.showinfo("Successfully added!!")
            set_win.destroy()
        
        tk.Button(set_win, text="Save", command=save).pack(pady=15)

    #View the password from GUI
    def view_password_gui():
        view_win = tk.Toplevel(menu)
        view_win.title("Look Password")
        view_win.geometry("400x350")
        view_win.resizable(False,False)

        tk.Label(view_win, text="Enter username").pack(pady=10)
        u_name = tk.Entry(view_win)
        u_name.pack()

        tk.Label(view_win, text="Enter email").pack(pady=10)
        email = tk.Entry(view_win)
        email.pack()

        password_entered = {"value": None}

        def look():
            entered_username = u_name.get()
            entered_email = email.get()

            password = view_password(entered_username,entered_email)
            password_entered["value"] = password

            hide_password = ""
            if not password :
                messagebox.showerror("Error ! Not Found")
            else:
                for i in range(len(password)):
                    if i % 2 == 0:
                        hide_password += password[i]
                    else:
                        hide_password += "*"

                messagebox.showinfo("Password", f"Password : {hide_password}")
                show_btn.config(state="normal")

        def show_full_password():
            messagebox.showinfo("Password", f"Password : {password_entered["value"]}")

        
        show_btn = tk.Button(view_win, text="Show Password", command=show_full_password, state="disabled")
        show_btn.pack(pady=10)

        tk.Button(view_win, text="View", command=look).pack(pady=20)

   
    #Update password in gui based system
    def update_password_gui():
        up_win = tk.Toplevel(menu)
        up_win.title("Update Password")
        up_win.geometry("400x350")
        up_win.resizable(False,False)

        tk.Label(up_win, text="Username").pack(pady=10)
        u_name = tk.Entry(up_win)
        u_name.pack()

        tk.Label(up_win, text="Email").pack(pady=10)
        email = tk.Entry(up_win)
        email.pack()

        def check_data():
            entered_username = u_name.get()
            entered_email = email.get()
            password = view_password(entered_username, entered_email)
            if not password:
                messagebox.showerror("Error","Not Found !")
            else:
                up_win.destroy()
                update_win = tk.Toplevel(menu)
                update_win.title("Update Password")
                update_win.geometry("400x350")
                update_win.resizable(False,False)

                tk.Label(update_win, text="New Password").pack(pady=10)
                new_password = tk.Entry(update_win, show="*")
                new_password.pack()

                tk.Label(update_win, text="Confirm Password").pack(pady=10)
                confirm_password = tk.Entry(update_win, show="*")
                confirm_password.pack()

                def update():
                    entered_new_password = new_password.get()
                    entered_confirm_password = confirm_password.get()
                    result = update_password(entered_username, entered_email, entered_new_password, entered_confirm_password)

                    if result:
                        messagebox.showinfo("Sucess", "Password Updated !")
                    else:
                        messagebox.showerror("Error","Confirm not matched !")
            
            tk.Button(update_win, text="Update", command=update).pack(pady= 20)


        
        tk.Button(up_win, text="Find", command=check_data).pack(pady= 20)

    #Delete the records
    def delete_password_gui():

        del_win = tk.Toplevel(menu)
        del_win.title("Delete Info")
        del_win.geometry("400x350")
        del_win.resizable(False,False)

        tk.Label(del_win, text= "Username").pack(pady=10)
        u_name = tk.Entry(del_win)
        u_name.pack()

        tk.Label(del_win, text= "Email").pack(pady=10)
        email = tk.Entry(del_win)
        email.pack()

        

        def delete():
            entered_username = u_name.get()
            entered_email = email.get()
            result = delete_password(entered_username, entered_email)

            if result:
                messagebox.showinfo("Success","Deleted !")
            else:
                messagebox.showerror("Error","Not Found !")

        tk.Button(del_win, text="Delete", command=delete).pack(pady=20)

    tk.Button(menu, text="Add Password",command=add_password_gui , width=25).pack(pady=5)
    tk.Button(menu, text="View Password", command=view_password_gui, width=25).pack(pady=5)
    tk.Button(menu, text="Update Password", command=update_password_gui,width=25).pack(pady=5)
    tk.Button(menu, text="Delete Password", command=delete_password_gui,width=25).pack(pady=5)
    
    
    menu.mainloop()


##Main part{
if not os.path.exists("master.hash"):
    messagebox.showinfo("First Create the master password.!")
    add_master_pass_gui()
#windows display 
tk.Label(root, text = "Enter the master password").pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text = "Login", command=login).pack(pady=20)


root.mainloop()
##}
