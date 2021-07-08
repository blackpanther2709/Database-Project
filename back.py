import pymysql
from tkinter import *
from tkinter import ttk

global db 
db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
global cursor 
cursor = db.cursor()
db.close()


###FRAME 1###
#---DEFINITIONS---#
# definition for Donor button
def create_donor():
	def subb(): # accepting data
		sub(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get())

	def sub(d,n,a,s,p,e,b,l):
			
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "insert into Donor values('"+d+"','"+n+"','"+a+"','"+s+"','"+p+"','"+e+"','"+b+"','"+l+"')"

		c.execute(add)

		db.commit()
		db.close()

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)
		e6.delete(0,END)
		e7.delete(0,END)
		e8.delete(0,END)


	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Donor"
						
		c.execute(add)

		row = c.fetchall()

		db.close()

		donor_tree.delete(*donor_tree.get_children())
		for rows in row:
			donor_tree.insert("",END,values =  rows)

	def search(): #SQL query for viewing single record
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Donor WHERE DID = %s"
							
		c.execute(add,e1.get())

		row = c.fetchall()

		db.close()

		donor_tree.delete(*donor_tree.get_children())
		for rows in row:
			donor_tree.insert("",END,values =  rows) 

	#Update records
	def update():

		updon = Tk()
		updon.title('Update Donor Records')

		don = Frame(updon)
		don.grid(row = 0, column = 0)

		ll1 = Label(don, text = "Donor ID:").grid(row = 0, column = 0)
		donorId=StringVar()
		ee1 = Entry(don,textvariable = donorId)
		ee1.grid(row = 0, column = 1)
		ll2 = Label(don, text = "Name:").grid(row = 0, column = 2)
		name=StringVar()
		ee2 = Entry(don,textvariable = name)
		ee2.grid(row = 0, column = 3)
		ll3 = Label(don, text = "Age:").grid(row = 1, column = 0)
		age=StringVar()
		ee3 = Entry(don,textvariable = age)
		ee3.grid(row = 1, column = 1)
		ll4 = Label(don, text = "Sex:").grid(row = 1, column = 2)
		sex=StringVar()
		ee4 = Entry(don,textvariable = sex)
		ee4.grid(row = 1, column = 3)
		ll5 = Label(don, text = "Phone Number:").grid(row = 2, column = 0)
		phno=StringVar()
		ee5 = Entry(don,textvariable = phno)
		ee5.grid(row = 2, column = 1)
		ll6 = Label(don, text = "Email ID:").grid(row = 2, column = 2)
		email=StringVar()
		ee6 = Entry(don,textvariable = email)
		ee6.grid(row = 2, column = 3)
		ll7 = Label(don, text = "Blood Group:").grid(row = 3, column = 0)
		bg=StringVar()
		ee7 = Entry(don,textvariable = bg)
		ee7.grid(row = 3, column = 1)
		ll8 = Label(don, text = "Last Donation Date:").grid(row = 3, column = 2)
		ldd=StringVar()
		ee8 = Entry(don,textvariable = ldd)
		ee8.grid(row = 3, column = 3)


		#Save updated values
		def save():
			db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
			c = db.cursor()

			add = "UPDATE Donor SET DName = %s, Age = %s, Sex = %s, phno = %s, email = %s, bg = %s, LDD = %s WHERE DID = %s"
			c.execute(add,(ee2.get(),ee3.get(),ee4.get(),ee5.get(),ee6.get(),ee7.get(),ee8.get(),ee1.get()))

			db.commit()
			db.close()

			e1.delete(0,END)
			updon.destroy()

		save = Button(don, text = "Save Record", command = save)
		save.grid(row = 5, column = 0, padx = 10, pady =10)

		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()

		add = "SELECT * FROM Donor WHERE DID = %s"
		c.execute(add,(e1.get()))
		records = c.fetchall()

		for record in records:
			ee1.insert(0,record[0])
			ee2.insert(0,record[1])
			ee3.insert(0,record[2])
			ee4.insert(0,record[3])
			ee5.insert(0,record[4])
			ee6.insert(0,record[5])
			ee7.insert(0,record[6])
			ee8.insert(0,record[7])
			
		db.commit()
		db.close()

	#delete operation	
	def delete():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "DELETE FROM Donor WHERE DID = %s"
						
		c.execute(add,(e1.get()))

		db.commit()
		db.close()
		e1.delete(0,END)


	donor_page = Tk()
	donor_page.title('Donor Details')

	#creating tree
	donor_tree = ttk.Treeview(donor_page)

	#define columns
	donor_tree['columns'] = ("DID","DName","Age","Sex","phno","email","bg","LDD")

	#format columns
	donor_tree.column("#0", width = 0, stretch = NO)
	donor_tree.column("DID", anchor = CENTER , width = 120)
	donor_tree.column("DName", anchor = CENTER , width = 120)
	donor_tree.column("Age", anchor = CENTER , width = 120)
	donor_tree.column("Sex", anchor = CENTER , width = 120)
	donor_tree.column("phno", anchor = CENTER , width = 120)
	donor_tree.column("email", anchor = CENTER , width = 120)
	donor_tree.column("bg", anchor = CENTER , width = 120)
	donor_tree.column("LDD", anchor = CENTER , width = 200)

	#headings
	donor_tree.heading("#0", text = "", anchor = CENTER)
	donor_tree.heading("DID", text = "Donor ID", anchor = CENTER)
	donor_tree.heading("DName", text = "Donor Name", anchor = CENTER)
	donor_tree.heading("Age", text = "Age", anchor = CENTER)
	donor_tree.heading("Sex", text = "Sex", anchor = CENTER)
	donor_tree.heading("phno", text = "Phone Number", anchor = CENTER)
	donor_tree.heading("email", text = "Email", anchor = CENTER)
	donor_tree.heading("bg", text = "Blood Group", anchor = CENTER)
	donor_tree.heading("LDD", text = "Last Donation Date", anchor = CENTER)

	donor_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, padx = 20, pady = (10,20))	

	#Frame for entry boxes(user input)
	donor_frame = Frame(donor_page)
	donor_frame.grid(row = 7, column = 0)

	l1 = Label(donor_frame, text = "Donor ID:").grid(row = 0, column = 0)
	donorId=StringVar()
	e1 = Entry(donor_frame,textvariable = donorId)
	e1.grid(row = 0, column = 1)
	l2 = Label(donor_frame, text = "Name:").grid(row = 0, column = 2)
	name=StringVar()
	e2 = Entry(donor_frame,textvariable = name)
	e2.grid(row = 0, column = 3)
	l3 = Label(donor_frame, text = "Age:").grid(row = 1, column = 0)
	age=StringVar()
	e3 = Entry(donor_frame,textvariable = age)
	e3.grid(row = 1, column = 1)
	l4 = Label(donor_frame, text = "Sex:").grid(row = 1, column = 2)
	sex=StringVar()
	e4 = Entry(donor_frame,textvariable = sex)
	e4.grid(row = 1, column = 3)
	l5 = Label(donor_frame, text = "Phone Number:").grid(row = 2, column = 0)
	phno=StringVar()
	e5 = Entry(donor_frame,textvariable = phno)
	e5.grid(row = 2, column = 1)
	l6 = Label(donor_frame, text = "Email ID:").grid(row = 2, column = 2)
	email=StringVar()
	e6 = Entry(donor_frame,textvariable = email)
	e6.grid(row = 2, column = 3)
	l7 = Label(donor_frame, text = "Blood Group:").grid(row = 3, column = 0)
	bg=StringVar()
	e7 = Entry(donor_frame,textvariable = bg)
	e7.grid(row = 3, column = 1)
	l8 = Label(donor_frame, text = "Last Donation Date:").grid(row = 3, column = 2)
	ldd=StringVar()
	e8 = Entry(donor_frame,textvariable = ldd)
	e8.grid(row = 3, column = 3)

	#Frame for operations buttons
	donor_bon = Frame(donor_page)
	donor_bon.grid(row = 8, column = 0)
	
	submit = Button(donor_bon, text = "Submit", command = subb)
	submit.grid(row = 0, column = 0, padx = 10, pady =10)

	view = Button(donor_bon, text = "View", command = view)
	view.grid(row = 0, column = 1, padx = 10, pady =10)

	search = Button(donor_bon, text = "Search", command = search)
	search.grid(row = 0, column = 2, padx = 10, pady = 10)

	update = Button(donor_bon, text = "Update", command = update)
	update.grid(row = 0, column = 3, padx = 10, pady =10)
	
	delete_button = Button(donor_bon, text = "Delete", command = delete)
	delete_button.grid(row = 0, column = 4, padx = 10, pady =10)

	donor_page.mainloop()	



