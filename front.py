import back
import pymysql
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 

# database connection section
# Open database connection
db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# disconnect from server
db.close()


def guiPy():
	root = Tk()
	root.title("Blood Bank Database")
	root.geometry("576x864")

	img1 = ImageTk.PhotoImage(Image.open('/home/deeksha/PROJECT/Blood4.jpg'))
	lbl1 = Label(root, image = img1) 
	lbl1.pack()

	### ----------- contents under frame 1 --------###

	frame1 = LabelFrame(root, text = "New Registrations", padx = 5, pady = 5, fg = "green")
	frame1.place(x = 144, y = 100)
	
	#---BUTTONS---#

	donor_button = Button(frame1, text = "Donor", bg = "green", fg = "white", command = back.create_donor)
	BB_button = Button(frame1, text = "Blood Bank", bg = "green", fg = "white", command = back.reg_BB)
	H_button = Button(frame1, text= "Hospital", bg = "green", fg = "white", command = back.Hos)

	donor_button.grid(row = 0, column = 0)
	BB_button.grid(row = 0, column = 1)
	H_button.grid(row = 0, column = 2)

	### ----------- contents under frame 2 --------###
	frame2 = LabelFrame(root, text = "Connect to Donor", padx = 10, pady = 10, fg = "red")
	frame2.place(x = 144, y = 200)

	#---BUTTONS---#
	contact = Button(frame2, text = "Contact Donor", bg = "orange", fg = "black", command = back.con)
	contact.grid(row = 0, column = 0)


	### ----------- contents under frame 3 --------###
	
	frame3 = LabelFrame(root, text = "Log section", padx = 5, pady = 5, fg = "red")
	frame3.place(x = 144, y = 300)
	
	#---BUTTONS---#

	blood_button = Button(frame3, text = "Log Blood Donation", bg = "red", fg = "black", command = back.donate)
	dist_button = Button(frame3, text = "Log Distribution", bg = "red", fg = "black", command = back.dist)

	blood_button.grid(row = 0, column = 0)
	dist_button.grid(row = 0, column = 1)


	root.mainloop()


### - - - - LOGIN PAGE - - - - ###

def validateLogin():
    if(username.get() == "admin" and password.get() == "test123"):
        tkWindow.destroy()
        guiPy()
    else:
        ll1 = Label(tkWindow, text="Incorrect username or password"
        ,fg="white",bg="red").place(x = 80, y = 80)


tkWindow = Tk()
tkWindow.geometry('1200x900')
tkWindow.title('Blood Bank Database')
#tkWindow.configure(bg = "red")

img2 = ImageTk.PhotoImage(Image.open('/home/deeksha/PROJECT/Blood3.jpeg'))
lbl2 = Label(tkWindow, image = img2) 
lbl2.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)

to = LabelFrame(tkWindow)
to.place(x = 0, y = 0)

usernameLabel = Label(to, text="User Name").grid(row=0, column=0, padx = 10, pady = 10)
username = StringVar()
usernameEntry = Entry(to, textvariable=username).grid(row=0, column=1, padx = 10, pady = 10)

passwordLabel = Label(to, text="Password", width = 9).grid(row=1, column=0, padx = 10, pady = 10)
password = StringVar()
passwordEntry = Entry(to, textvariable=password,
                      show='*').grid(row=1, column=1, padx = 10, pady = 10)

loginButton = ttk.Button(to, text="Login",
                         command=validateLogin).grid(row=2, column=0, padx = 10, pady = 10)

tkWindow.mainloop()

#guiPy()