from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddProduct import *
from DeleteProduct import *
#from SearchProduct import *
from UpdateProduct import *
from showAllRecord import *
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="onlineshopping"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def mainmenu():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Take n greater than 0.25 and less than 5
    same = True
    n = 0.25

    # Adding a background image
    background_image = Image.open("lib1.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FDFEFE", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome \nto \n TECH007 MART", bg='#FDFEFE', fg='#17202A',
                         font='40')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Add a product ", bg='#AED6F1', fg='black', command=addProduct)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete a Product", bg='#AED6F1', fg='black', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="Update product", bg='#AED6F1', fg='black', command=update_product)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Show All products", bg='#AED6F1', fg='black', command=showAll)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    #btn5 = Button(root, text="Search a product", bg='#AED6F1', fg='black', command=Searchproduct)
    #btn5.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
    root.mainloop()