# definition for Bloodbank button
def reg_BB():

	def subb(): # accepting data
		sub(e1.get(),e2.get(),e3.get(),e4.get())
			
	def sub(i,n,l,p):
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "insert into Bloodbank(CID,CName,Cloc,Cph) values('"+i+"','"+n+"','"+l+"','"+p+"')"
			
		c.execute(add)
		db.commit()
		db.close()

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)

	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Bloodbank"
							
		c.execute(add)

		row = c.fetchall()

		db.close()

		BB_tree.delete(*BB_tree.get_children())
		for rows in row:
			BB_tree.insert("",END,values =  rows)

	def search(): #SQL query for viewing single record
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Bloodbank WHERE CID = %s"
							
		c.execute(add,e1.get())

		row = c.fetchall()

		db.close()

		BB_tree.delete(*BB_tree.get_children())
		for rows in row:
			BB_tree.insert("",END,values =  rows)

	#Update records
	def update():

		upBB = Tk()
		upBB.title('Update Bloodbank Records')

		BG = Frame(upBB)
		BG.grid(row = 0, column = 0)

		ll1 = Label(BG, text = "Center ID:").grid(row = 0, column = 0)
		cid = StringVar()
		ee1 = Entry(BG, textvariable = cid)
		ee1.grid(row = 0, column = 1)
		ll2 = Label(BG, text = "Center Name:").grid(row = 0, column = 2)
		name = StringVar()
		ee2 = Entry(BG, textvariable = name)
		ee2.grid(row = 0, column = 3)
		ll3 = Label(BG, text = "Location:").grid(row = 0, column = 4)
		loc = StringVar()
		ee3 = Entry(BG, textvariable = loc)
		ee3.grid(row = 0, column = 5)
		ll4 = Label(BG, text = "Phone Number:").grid(row = 0, column = 6)
		ph = StringVar()
		ee4 = Entry(BG, textvariable = ph)
		ee4.grid(row = 0, column = 7)

		lbg1 = Label(BG, text = "A Positive:").grid(row = 1, column = 0, pady = (20,0))
		ap = StringVar()
		ebg1 = Entry(BG, textvariable = ap)
		ebg1.grid(row = 1, column = 1, pady = (20,0))
		lbg2 = Label(BG, text = "A Negative:").grid(row = 1, column = 2, pady = (20,0))
		an = StringVar()
		ebg2 = Entry(BG, textvariable = an)
		ebg2.grid(row = 1, column = 3, pady = (20,0))
		lbg3 = Label(BG, text = "B Positive:").grid(row = 2, column = 0)
		bp = StringVar()
		ebg3 = Entry(BG, textvariable = bp)
		ebg3.grid(row = 2, column = 1)
		lbg4 = Label(BG, text = "B Negative:").grid(row = 2, column = 2)
		bn = StringVar()
		ebg4 = Entry(BG, textvariable = bn)
		ebg4.grid(row = 2, column = 3)

		lbg5 = Label(BG, text = "AB Positive:").grid(row = 3, column = 0)
		abp = StringVar()
		ebg5 = Entry(BG, textvariable = abp)
		ebg5.grid(row = 3, column = 1)
		lbg6 = Label(BG, text = "AB Negative:").grid(row = 3, column = 2)
		abn = StringVar()
		ebg6 = Entry(BG, textvariable = abn)
		ebg6.grid(row = 3, column = 3)
		lbg7 = Label(BG, text = "O Positive:").grid(row = 4, column = 0)
		op = StringVar()
		ebg7 = Entry(BG, textvariable = op)
		ebg7.grid(row = 4, column = 1)
		lbg8 = Label(BG, text = "O Negative:").grid(row = 4, column = 2)
		on = StringVar()
		ebg8 = Entry(BG, textvariable = on)
		ebg8.grid(row = 4, column = 3)

		#save updated values
		def save():
			db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
			c = db.cursor()

			add = "UPDATE Bloodbank SET CName = %s, Cloc = %s, Cph = %s, A_pos = %s, A_neg = %s, B_pos = %s, B_neg = %s, AB_pos = %s, AB_neg = %s, O_pos = %s, O_neg = %s WHERE CID = %s"
			c.execute(add,(ee2.get(),ee3.get(),ee4.get(),ebg1.get(),ebg2.get(),ebg3.get(),ebg4.get(),ebg5.get(),ebg6.get(),ebg7.get(),ebg8.get(),ee1.get()))

			db.commit()
			db.close()

			e1.delete(0,END)
			upBB.destroy()

		save = Button(BG, text = "Save Record", command = save)
		save.grid(row = 5, column = 0, padx = 10, pady =10)

		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()

		add = "SELECT * FROM Bloodbank WHERE CID = %s"
		c.execute(add,(e1.get()))
		records = c.fetchall()

		for record in records:
			ee1.insert(0,record[0])
			ee2.insert(0,record[1])
			ee3.insert(0,record[2])
			ee4.insert(0,record[3])
			ebg1.insert(0,record[4])
			ebg2.insert(0,record[5])
			ebg3.insert(0,record[6])
			ebg4.insert(0,record[7])
			ebg5.insert(0,record[8])
			ebg6.insert(0,record[9])
			ebg7.insert(0,record[10])
			ebg8.insert(0,record[11])


		db.commit()
		db.close()

	#delete opertion	
	def delete():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "DELETE FROM Bloodbank WHERE CID = %s"
							
		c.execute(add,(e1.get()))

		db.commit()
		db.close()
		e1.delete(0,END)
		

	BB = Tk()
	BB.title("Blood Bank Details")

	#creating tree
	BB_tree = ttk.Treeview(BB)

	#define columns
	BB_tree['columns'] = ("CID","CName","Cloc","Cph","A_pos","A_neg","B_pos","B_neg","AB_pos","AB_neg","O_pos","O_neg")

	#format columns
	BB_tree.column("#0", width = 0, stretch = NO)
	BB_tree.column("CID", anchor = CENTER , width = 120)
	BB_tree.column("CName", anchor = CENTER , width = 120)
	BB_tree.column("Cloc", anchor = CENTER , width = 180)
	BB_tree.column("Cph", anchor = CENTER , width = 180)
	BB_tree.column("A_pos", anchor = CENTER , width = 80)
	BB_tree.column("A_neg", anchor = CENTER , width = 80)
	BB_tree.column("B_pos", anchor = CENTER , width = 80)
	BB_tree.column("B_neg", anchor = CENTER , width = 80)
	BB_tree.column("AB_pos", anchor = CENTER , width = 80)
	BB_tree.column("AB_neg", anchor = CENTER , width = 80)
	BB_tree.column("O_pos", anchor = CENTER , width = 80)
	BB_tree.column("O_neg", anchor = CENTER , width = 80)
		
	#headings
	BB_tree.heading("#0", text = "", anchor = CENTER)
	BB_tree.heading("CID", text = "Center ID", anchor = CENTER)
	BB_tree.heading("CName", text = "Center Name", anchor = CENTER)
	BB_tree.heading("Cloc", text = "Location", anchor = CENTER)
	BB_tree.heading("Cph", text = "Phone Number", anchor = CENTER)
	BB_tree.heading("A_pos", text = "A+", anchor = CENTER)
	BB_tree.heading("A_neg", text = "A-", anchor = CENTER)
	BB_tree.heading("B_pos", text = "B+", anchor = CENTER)
	BB_tree.heading("B_neg", text = "B-", anchor = CENTER)
	BB_tree.heading("AB_pos", text = "AB+", anchor = CENTER)
	BB_tree.heading("AB_neg", text = "AB-", anchor = CENTER)
	BB_tree.heading("O_pos", text = "O+", anchor = CENTER)
	BB_tree.heading("O_neg", text = "O-", anchor = CENTER)
	
	BB_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 4, padx = 20, pady = (10,20))
	
	#Frame for entry boxes
	BB_frame = Frame(BB)
	BB_frame.grid(row = 7, column = 0)

	l1 = Label(BB_frame, text = "Center ID:").grid(row = 1, column = 0)
	cid = StringVar()
	e1 = Entry(BB_frame, textvariable = cid)
	e1.grid(row = 1, column = 1)
	l2 = Label(BB_frame, text = "Center Name:").grid(row = 1, column = 2)
	name = StringVar()
	e2 = Entry(BB_frame, textvariable = name)
	e2.grid(row = 1, column = 3)
	l3 = Label(BB_frame, text = "Location:").grid(row = 2, column = 0)
	loc = StringVar()
	e3 = Entry(BB_frame, textvariable = loc)
	e3.grid(row = 2, column = 1)
	l4 = Label(BB_frame, text = "Phone Number:").grid(row = 2, column = 2)
	ph = StringVar()
	e4 = Entry(BB_frame, textvariable = ph)
	e4.grid(row = 2, column = 3)

	#Frame for Operation buttons
	BB_bon = Frame(BB)
	BB_bon.grid(row = 8, column = 0)

	submit = Button(BB_bon, text = "Submit", command = subb)
	submit.grid(row = 0, column = 0, padx = 10, pady =10)

	view = Button(BB_bon, text = "View", command = view)
	view.grid(row = 0, column = 1, padx = 10, pady =10)

	search = Button(BB_bon, text = "Search", command = search)
	search.grid(row = 0, column = 2, padx = 10, pady = 10)

	update = Button(BB_bon, text = "Update", command = update)
	update.grid(row = 0, column = 3, padx = 10, pady =10)	

	delete_button = Button(BB_bon, text = "Delete", command = delete)
	delete_button.grid(row = 0, column = 4, padx = 10, pady =10)

	BB.mainloop()


