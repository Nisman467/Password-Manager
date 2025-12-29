from getpass import getpass
import os
import hashlib


#encrypt the master password
def hash_password(master):
    return(hashlib.sha256(master.encode()).hexdigest())

#set the master password
def add_master_pass():
    master= getpass("Enter the master password : ")
    conform= getpass("Conform the password : ")

    if conform != master :
        print("Conform password doesnot match.")
        return False
    
    hashed = hash_password(master)
    with open ("master.hash","w") as file:
        file.write(hashed)

    print("Master Password Set Successfully !!")

#checks whether the master pass is matched
def verify_master_password(password_entry):
    
    with open("master.hash","r") as file:
        saved_master= file.read()

    if saved_master == password_entry:
        return True
    else:
        return False

