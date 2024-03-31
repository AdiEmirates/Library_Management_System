from tkinter import *
from tkinter import ttk
from tkinter import Scrollbar
import tkinter
import mysql.connector
from tkinter import messagebox
import datetime


class LibrartManagemnetSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x768+200+100")

        # variable
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysofbook_var = StringVar()
        self.laterreturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        lbltitle = Label(
            self.root,
            text="Library Management System",
            bd=20,
            relief=RIDGE,
            padx=2,
            font=("times new roman", 50, "bold"),
            fg="red",
        )
        lbltitle.pack(side=TOP, fill=X)

        # DataFrameleft
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1540, height=400)

        DataFrameleft = LabelFrame(
            frame,
            text="Library Membership Information",
            bd=12,
            relief=RIDGE,
            padx=2,
            font=("times new roman", 12, "bold"),
        )
        DataFrameleft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(
            DataFrameleft,
            text="Member Type:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(
            DataFrameleft,
            textvariable=self.member_var,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=27,
        )
        comMember["values"] = ("Admin", "Student", "Lectures")
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(
            DataFrameleft,
            text="PRN_NO:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(
            DataFrameleft,
            textvariable=self.prn_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(
            DataFrameleft,
            text="ID No.:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(
            DataFrameleft,
            textvariable=self.id_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtTitle.grid(row=2, column=1)

        lblFirstname = Label(
            DataFrameleft,
            text="First Name:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblFirstname.grid(row=3, column=0, sticky=W)
        txtFirstname = Entry(
            DataFrameleft,
            textvariable=self.firstname_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtFirstname.grid(row=3, column=1)

        lblLastName = Label(
            DataFrameleft,
            text="Last name:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(
            DataFrameleft,
            textvariable=self.lastname_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(
            DataFrameleft,
            text="Address 1:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(
            DataFrameleft,
            textvariable=self.address1_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(
            DataFrameleft,
            text="Address 2:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(
            DataFrameleft,
            textvariable=self.address2_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtAddress2.grid(row=6, column=1)

        lblContact = Label(
            DataFrameleft,
            text="Contact:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblContact.grid(row=7, column=0, sticky=W)
        txtContact = Entry(
            DataFrameleft,
            textvariable=self.mobile_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtContact.grid(row=7, column=1)

        lblPostcode = Label(
            DataFrameleft,
            text="Post code:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblPostcode.grid(row=8, column=0, sticky=W)
        txtPostcode = Entry(
            DataFrameleft,
            textvariable=self.postcode_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtPostcode.grid(row=8, column=1)

        lblBookID = Label(
            DataFrameleft,
            text="Book Id:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(
            DataFrameleft,
            textvariable=self.bookid_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(
            DataFrameleft,
            text="Book Title:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(
            DataFrameleft,
            textvariable=self.booktitle_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(
            DataFrameleft,
            text="Author Name:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(
            DataFrameleft,
            textvariable=self.author_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(
            DataFrameleft,
            text="Date Borrowed:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(
            DataFrameleft,
            textvariable=self.dateborrowed_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtDateBorrowed.grid(row=3, column=3, sticky=W)

        lblDateDue = Label(
            DataFrameleft,
            text="Date Due:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(
            DataFrameleft,
            textvariable=self.datedue_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtDateDue.grid(row=4, column=3, sticky=W)

        lblDateonBook = Label(
            DataFrameleft,
            text="Date on Book:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateonBook.grid(row=5, column=2, sticky=W)
        txtDateonBook = Entry(
            DataFrameleft,
            textvariable=self.daysofbook_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtDateonBook.grid(row=5, column=3, sticky=W)

        lblLateReturnFine = Label(
            DataFrameleft,
            text="Late Return Book:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(
            DataFrameleft,
            textvariable=self.laterreturnfine_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtLateReturnFine.grid(row=6, column=3, sticky=W)

        lblDateOverdate = Label(
            DataFrameleft,
            text="Date Over Due:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(
            DataFrameleft,
            textvariable=self.dateoverdue_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtDateOverdate.grid(row=7, column=3, sticky=W)

        lblActualPrice = Label(
            DataFrameleft,
            text="Actual Price:",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(
            DataFrameleft,
            textvariable=self.finalprice_var,
            font=("times new roman", 12, "bold"),
            width=29,
        )
        txtActualPrice.grid(row=8, column=3, sticky=W)

        # ==============================Button Frame Right Side =====================================#
        DataFrameright = LabelFrame(
            frame,
            text="Book Details",
            bd=12,
            relief=RIDGE,
            padx=2,
            font=("times new roman", 12, "bold"),
        )
        DataFrameright.place(x=910, y=5, width=570, height=350)

        self.txtbox = Text(
            DataFrameright,
            font=("times new roman", 12, "bold"),
            width=32,
            height=12,
            padx=2,
            pady=6,
        )
        self.txtbox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameright)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listbook = [
            "Head Firt Book",
            "Learn Python The Hard Way",
            "Python Programming",
            "Secrete Rahshy",
            "Python CookBook",
            "Into to Machine Learning",
            "Fluent Python",
            "Machine tecno",
            "My Python",
            "Joss Ellif guru",
            "Elite Jungle python",
            "Jungli Python",
            "Mumbai Python",
            "Pune Python ",
            "Python Crash Course",
            "Head First Python",
            "Learn Python the Hard Way",
            "Automate the Boring Stuff with Python",
            "Python for Data Analysis",
            "Flask Web Development",
            "Django for Beginners",
        ]

        def selectbook(event=""):
            value = str(listbox.get(listbox.curselection()))
            if value:
                x = value
                if x == "Head Firt Book":
                    self.bookid_var.set("BKID001")
                    self.booktitle_var.set("Head Firt Book")
                    self.author_var.set("Joss Ellif guru")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysofbook_var.set(15)
                    self.laterreturnfine_var.set("Rs.50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs.500")

                elif x == "Learn Python The Hard Way":
                    self.bookid_var.set("BKID001")
                    self.booktitle_var.set("Learn Python The Hard Way")
                    self.author_var.set("Joss Ellif guru")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysofbook_var.set(15)
                    self.laterreturnfine_var.set("Rs.50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs.500")

                elif x == "Python Programming":
                    self.bookid_var.set("BKID001")
                    self.booktitle_var.set("Python Programming")
                    self.author_var.set("Joss Ellif guru")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysofbook_var.set(15)
                    self.laterreturnfine_var.set("Rs.50")
                    self.dateoverdue_var.set("No")
                    self.finalprice_var.set("Rs.500")
            else:
                print("No selection made.")

        listbox = Listbox(
            DataFrameright, font=("times new roman", 12, "bold"), width=20, height=16
        )
        listbox.bind("<<ListboxSelect>>", selectbook)
        listbox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listbox.yview)

        for item in listbook:
            listbox.insert(END, item)

        # Button to add a new book in the library
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1540, height=70)

        btnAddData = Button(
            framebutton,
            command=self.adda_data,
            text="Add Data",
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(
            framebutton,
            text="Show Data",
            command=self.show_data,
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(
            framebutton,
            text="Update",
            command=self.update,
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(
            framebutton,
            text="Delete",
            command=self.delete,
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(
            framebutton,
            text="Reset",
            command=self.reset,
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(
            framebutton,
            text="Exit",
            command=self.exit,
            font=("times new roman", 13, "bold"),
            width=23,
            bg="green",
            fg="white",
        )
        btnAddData.grid(row=0, column=5)

        # information
        framedetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framedetails.place(x=0, y=600, width=1540, height=210)

        Table_Frame = Frame(framedetails, bd=6, relief=RIDGE, bg="white")
        Table_Frame.place(x=0, y=2, width=1465, height=170)

        xscroll = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(
            Table_Frame,
            columns=(
                "memebertype",
                "prnno",
                "title",
                "firtname",
                "lastname",
                "adress1",
                "adress2",
                "postid",
                "mobile",
                "bookid",
                "booktitle",
                "auther",
                "dateborrowed",
                "datedue",
                "days",
                "latereturnfine",
                "dateoverdue",
                "finalprice",
            ),
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set,
        )

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Address 1")
        self.library_table.heading("adress2", text="Address 2")
        self.library_table.heading("postid", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("memebertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=100)

        self.fatch_data()
        self.library_table.bind(
            "<ButtonRelease-1>", self.get_cursor
        )  # bind the table with the button

    def adda_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Test12345",
            database="sales",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        my_cursor.execute(
            "insert into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)",
            (
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.laterreturnfine_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysofbook_var.get(),
                self.finalprice_var.get(),
                self.dateoverdue_var.get(),
            ),
        )
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Book has been added successfully")

    def update(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Test12345",
            database="sales",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, BookId=%s, Author=%s, Dateborrowed=%s, DateDue=%s, Daysofbook=%s, laterreturnfine=%s, dateoverdue=%s, finalprice=%s where PRN NO='%s'",
            (
                self.member_var.get(),
                self.id_var.get(),
                self.laterreturnfine_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysofbook_var.get(),
                self.finalprice_var.get(),
                self.dateoverdue_var.get(),
                self.prn_var.get(),
            ),
        )
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated successfully")

    def fatch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Test12345",
            database="sales",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.laterreturnfine_var.set(row[3])
        self.firstname_var.set(row[4])
        self.lastname_var.set(row[5])
        self.address1_var.set(row[6])
        self.address2_var.set(row[7])
        self.postcode_var.set(row[8])
        self.mobile_var.set(row[9])
        self.bookid_var.set(row[10])
        self.booktitle_var.set(row[11])
        self.author_var.set(row[12])
        self.dateborrowed_var.set(row[13])
        self.datedue_var.set(row[14])
        self.daysofbook_var.set(row[15])
        self.laterreturnfine_var.set(row[16])
        self.finalprice_var.set(row[17])


    def show_data(self,event=""):
        self.txtbox.insert(END, "Member Type\t\t" + self.member_var.get() + "\n")
        self.txtbox.insert(END, "PRN No\t\t" + self.prn_var.get() + "\n")
        self.txtbox.insert(END, "Book Id\t\t" + self.id_var.get() + "\n")
        self.txtbox.insert(END, "Late Return Fine\t\t" + self.laterreturnfine_var.get() + "\n")
        self.txtbox.insert(END, "First Name\t\t" + self.firstname_var.get() + "\n")
        self.txtbox.insert(END, "Last Name\t\t" + self.lastname_var.get() + "\n")
        self.txtbox.insert(END, "Address 1\t\t" + self.address1_var.get() + "\n")
        self.txtbox.insert(END, "Address 2\t\t" + self.address2_var.get() + "\n")
        self.txtbox.insert(END, "Post Code\t\t" + self.postcode_var.get() + "\n")
        self.txtbox.insert(END, "Mobile\t\t" + self.mobile_var.get() + "\n")
        self.txtbox.insert(END, "Book Id\t\t" + self.bookid_var.get() + "\n")
        self.txtbox.insert(END, "Book Title\t\t" + self.booktitle_var.get() + "\n")
        self.txtbox.insert(END, "Author\t\t" + self.author_var.get() + "\n")
        self.txtbox.insert(END, "Date Borrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END, "Days of Book:\t\t" + self.daysofbook_var.get() + "\n")
        self.txtbox.insert(END, "Date Due\t\t" + self.datedue_var.get() + "\n")
        self.txtbox.insert(END, "Late Return Fine\t\t" + self.laterreturnfine_var.get() + "\n")
        self.txtbox.insert(END, "Final Price\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.laterreturnfine_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysofbook_var.set("")
        self.laterreturnfine_var.set("")
        self.finalprice_var.set("")
        self.txtbox.delete("1.0", END)

    def exit(self):
        exit = tkinter.messagebox.askyesno("Exit", "Do you want to quit?")
        if exit == True:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "First select the member")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Test12345",
                database="sales",
                auth_plugin="mysql_native_password",
            )
            my_cursor = conn.cursor()
            query = "delete from library where PRN NO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted successfully")


if __name__ == "__main__":
    root = Tk()
    obj = LibrartManagemnetSystem(root)
    root.mainloop()