# definition for Hospital button
def Hos():

	def subb(): # accepting data
		sub(e1.get(),e2.get(),e3.get(),e4.get())
			
	def sub(i,n,l,p):
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "insert into Hospital values('"+i+"','"+n+"','"+l+"','"+p+"')"
			
		c.execute(add)
		db.commit()
		db.close()

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)

	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Hospital"
							
		c.execute(add)

		row = c.fetchall()

		db.close()

		H_tree.delete(*H_tree.get_children())
		for rows in row:
			H_tree.insert("",END,values =  rows)

	def search(): #SQL query for viewing single record
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Hospital WHERE HID = %s"
							
		c.execute(add,e1.get())

		row = c.fetchall()

		db.close()

		H_tree.delete(*H_tree.get_children())
		for rows in row:
			H_tree.insert("",END,values =  rows)

	#Update records
	def update():

		uphos = Tk()
		uphos.title('Update Hospital Records')

		hos = Frame(uphos)
		hos.grid(row = 0, column = 0)

		ll1 = Label(hos, text = "Hospital ID:").grid(row = 0, column = 0)
		hid = StringVar()
		ee1 = Entry(hos, textvariable = hid)
		ee1.grid(row = 0, column = 1)
		ll2 = Label(hos, text = "Hospital Name:").grid(row = 0, column = 2)
		name = StringVar()
		ee2 = Entry(hos, textvariable = name)
		ee2.grid(row = 0, column = 3)
		ll3 = Label(hos, text = "Location:").grid(row = 1, column = 0)
		loc = StringVar()
		ee3 = Entry(hos, textvariable = loc)
		ee3.grid(row = 1, column = 1)
		ll4 = Label(hos, text = "Phone Number:").grid(row = 1, column = 2)
		ph = StringVar()
		ee4 = Entry(hos, textvariable = ph)
		ee4.grid(row = 1, column = 3)


		#Save updated values
		def save():
			db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
			c = db.cursor()

			add = "UPDATE Hospital SET HName = %s, HLoc = %s, Hph = %s WHERE HID = %s"
			c.execute(add,(ee2.get(),ee3.get(),ee4.get(),ee1.get()))

			db.commit()
			db.close()

			e1.delete(0,END)
			uphos.destroy()

		save = Button(hos, text = "Save Record", command = save)
		save.grid(row = 5, column = 0, padx = 10, pady =10)

		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()

		add = "SELECT * FROM Hospital WHERE HID = %s"
		c.execute(add,(e1.get()))
		records = c.fetchall()

		for record in records:
			ee1.insert(0,record[0])
			ee2.insert(0,record[1])
			ee3.insert(0,record[2])
			ee4.insert(0,record[3])
						
		db.commit()
		db.close()

	#delete operation
	def delete():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "DELETE FROM Hospital WHERE HID = %s"
							
		c.execute(add,(e1.get()))

		db.commit()
		db.close()
		e1.delete(0,END)	

	H = Tk()
	H.title("Hospital Details")

	#creating tree
	H_tree = ttk.Treeview(H)

	#define columns
	H_tree['columns'] = ("HID","HName","Hloc","Hph")

	#format columns
	H_tree.column("#0", width = 0, stretch = NO)
	H_tree.column("HID", anchor = CENTER , width = 120)
	H_tree.column("HName", anchor = CENTER , width = 120)
	H_tree.column("Hloc", anchor = CENTER , width = 180)
	H_tree.column("Hph", anchor = CENTER , width = 180)
		
	#headings
	H_tree.heading("#0", text = "", anchor = CENTER)
	H_tree.heading("HID", text = "Hospital ID", anchor = CENTER)
	H_tree.heading("HName", text = "Hospital Name", anchor = CENTER)
	H_tree.heading("Hloc", text = "Location", anchor = CENTER)
	H_tree.heading("Hph", text = "Phone Number", anchor = CENTER)
		
	H_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, padx = 20, pady = (10,20))

	#Frame for entry boxes
	H_frame = Frame(H)
	H_frame.grid(row = 7, column = 0)

	l1 = Label(H_frame, text = "Hospital ID:").grid(row = 0, column = 0)
	hid = StringVar()
	e1 = Entry(H_frame, textvariable = hid)
	e1.grid(row = 0, column = 1)
	l2 = Label(H_frame, text = "Hospital Name:").grid(row = 0, column = 2)
	name = StringVar()
	e2 = Entry(H_frame, textvariable = name)
	e2.grid(row = 0, column = 3)
	l3 = Label(H_frame, text = "Location:").grid(row = 1, column = 0)
	loc = StringVar()
	e3 = Entry(H_frame, textvariable = loc)
	e3.grid(row = 1, column = 1)
	l4 = Label(H_frame, text = "Phone Number:").grid(row = 1, column = 2)
	ph = StringVar()
	e4 = Entry(H_frame, textvariable = ph)
	e4.grid(row = 1, column = 3)

	#Frame for operation buttons
	H_bon = Frame(H)
	H_bon.grid(row = 8, column = 0)
		
	submit = Button(H_bon, text = "Submit", command = subb)
	submit.grid(row = 0, column = 0, padx = 10, pady =10)

	view = Button(H_bon, text = "View", command = view)
	view.grid(row = 0, column = 1, padx = 10, pady =10)

	search = Button(H_bon, text = "Search", command = search)
	search.grid(row = 0, column = 2, padx = 10, pady = 10)

	update = Button(H_bon, text = "Update", command = update)
	update.grid(row = 0, column = 3, padx = 10, pady =10)

	delete_button = Button(H_bon, text = "Delete", command = delete)
	delete_button.grid(row = 0, column = 4, padx = 10, pady =10)

	H.mainloop()

