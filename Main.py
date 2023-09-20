from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBook import *
from IssueBook import *
from ReturnBook import *

mypass = "YESs" #use your own password
mydatabase="db" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library Management System")
#root.minsize(width=400,height=400)
root.geometry("1920x1080")

same=True
n=0.25
# Adding a background image
background_image =Image.open("lib2.jpg")
[imageSizeWidth, imageSizeHeight] = (10000,4016)
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="blue",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="white",bd=5)
headingFrame1.place(relx=0.31,rely=0.1,relwidth=0.35,relheight=0.20)
#headingFrame1.attribute('-alpha, 0.2')
headingLabel = Label(headingFrame1, text="Welcome to \nThe Neotia University's Library", bg='orange', fg='black', font=('Courier 20 bold italic'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="Add Book Details",bg='white', fg='black', font=('calibri 18 bold'), command=addBook)
btn1.place(relx=0.33,rely=0.4, relwidth=0.30,relheight=0.06)
#btn1.attribute('-alpha, 0.2')
    
btn2 = Button(root,text="Delete Book",bg='white', fg='black',font=('Calibri 18 bold'), command=delete)
btn2.place(relx=0.33,rely=0.46, relwidth=0.30,relheight=0.06)
#btn2.attribute('-alpha, 0.2')
    
btn3 = Button(root,text="View Book List",bg='white', fg='black',font=('Calibri 18 bold'), command=View)
btn3.place(relx=0.33,rely=0.52, relwidth=0.30,relheight=0.06)
#btn3.attribute('-alpha, 0.2')
    
btn4 = Button(root,text="Issue Book to Student",bg='white', fg='black',font=('Calibri 18 bold'), command = issueBook)
btn4.place(relx=0.33,rely=0.58, relwidth=0.30,relheight=0.06)
#btn4.attribute('-alpha, 0.2')

btn5 = Button(root,text="Return Book",bg='white', fg='black',font=('Calibri 18 bold'), command = returnBook)
btn5.place(relx=0.33,rely=0.64, relwidth=0.30,relheight=0.06)
#btn5.attribute('-alpha, 0.2')

root.mainloop()