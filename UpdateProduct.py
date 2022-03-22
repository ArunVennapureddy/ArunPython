from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "onlineshopping"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def update_product():
    update_product = Tk()
    update_product.title("Update Products")
    update_product.geometry("600x500")

    def edit_plan():
        sql_c = """UPDATE products SET  product_name=%s, product_color=%s, quality_type=%s, price=%s, model_no=%s WHERE product_id = %s """
        

        prodId = e11.get()
        prodName = e22.get()
        prodColor = e33.get()
        prodQual = e44.get()
        prodPric = e55.get()
        prodModel = e66.get()
  

        input = (prodName, prodColor, prodQual, prodPric, prodModel,  prodId)
        cur.execute(sql_c, input)

        con.commit()
        messagebox.showinfo("Record Updated!!")
        update_product.destroy()

    def search_up():
        search_edit = search_box.get()
        sqlcommand = "SELECT * FROM products WHERE product_id = %s"
        name = (search_edit,)
        result2 = cur.execute(sqlcommand, name)
        result2 = cur.fetchall()

        if not result2:
            messagebox.showinfo("No Results")
        else:
            # print(result2)
            for x in result2:
                plan = x[0]

            # result_label = Label(update_product, text=result2)
            # result_label.grid(row=2, column=0, padx=10)
            #
            # edit_button = Button(update_product, text="Edit")
            # edit_button.grid(row=3, column=0)

        planId = Label(update_product, text="prodId", width=20, height=2).grid(row=12, column=0, sticky=W)
        PlanName = Label(update_product, text="Prod Name", width=20, height=2).grid(row=13, column=0, sticky=W)
        PlanStartDate = Label(update_product, text="prod Color", width=20, height=2).grid(row=14, column=0, sticky=W)
        PlanEndDate = Label(update_product, text="prod Qual", width=20, height=2).grid(row=15, column=0, sticky=W)
        PlanValidityDays = Label(update_product, text="prod Price", width=20, height=2).grid(row=16, column=0, sticky=W)
        PlanValidityDays = Label(update_product, text="prodModel", width=20, height=2).grid(row=17, column=0, sticky=W)

        global e11
        e11 = Entry(update_product, width=30, borderwidth=2)
        e11.grid(row=12, column=1)
        e11.insert(0, result2[0][0])
        e11.config(state=DISABLED)
        global e22
        e22 = Entry(update_product, width=30, borderwidth=2)
        e22.grid(row=13, column=1)
        e22.insert(0, result2[0][1])
        global e33
        e33 = Entry(update_product, width=30, borderwidth=2)
        e33.grid(row=14, column=1)
        e33.insert(0, result2[0][2])
        global e44
        e44 = Entry(update_product, width=30, borderwidth=2)
        e44.grid(row=15, column=1)
        e44.insert(0, result2[0][3])
        global e55
        e55 = Entry(update_product, width=30, borderwidth=2)
        e55.grid(row=16, column=1)
        e55.insert(0, result2[0][4])
        global e66
        e66 = Entry(update_product, width=30, borderwidth=2)
        e66.grid(row=17, column=1)
        e66.insert(0, result2[0][4])

        submit_button = Button(update_product, text="Submit", command=edit_plan)
        submit_button.grid(row=20, column=0)

    def clear_fields():
        e11.delete(0, END)
        e22.delete(0, END)
        e33.delete(0, END)
        e44.delete(0, END)
        e55.delete(0, END)

    search_box = Entry(update_product)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    search_box_label = Label(update_product, text="Search product to update using prod Id")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_up_button = Button(update_product, text="Search", command=search_up)
    search_up_button.grid(row=1, column=0, padx=10)

    # button
    quitBtn = Button(update_product, text="CLEAR", bg='#f7f1e3', fg='black', command=clear_fields)
    quitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(update_product, text="QUIT", bg='#f7f1e3', fg='black', command=update_product.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    update_product.mainloop()