###FRAME 2###
#---DEFINITIONS---#
# definition for log donation button
def con():

	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT DID,DName,bg,phno,LDD from Donor;"
							
		c.execute(add)

		row = c.fetchall()

		db.close()

		con_tree.delete(*con_tree.get_children())
		for rows in row:
			con_tree.insert("",END,values =  rows)

	def enter():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT DID,DName,bg,phno,LDD from Donor WHERE bg = %s"
							
		c.execute(add,e1.get())

		row = c.fetchall()

		db.close()

		con_tree.delete(*con_tree.get_children())
		for rows in row:
			con_tree.insert("",END,values =  rows)

		e1.delete(0,END)

	op = Tk()
	op.title("Donor Contact Info")

	#creating tree
	con_tree = ttk.Treeview(op)

	#define columns
	con_tree['columns'] = ("DID","DName","bg","phno","LDD")

	#format columns
	con_tree.column("#0", width = 0, stretch = NO)
	con_tree.column("DID", anchor = CENTER , width = 120)
	con_tree.column("DName", anchor = CENTER , width = 120)
	con_tree.column("bg", anchor = CENTER , width = 120)
	con_tree.column("phno", anchor = CENTER , width = 180)
	con_tree.column("LDD", anchor = CENTER , width = 180)
		
	#headings
	con_tree.heading("#0", text = "", anchor = CENTER)
	con_tree.heading("DID", text = "Donor ID", anchor = CENTER)
	con_tree.heading("DName", text = "Donor Name", anchor = CENTER)
	con_tree.heading("bg", text = "Blood Group", anchor = CENTER)
	con_tree.heading("phno", text = "Phone Number", anchor = CENTER)
	con_tree.heading("LDD", text = "Center ID", anchor = CENTER)
		
	con_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 3, padx = 20, pady = (10,20))

	view = Button(op, text = "View All", command = view)
	view.grid(row = 7, column = 0, padx = 10, pady = 10)

	l1 = Label(op, text = "Blood Group:").grid(row = 7, column = 1)
	bg=StringVar()
	e1 = Entry(op,textvariable = bg)
	e1.grid(row = 7, column = 2)

	enter_button = Button(op, text = "Enter", command = enter)
	enter_button.grid(row = 8, column = 1, padx = 10, pady =10)


