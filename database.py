from getpass import getpass
import sqlite3
from crypto import encrypt_password,decrypt_password

#For Viewing the stored passwords
def view_password(u_name,email):
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT password FROM accounts WHERE username = ? AND login = ?""",(u_name,email))

    result = cursor.fetchall()

    if result:
        for record in result:
            encrypted_password= record[0]
            decrypt= decrypt_password(encrypted_password)
        return decrypt
    else:
        return False

    conn.close()

#Add new login in table
def add_password(u_name,email,password):
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()

    encrypt = encrypt_password(password)

    cursor.execute("INSERT INTO accounts (username,login,password) VALUES(?,?,?)",(u_name,email,encrypt))

    conn.commit()
    conn.close()

#delete the existing login
def delete_password(u_name, email):
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()


    cursor.execute("SELECT password FROM accounts WHERE username=? AND login=?",(u_name,email))

    result = cursor.fetchall()

    if result :
        cursor.execute("DELETE FROM accounts WHERE username=? AND login=?",(u_name,email))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

    

#update the existing login
def update_password(u_name, email, new_password, confirm_password):

    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()

    if new_password == confirm_password:
        encrypt= encrypt_password(new_password)
        cursor.execute("UPDATE accounts SET password=? WHERE username=? AND login=?",(encrypt,u_name,email))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
        

    
