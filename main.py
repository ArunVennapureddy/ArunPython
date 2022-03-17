from MainMenu import *
from SearchPlan import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import pymysql
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="onlineshopping"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Login")
root.geometry("600x480")

def login():
    usern = username_box.get()
    passw = password_box.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are required")
    else:
        try:
            cur.execute("select * from users where userId=%s and Password=%s", (usern, passw))
            op = cur.fetchone()
            print(op)
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")
            else:
                root.destroy()
                mainmenu()
        except EXCEPTION as es:
            messagebox.showerror("Error"f"Error Due to: {str(es)}")


bg = ImageTk.PhotoImage(file="lib.jpg")
bg_image = Label(root, image=bg).grid()

del_frame = Frame(root, bd=4, relief=RIDGE, bg="#7393B3")
del_frame.place(x=100, y=300, width=500, height=280)

# Label for username and password
username = Label(del_frame, text="USER ID", bg="#7393B3", fg="black", font=15)
username.grid(row=12, column=0, sticky=W, padx=10, pady=10)
password = Label(del_frame, text="PASSWORD", bg="#7393B3", fg="black", font=15)
password.grid(row=14, column=0, sticky=W, padx=10, pady=10)

# Text boxes for username and password
global username_box
username_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
username_box.grid(row=12, column=1, pady=10, padx=10, sticky="w")

global password_box
password_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
password_box.grid(row=14, column=1, pady=10, padx=10, sticky="w")
password_box.config(show="*");

usern = username_box.get()
passw = password_box.get()

# Login Button
login = Button(del_frame, text="Login", fg="black", font=15,command=login)
login.grid(row=20, column=1, pady=10, padx=10)

root.mainloop()