###FRAME 3###
#---DEFINITIONS---#
# definition for log donation button
def donate():

	def subb(): # accepting data
		sub(e1.get(),e2.get(),e3.get(),e4.get(),e5.get())

	def sub(bid,bg,u,dd,did):
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "insert into Blood(BID,bg,units,DD,DID) values('"+bid+"','"+bg+"','"+u+"','"+dd+"','"+did+"')"
			
		c.execute(add)
		db.commit()
		db.close()

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)

	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Blood"
							
		c.execute(add)

		row = c.fetchall()

		db.close()

		don_tree.delete(*don_tree.get_children())
		for rows in row:
			don_tree.insert("",END,values =  rows)

	def search(): #SQL query for viewing single record
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Blood WHERE BID = %s"
							
		c.execute(add,e1.get())

		row = c.fetchall()

		db.close()

		don_tree.delete(*don_tree.get_children())
		for rows in row:
			don_tree.insert("",END,values =  rows)

	#Update records
	def update():

		upblood = Tk()
		upblood.title('Update Hospital Records')

		blood = Frame(upblood)
		blood.grid(row = 0, column = 0)

		ll1 = Label(blood, text = "Blood ID:").grid(row = 0, column = 0)
		bid=StringVar()
		ee1 = Entry(blood,textvariable = bid)
		ee1.grid(row = 0, column = 1)
		ll2 = Label(blood, text = "Blood Group:").grid(row = 0, column = 2)
		bg=StringVar()
		ee2 = Entry(blood,textvariable = bg)
		ee2.grid(row = 0, column = 3)
		ll3 = Label(blood, text = "Units:").grid(row = 1, column = 0)
		units=StringVar()
		ee3 = Entry(blood,textvariable = units)
		ee3.grid(row = 1, column = 1)
		ll4 = Label(blood, text = "Donation Date:").grid(row = 1, column = 2)
		dd=StringVar()
		ee4 = Entry(blood,textvariable = dd)
		ee4.grid(row = 1, column = 3)
		ll5 = Label(blood, text = "Donor ID:").grid(row = 2, column = 0)
		did=StringVar()
		ee5 = Entry(blood,textvariable = did)
		ee5.grid(row = 2, column = 1)


		#Save updated values
		def save():
			db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
			c = db.cursor()

			add = "UPDATE Blood SET bg = %s, units = %s, DD = %s, DID = %s WHERE BID = %s"
			c.execute(add,(ee2.get(),ee3.get(),ee4.get(),ee5.get(),ee1.get()))

			db.commit()
			db.close()

			e1.delete(0,END)
			upblood.destroy()

		save = Button(blood, text = "Save Record", command = save)
		save.grid(row = 5, column = 0, padx = 10, pady =10)

		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()

		add = "SELECT * FROM Blood WHERE BID = %s"
		c.execute(add,(e1.get()))
		records = c.fetchall()

		for record in records:
			ee1.insert(0,record[0])
			ee2.insert(0,record[1])
			ee3.insert(0,record[2])
			ee4.insert(0,record[3])
			ee5.insert(0,record[4])
						
		db.commit()
		db.close()

	#delete operation
	def delete():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "DELETE FROM Blood WHERE BID = %s"
							
		c.execute(add,(e1.get()))

		db.commit()
		db.close()
		e1.delete(0,END)

	donate = Tk()
	donate.title('Blood Donations')

	#creating tree
	don_tree = ttk.Treeview(donate)

	#define columns
	don_tree['columns'] = ("BID","bg","units","dd","DID")

	#format columns
	don_tree.column("#0", width = 0, stretch = NO)
	don_tree.column("BID", anchor = CENTER , width = 120)
	don_tree.column("bg", anchor = CENTER , width = 120)
	don_tree.column("units", anchor = CENTER , width = 180)
	don_tree.column("dd", anchor = CENTER , width = 180)
	don_tree.column("DID", anchor = CENTER , width = 120)
		
	#headings
	don_tree.heading("#0", text = "", anchor = CENTER)
	don_tree.heading("BID", text = "Blood ID", anchor = CENTER)
	don_tree.heading("bg", text = "Blood Group", anchor = CENTER)
	don_tree.heading("units", text = "Units", anchor = CENTER)
	don_tree.heading("dd", text = "Donation Date", anchor = CENTER)
	don_tree.heading("DID", text = "Donor ID", anchor = CENTER)
		
	don_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, padx = 20, pady = (10,20))

	#Frame for entry boxes
	don_frame = Frame(donate)
	don_frame.grid(row = 7, column = 0)

	l1 = Label(don_frame, text = "Blood ID:").grid(row = 0, column = 0)
	bid=StringVar()
	e1 = Entry(don_frame,textvariable = bid)
	e1.grid(row = 0, column = 1)
	l2 = Label(don_frame, text = "Blood Group:").grid(row = 0, column = 2)
	bg=StringVar()
	e2 = Entry(don_frame,textvariable = bg)
	e2.grid(row = 0, column = 3)
	l3 = Label(don_frame, text = "Units:").grid(row = 1, column = 0)
	units=StringVar()
	e3 = Entry(don_frame,textvariable = units)
	e3.grid(row = 1, column = 1)
	l4 = Label(don_frame, text = "Donation Date:").grid(row = 1, column = 2)
	dd=StringVar()
	e4 = Entry(don_frame,textvariable = dd)
	e4.grid(row = 1, column = 3)
	l5 = Label(don_frame, text = "Donor ID:").grid(row = 2, column = 0)
	did=StringVar()
	e5 = Entry(don_frame,textvariable = did)
	e5.grid(row = 2, column = 1)

	#Frame for operation buttons
	don_bon = Frame(donate)
	don_bon.grid(row = 8, column = 0)

	submit = Button(don_bon, text = "Submit", command = subb)
	submit.grid(row = 0, column = 0, padx = 10, pady = 10)

	view = Button(don_bon, text = "View", command = view)
	view.grid(row = 0, column = 1, padx = 10, pady = 10)

	search = Button(don_bon, text = "Search", command = search)
	search.grid(row = 0, column = 2, padx = 10, pady = 10)

	update = Button(don_bon, text = "Update", command = update)
	update.grid(row = 0, column = 3, padx = 10, pady = 10)

	delete_button = Button(don_bon, text = "Delete", command = delete)
	delete_button.grid(row = 0, column = 4, padx = 10, pady = 10)


	donate.mainloop()


