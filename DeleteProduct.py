from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="onlineshopping"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()




def deleteProd():

    prodId = productId.get()
    deleteByprodId = "Delete from products where product_id = '%s'" % prodId

    try:
        cur.execute(deleteByprodId)
        con.commit()
        messagebox.showinfo("Information", "Record Deleted")
    except:
        messagebox.showinfo("Please check prod ID")

    print(deleteByprodId)

    root.destroy()
    
def delete(): 
    
    global productId,Canvas1,con,cur,root
    
    root = Tk()
    root.title("Delete")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FDFEFE")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FDFEFE",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete A Product", bg='#FDFEFE', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#FDFEFE')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Plan ID to Delete
    lb1 = Label(labelFrame,text="Prod ID: ", bg='#FDFEFE', fg='black')
    lb1.place(relx=0.05,rely=0.5)
        
    productId = Entry(labelFrame)
    productId.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=deleteProd)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
