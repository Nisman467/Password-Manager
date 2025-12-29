from cryptography.fernet import Fernet 
import os

#generates a key 
def generate_key():
    key= Fernet.generate_key()

    with open("Key.key","wb") as file:
        file.write(key)

#read Key
def read_key():
    if not os.path.exists("Key.key"):
        generate_key()

    with open("Key.key","rb") as file:
        return file.read()

load_key= read_key()
fernet= Fernet(load_key)

#encrypt password
def encrypt_password(password):
    return fernet.encrypt(password.encode())

#decrypt password
def decrypt_password(encrypt_password):
    return fernet.decrypt(encrypt_password).decode()