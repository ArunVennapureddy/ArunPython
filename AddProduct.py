from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def productRegister():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    prodId = product_id.get()
    prodName = product_name.get()
    prodColor = product_color.get()
    prodQual = quality_type.get()
    prodPric = price.get()
    prodModel = model_no.get()
  
    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase = "onlineshopping"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    if product_id != "" and product_name != "" and product_color != "" and quality_type != "" and price != "" and model_no != "" :
        insert_Data = "Insert into products(product_id,product_name,product_color,quality_type,price,model_no) value (%s,%s,%s,%s,%s,%s)"
        value = (prodId,prodName,prodColor,prodQual,prodPric,prodModel)
        print(value)
        cur.execute(insert_Data, value)
        con.commit()
        messagebox.showinfo("Info", "Record Inserted")
    else:
        messagebox.showinfo("Info", "Enter Valid Records")
    
   
    root.destroy()
    
def addProduct(): 
    
    global product_id,product_name,product_color,quality_type,price,model_no
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#F8F9F9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#F8F9F9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD A PRODUCT",bg='#F8F9F9', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#F8F9F9')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
        
    headingFrame1 = Frame(root,bg="#F8F9F9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD A BOOK",bg='#F8F9F9', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#F8F9F9')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Product ID
    lb1 = Label(labelFrame,text="Product ID : ",bg='#F8F9F9', fg='black')
    lb1.place(relx=0.05,rely=0.02, relheight=0.08)
        
    product_id = Entry(labelFrame)
    product_id.place(relx=0.3,rely=0.02, relwidth=0.62, relheight=0.08)
        
    # name
    lb2 = Label(labelFrame,text="Product Name",bg='#F8F9F9', fg='black')
    lb2.place(relx=0.05,rely=0.15, relheight=0.08)
        
    product_name = Entry(labelFrame)
    product_name.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.08)
        
    #color
    lb3 = Label(labelFrame,text="Product Color : ",bg='#F8F9F9', fg='black')
    lb3.place(relx=0.05,rely=0.30, relheight=0.08)
        
    product_color = Entry(labelFrame)
    product_color.place(relx=0.3,rely=0.30, relwidth=0.62, relheight=0.08)
        
    # Quality
    lb4 = Label(labelFrame,text="Quality",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.45, relheight=0.08)

    quality_type = Entry(labelFrame)
    quality_type.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # price
    lb5 = Label(labelFrame, text="price",bg='#F8F9F9', fg='black')
    lb5.place(relx=0.05, rely=0.60, relheight=0.08)

    price = Entry(labelFrame)
    price.place(relx=0.3, rely=0.60, relwidth=0.62, relheight=0.08)

    # model no
    lb6 = Label(labelFrame, text="model no: ",bg='#F8F9F9', fg='black')
    lb6.place(relx=0.05, rely=0.75, relheight=0.08)

    model_no= Entry(labelFrame)
    model_no.place(relx=0.3, rely=0.75, relwidth=0.62, relheight=0.08)
    

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#82E0AA', fg='black',command=productRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#EC7063', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    
    root.mainloop()
