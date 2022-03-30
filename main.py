from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

# item register
def itemRegister():
    # getting information from client
    bid = info1.get()
    title = info2.get()
    author = info3.get()
    status = info4.get()
    status = status.lower()
    
    # sql
    insertItem = "insert into books values ('" + bid + "', '" + title + "', '" + author + "', '" + status + "')"
    try:
        # trying to send query to database
        cursor.execute(insertItem)
        connection.commit()
        messagebox.showinfo("Success", "Item added successfully!")
    except:
        messagebox.showinfo("Error", "The item was not added.")

# add item
def addItem():
    # setting global variables
    global info1, info2, info3, info4
    # additem window (this will happen for every new function)
    win = Tk()
    win.title("Management System")
    win.minsize(width=800, height=600)
    win.configure(bg="#6b6b6b")
    
    canvas = Canvas(win)
    
    canvas.config(bg="grey")
    canvas.pack(expand=True, fill=BOTH)
    
    # frames and labels
    hframe = Frame(win, bg="#2e2e2e")
    hframe.place(rely=0.1, relwidth=1, relheight=0.1)
    hlabel = Label(hframe, text="Add Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15))
    hlabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    lframe = Frame(win, bg="#6b6b6b")
    lframe.place(relx=0.18, rely=0.28, relwidth=0.62, relheight=0.60)
    
    lb1 = Label(lframe, text="Item ID: ", fg="#2e2e2e", bg="#6b6b6b")
    lb1.place(relx=0.05, rely=0.15, relheight=0.08)
    info1 = Entry(lframe)
    info1.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.08)
    
    lb2 = Label(lframe, text="Item title: ", fg="#2e2e2e", bg="#6b6b6b")
    lb2.place(relx=0.05, rely=0.3, relheight=0.08)
    info2 = Entry(lframe)
    info2.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)
    
    lb3 = Label(lframe, text="Item author: ", fg="#2e2e2e", bg="#6b6b6b")
    lb3.place(relx=0.05, rely=0.45, relheight=0.08)
    info3 = Entry(lframe)
    info3.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.08)
    
    lb4 = Label(lframe, text="Item status: ", fg="#2e2e2e", bg="#6b6b6b")
    lb4.place(relx=0.05, rely=0.6, relheight=0.08)
    info4 = Entry(lframe)
    info4.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)
    
    sbtn = Button(win, text="Submit", bg="#2e2e2e", fg="black", command=itemRegister)
    sbtn.place(relx=0.53, rely=0.74, relwidth=0.18, relheight=0.08)
    
    qbtn = Button(win, text="Back", bg="#2e2e2e", fg="black", command=win.destroy)
    qbtn.place(relx=0.28, rely=0.74, relwidth=0.18, relheight=0.08)
    # deleting stored datas
    info1.delete(0, END)
    info2.delete(0, END)
    info3.delete(0, END)
    info4.delete(0, END)
    # mainloop
    win.mainloop()
# delete method database query
def delete():

    itemid = info1.get()
    # deleting from books and book_issued tables (it was supposed to be a books system, that's why these table names were given)
    deleteItem = "delete from books where bid = " + itemid
    deleteIssue = "delete from books_issued where bid = " + itemid

    try:
        cursor.execute(deleteItem)
        connection.commit()
        cursor.execute(deleteIssue)
        connection.commit()
        messagebox.showinfo("Success","Item deleted successfully!")
    except:
        messagebox.showinfo("Error", "The item was not deleted.")

    info1.delete(0, END)
# deleteitem method
def deleteItem():

    global info1

    win = Tk()
    win.title("Management System")
    win.minsize(width=800, height=600)
    win.configure(bg="#6b6b6b")
    
    canvas = Canvas(win)
    
    canvas.config(bg="grey")
    canvas.pack(expand=True, fill=BOTH)
    
    # frames and labels
    hframe = Frame(win, bg="#2e2e2e")
    hframe.place(rely=0.1, relwidth=1, relheight=0.1)
    hlabel = Label(hframe, text="Delete Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15))
    hlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    lframe = Frame(win, bg="#6b6b6b")
    lframe.place(relx=0.18, rely=0.35, relwidth=0.62, relheight=0.25)
    
    lb1 = Label(lframe, text="Inform the ID of the item you want to be removed.", fg="#2e2e2e", bg="#6b6b6b")
    lb1.place(relx=0.17, rely=-0.2, relheight=1)
    info1 = Entry(lframe)
    info1.place(relx=0.2, rely=0.5, relwidth=0.62, relheight=0.2)

    sbtn = Button(win, text="Delete", bg="#2e2e2e", fg="black", command=delete)
    sbtn.place(relx=0.53, rely=0.74, relwidth=0.18, relheight=0.08)
    
    qbtn = Button(win, text="Back", bg="#2e2e2e", fg="black", command=win.destroy)
    qbtn.place(relx=0.28, rely=0.74, relwidth=0.18, relheight=0.08)

    win.mainloop()
# view method
def viewList():
    win = Tk()
    win.title("Management System")
    win.minsize(width=800, height=600)
    win.configure(bg="#6b6b6b")
    
    canvas = Canvas(win)
    
    canvas.config(bg="grey")
    canvas.pack(expand=True, fill=BOTH)
    
    # frames and labels
    hframe = Frame(win, bg="#2e2e2e")
    hframe.place(rely=0.1, relwidth=1, relheight=0.1)
    hlabel = Label(hframe, text="View List", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15))
    hlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    lframe = Frame(win, bg="#6b6b6b")
    lframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(lframe, text="%-10s%-40s%-30s%-20s"%("ID","   Title","Author","    Status"), bg="#2e2e2e", fg="#b5b5b5").place(relx=0.035, rely=0.1, relwidth=0.926)
    
    getItems = "select * from books"
    y = 0.25

    try:
        cursor.execute(getItems)
        connection.commit()
        # printing every line and column from database
        for i in cursor:
            Label(lframe, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]), bg="#6b6b6b", fg="#2e2e2e").place(relx=0.035, rely=y, relwidth=0.926)
            y += 0.1

    except:
        messagebox.showinfo("Error", "Failed to fetch files from the database.")

    qbtn = Button(win, text="Back", bg="#2e2e2e", fg="black", command=win.destroy)
    qbtn.place(relx=0.41, rely=0.85, relwidth=0.18, relheight=0.08)

    win.mainloop()
    

# connecting to the database
connection = pymysql.connect (host="localhost", user="root", password="123", database="management_system")

# setting the cursor
cursor = connection.cursor()

# creating the main window
win = Tk()
win.title("Management System")
win.minsize(width=800, height=600)
win.configure(bg="#6b6b6b")

# header
hframe = Frame(win, bg="#2e2e2e")
hframe.place(rely=0.1, relwidth=1, relheight=0.1)
hlabel = Label(hframe, text="My Management System", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15))
hlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# adding the buttons
btn1 = Button(win, text="Add Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15), command=addItem)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(win, text="Delete Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15), command=deleteItem)
btn2.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

btn3 = Button(win, text="View List", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15), command=viewList)
btn3.place(relx=0.28, rely=0.70, relwidth=0.45, relheight=0.1)

# btn4 = Button(win, text="Issue Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15), command=issueItem)
# btn4.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

# btn5 = Button(win, text="Return Item", bg="#2e2e2e", fg="#b5b5b5", font=("Times New Roman", 15), command=returnItem)
# btn5.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

# main loop
win.mainloop()


