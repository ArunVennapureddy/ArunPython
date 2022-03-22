from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "onlineshopping"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()



def showAll():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def CreateUI(self):
            tv = Treeview(self)
            tv['columns'] = ('Product Id', 'Product Name', 'Color', 'Quality', 'Price', 'Model', )
            tv.heading('#0', text='Product Id', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='Product Name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Color', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='Quality', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Price', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Model', anchor='center')
            tv.column('#5', anchor='center')
            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select = "Select * from products"
            cur.execute(Select)
            result = cur.fetchall()
            ProductId = ""
            ProductName = ""
            Color = ""
            Quality = ""
            Price = ""
            Model = ""
            for i in result:
                ProductId = i[0]
                ProductName = i[1]
                Color = i[2]
                Quality = i[3]
                Price = i[4]
                Model = i[5]
                self.treeview.insert("", 'end', text=ProductId,
                                     values=(ProductName, Color, Quality, Price, Model))

    root = Tk()
    root.title("Overview Page")
    A(root)