# definition for log distribution button
def dist():

	def subb(): # accepting data
		sub(e1.get(),e2.get(),e3.get(),e4.get())

	def sub(cid,hid,bg,u):
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "insert into Log values('"+cid+"','"+hid+"','"+bg+"','"+u+"')"
			
		c.execute(add)
		db.commit()
		db.close()

		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		
	def view(): #SQL query for viewing all records of table Donor
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Log"
							
		c.execute(add)

		row = c.fetchall()

		db.close()

		log_tree.delete(*log_tree.get_children())
		for rows in row:
			log_tree.insert("",END,values =  rows) 

	def search(): #SQL query for viewing single record
				
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "SELECT * FROM Log WHERE CID = %s AND HID = %s"
							
		c.execute(add,(e1.get(),e2.get()))

		row = c.fetchall()

		db.close()

		log_tree.delete(*log_tree.get_children())
		for rows in row:
			log_tree.insert("",END,values =  rows)

	#Update records
	def update():

		uplog = Tk()
		uplog.title('Update Hospital Records')

		log = Frame(uplog)
		log.grid(row = 0, column = 0)

		ll1 = Label(log, text = "Center ID:").grid(row = 0, column = 0)
		cid=StringVar()
		ee1 = Entry(log,textvariable = cid)
		ee1.grid(row = 0, column = 1)
		ll2 = Label(log, text = "Hospital ID:").grid(row = 0, column = 2)
		hid=StringVar()
		ee2 = Entry(log,textvariable = hid)
		ee2.grid(row = 0, column = 3)
		ll3 = Label(log, text = "Blood Group:").grid(row = 1, column = 0)
		bg=StringVar()
		ee3 = Entry(log,textvariable = bg)
		ee3.grid(row = 1, column = 1)
		ll4 = Label(log, text = "Units:").grid(row = 1, column = 2)
		units=StringVar()
		ee4 = Entry(log,textvariable = units)
		ee4.grid(row = 1, column = 3)


		#Save updated values
		def save():
			db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
			c = db.cursor()

			add = "UPDATE Log SET bg = %s, units = %s WHERE CID = %s and HID = %s"
			c.execute(add,(ee3.get(),ee4.get(),ee1.get(),ee2.get()))

			db.commit()
			db.close()

			e1.delete(0,END)
			e2.delete(0,END)
			uplog.destroy()

		save = Button(log, text = "Save Record", command = save)
		save.grid(row = 5, column = 0, padx = 10, pady =10)

		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()

		add = "SELECT * FROM Log WHERE CID = %s and HID = %s"
		c.execute(add,(e1.get(),e2.get()))
		records = c.fetchall()

		for record in records:
			ee1.insert(0,record[0])
			ee2.insert(0,record[1])
			ee3.insert(0,record[2])
			ee4.insert(0,record[3])
									
		db.commit()
		db.close()

	#dalete operation
	def delete():
		db = pymysql.connect("localhost","root","1JB18EC027","BloodBank" )
		c = db.cursor()
		add = "DELETE FROM Log WHERE CID = %s and HID = %s"
							
		c.execute(add,(e1.get(),e2.get()))

		db.commit()
		db.close()
		e1.delete(0,END)
		e2.delete(0,END)

	dist = Tk()
	dist.title('Distribution')

	#creating tree
	log_tree = ttk.Treeview(dist)

	#define columns
	log_tree['columns'] = ("CID","HID","bg","units")

	#format columns
	log_tree.column("#0", width = 0, stretch = NO)
	log_tree.column("CID", anchor = CENTER , width = 120)
	log_tree.column("HID", anchor = CENTER , width = 120)
	log_tree.column("bg", anchor = CENTER , width = 120)
	log_tree.column("units", anchor = CENTER , width = 180)
		
		
	#headings
	log_tree.heading("#0", text = "", anchor = CENTER)
	log_tree.heading("CID", text = "Center ID", anchor = CENTER)
	log_tree.heading("HID", text = "Hospital ID", anchor = CENTER)
	log_tree.heading("bg", text = "Blood Group", anchor = CENTER)
	log_tree.heading("units", text = "Units", anchor = CENTER)

	log_tree.grid(row = 0, column = 0, rowspan = 6, columnspan = 2, padx = 20, pady = (10,20))

	#Frame for entry boxes
	log_frame = Frame(dist)
	log_frame.grid(row = 7, column = 0)

	l1 = Label(log_frame, text = "Center ID:").grid(row = 0, column = 0)
	cid=StringVar()
	e1 = Entry(log_frame,textvariable = cid)
	e1.grid(row = 0, column = 1)
	l2 = Label(log_frame, text = "Hospital ID:").grid(row = 0, column = 2)
	hid=StringVar()
	e2 = Entry(log_frame,textvariable = hid)
	e2.grid(row = 0, column = 3)
	l3 = Label(log_frame, text = "Blood Group:").grid(row = 1, column = 0)
	bg=StringVar()
	e3 = Entry(log_frame,textvariable = bg)
	e3.grid(row = 1, column = 1)
	l4 = Label(log_frame, text = "Units:").grid(row = 1, column = 2)
	units=StringVar()
	e4 = Entry(log_frame,textvariable = units)
	e4.grid(row = 1, column = 3)

	#Frame for operation buttons
	log_bon = Frame(dist)
	log_bon.grid(row = 8, column = 0)
	
	submit = Button(log_bon, text = "Submit", command = subb)
	submit.grid(row = 0, column = 0, padx = 10, pady = 10)

	view = Button(log_bon, text = "View", command = view)
	view.grid(row = 0, column = 1, padx = 10, pady = 10)

	search = Button(log_bon, text = "Search", command = search)
	search.grid(row = 0, column = 2, padx = 10, pady = 10)

	update = Button(log_bon, text = "Update", command = update)
	update.grid(row = 0, column = 3, padx = 10, pady = 10)

	delete_button = Button(log_bon, text = "Delete", command = delete)
	delete_button.grid(row = 0, column = 4, padx = 10, pady = 10)

	dist.mainloop()

