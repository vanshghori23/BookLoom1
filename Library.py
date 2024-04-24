from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter 
import datetime
from tkinter import Toplevel
from tkinter import Toplevel, Button, PhotoImage
import re
import tkinter as tk


listBoooks = [
    'To Kill a Mockingbird', '1984', 'Nowhere To Run', 'The Great Gatsby',
    'Pride and Prejudice', 'The Catcher in the Rye', 'Harry Potter and the Philosopher_s Stone',
    'The Lord of the Rings', 'The Hobbit', 'To the Lighthouse', 'The Da Vinci Code', 'Animal Farm',
    'The Diary of a Young Girl', 'The Alchemist', 'The Picture of Dorian Gray', 'Moby-Dick',
    'Frankenstein', 'Brave New World', 'One Hundred Years of Solitude', 'The Kite Runner'
]


class StartPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Library Management System")
        self.parent.attributes("-fullscreen", True)

        self.background_image = PhotoImage(file="C:\\Users\\ivans\\OneDrive\\Desktop\\assets\\Bookloom.png")
        self.canvas = Canvas(self.parent, width=1920, height=1080)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_image)

        btn_start = Button(self.canvas, text="Start", command=self.open_login_window, fg="white", bg="#3B2623",
                           font=("arial", 14), width=10)
        btn_start.place(relx=0.5, rely=0.694, anchor=CENTER)

    def open_login_window(self):
        self.parent.destroy()
        root = Tk()
        obj = LoginWindow(root)
        root.mainloop()


class LoginWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Login")
        self.parent.attributes("-fullscreen", True)

        self.users = {"admin": "1234", "admin2": "1"}  

        self.username_var = StringVar()
        self.password_var = StringVar()

        self.background_image = PhotoImage(file="C:\\Users\\ivans\\OneDrive\\Desktop\\assets\\1.png")
        self.canvas = Canvas(self.parent, width=1920, height=1080)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_image)

        lbl_username = Label(self.canvas, text="Username:", font=("arial", 14), bg="#3B2623", fg="white")
        lbl_username.place(relx=0.4, rely=0.54, anchor=CENTER)
        entry_username = Entry(self.canvas, textvariable=self.username_var, font=("arial", 14), bg="#3B2623", fg="white", highlightbackground="white", highlightcolor="white")
        entry_username.place(relx=0.585, rely=0.54, anchor=CENTER)

        lbl_password = Label(self.canvas, text="Password:", font=("arial", 14), bg="#3B2623", fg="white")
        lbl_password.place(relx=0.4, rely=0.66, anchor=CENTER)
        entry_password = Entry(self.canvas, textvariable=self.password_var, font=("arial", 14), show="*", bg="#3B2623", fg="white", highlightbackground="white", highlightcolor="white")
        entry_password.place(relx=0.585, rely=0.66, anchor=CENTER)

        btn_login = Button(self.canvas, text="Login", command=self.login,fg="white",bg="#3B2623", font=("arial", 14), width=10)
        btn_login.place(relx=0.437, rely=0.765, anchor=CENTER)

        btn_exit = Button(self.canvas, text="Exit", command=self.parent.destroy,fg="white",bg="#3B2623", font=("arial", 14), width=10)
        btn_exit.place(relx=0.564, rely=0.765, anchor=CENTER)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username in self.users and self.users[username] == password:
            self.open_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_main_window(self):
        self.parent.destroy()
        root = Tk()
        obj = LibraryManagementSystem(root)
        root.mainloop()


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.attributes("-fullscreen",True)


        #==================Variable==========
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.name_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.fine_var=StringVar()
        self.actualprice_var=StringVar()
        self.finalprice_var=StringVar()
        self.payment_var = StringVar()


        lbltitle=Label(self.root,text="BookLoom",bg="#3B2623",fg="white",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fil=X)
        
    
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#3B2623")
        frame.place(x=0,y=130,width=1920,height=450)


        #==========Dataframe==========
        DataFrameLeft=LabelFrame(frame,text="Membership",bg="#3B2623",fg="white",bd=12,relief=RIDGE,font=("times new roman",25,"bold"))
        DataFrameLeft.place(x=0,y=5,width=970,height=415)

        lblMember=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Member Type:",font=("arial",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",15,"bold"),width=25,state="readonly")
        comMember["value"]=("Student","Teacher")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="#3B2623",fg="white",text="PID No:",font=("arial",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblName=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Name:",font=("arial",15,"bold"),padx=2,pady=6)
        lblName.grid(row=2,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,textvariable=self.name_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtName.grid(row=2,column=1)

        lblAddress=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Address:",font=("arial",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=3,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtAddress.grid(row=3,column=1)

        lblPostCode=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Post Code:",font=("arial",15,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        lblMobile=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Mobile No:",font=("arial",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        lblBookId=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Book ID:",font=("arial",15,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Book Title:",font=("arial",15,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Auther Name:",font=("arial",15,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,textvariable=self.auther_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Date Borrowed:",font=("arial",15,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Due Date:",font=("arial",15,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblLateReturn=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Late Return Fine:",font=("arial",15,"bold"),padx=2,pady=6)
        lblLateReturn.grid(row=5,column=2,sticky=W)
        txtLateReturn=Entry(DataFrameLeft,textvariable=self.fine_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtLateReturn.grid(row=5,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Actual Price:",font=("arial",15,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=6,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtActualPrice.grid(row=6,column=3)

        lblPayment=Label(DataFrameLeft,bg="#3B2623",fg="white",text="Payment:",font=("arial",15,"bold"),padx=2,pady=6)
        lblPayment.grid(row=7,column=2,sticky=W)
        txtPayment=Entry(DataFrameLeft,textvariable=self.payment_var,bg="#9D9391",font=("times new roman",15,"bold"),width=29)
        txtPayment.grid(row=7,column=3)


        #============Dataframe======
        DataFrameRight=LabelFrame(frame,text="Book List",bg="#3B2623",fg="white",bd=12,relief=RIDGE,font=("times new roman",25,"bold"))
        DataFrameRight.place(x=1030,y=5,width=800,height=415)

        self.txtBox=Text(DataFrameRight,bg="#3B2623",fg="white",font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBoooks=['To Kill a Mockingbird', '1984', 'The Great Gatsby',
    'Pride and Prejudice', 'The Catcher in the Rye', 'Harry Potter and the Philosopher_s Stone',
    'The Lord of the Rings', 'The Hobbit', 'To the Lighthouse', 'The Da Vinci Code', 'Animal Farm',
    'The Diary of a Young Girl', 'The Alchemist', 'The Picture of Dorian Gray', 'Moby-Dick',
    'Frankenstein', 'Brave New World', 'One Hundred Years of Solitude', 'The Kite Runner']


        def SelectBook(event=""):
            if listBox.curselection(): 
                value = str(listBox.get(listBox.curselection()))
                x = value
            if (x=="To Kill a Mockingbird'"):
                self.bookid_var.set("BID1001")
                self.booktitle_var.set("Racism")
                self.auther_var.set("Harper Lee")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 70")
                self.finalprice_var.set("Rs 350")

            elif (x=="1984"):
                self.bookid_var.set("BID1002")
                self.booktitle_var.set("Totalitarianism")
                self.auther_var.set("George Orwell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 60")
                self.finalprice_var.set("Rs 250")

            elif (x=="The Great Gatsby"):
                self.bookid_var.set("BID1003")
                self.booktitle_var.set("Wealth")
                self.auther_var.set("Sova")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 90")
                self.finalprice_var.set("Rs 450")

            elif (x=="Pride and Prejudice"):
                self.bookid_var.set("BID1004")
                self.booktitle_var.set("Marriage")
                self.auther_var.set("Marriage")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 150")

            elif (x=="The Catcher in the Rye"):
                self.bookid_var.set("BID1005")
                self.booktitle_var.set("Adolescent")
                self.auther_var.set("Adolescent ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 80")
                self.finalprice_var.set("Rs 400")

            elif (x=="Harry Potter and the Philosopher's Stone"):
                self.bookid_var.set("BID1006")
                self.booktitle_var.set("Magic")
                self.auther_var.set("J.K. Rowling")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 60")
                self.finalprice_var.set("Rs 350")

            elif (x=="The Lord of the Rings"):
                self.bookid_var.set("BID1007")
                self.booktitle_var.set("Heroism")
                self.auther_var.set(" J.R.R. Tolkien")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 150")

            elif (x=="The Hobbit"):
                self.bookid_var.set("BID1008")
                self.booktitle_var.set("Adventure")
                self.auther_var.set("J.R.R. Tolkien")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 30")
                self.finalprice_var.set("Rs 250")

            elif (x=="The Da Vinci Code"):
                self.bookid_var.set("BID1009")
                self.booktitle_var.set("Religion")
                self.auther_var.set(" Dan Brown")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 55")
                self.finalprice_var.set("Rs 340")

            elif (x=="To the Lighthouse"):
                self.bookid_var.set("BID10010")
                self.booktitle_var.set("Subjectivity")
                self.auther_var.set("Virginia Woolf")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 30")
                self.finalprice_var.set("Rs 200")

            elif (x=="Animal Farm"):
                self.bookid_var.set("BID10011")
                self.booktitle_var.set("Corruption")
                self.auther_var.set("George Orwell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 180")

            elif (x=="The Diary of a Young Girl "):
                self.bookid_var.set("BID10012")
                self.booktitle_var.set("Holocaust")
                self.auther_var.set("Anne Frank")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 70")
                self.finalprice_var.set("Rs 300")

            elif (x=="The Alchemist"):
                self.bookid_var.set("BID10013")
                self.booktitle_var.set("Destiny")
                self.auther_var.set("Paulo Coelho")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 150")

            elif (x=="The Picture of Dorian Gray"):
                self.bookid_var.set("BID10014")
                self.booktitle_var.set("Hedonism")
                self.auther_var.set("Oscar Wilde")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 70")
                self.finalprice_var.set("Rs 240")

            elif (x=="Moby-Dick"):
                self.bookid_var.set("BID10015")
                self.booktitle_var.set("Obsession")
                self.auther_var.set("Herman Melville")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 50")
                self.finalprice_var.set("Rs 180")

            elif (x=="Frankenstein"):
                self.bookid_var.set("BID10016")
                self.booktitle_var.set("Science")
                self.auther_var.set("Mary Shelley")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 20")
                self.finalprice_var.set("Rs 100")

            elif (x=="Brave New World"):
                self.bookid_var.set("BID10017")
                self.booktitle_var.set("Dystopia")
                self.auther_var.set("Aldous Huxley")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 70")
                self.finalprice_var.set("Rs 200")

            elif (x=="One Hundred Years of Solitude"):
                self.bookid_var.set("BID10018")
                self.booktitle_var.set("Family")
                self.auther_var.set(" Gabriel García Márquez")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 170")

            elif (x=="The Kite Runner"):
                self.bookid_var.set("BID10019")
                self.booktitle_var.set("Friendship")
                self.auther_var.set("Khaled Hosseini")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=7)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.fine_var.set("Rs 40")
                self.finalprice_var.set("Rs 150")
            

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=32,height=17)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column=0,padx=6)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)


        # =====Buttons=======
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#3B2623")
        Framebutton.place(x=0,y=580,width=1920,height=57)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=14,bg="black",fg="white")
        btnAddData.grid(row=1,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=21,bg="black",fg="white")
        btnAddData.grid(row=1,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="black",fg="white")
        btnAddData.grid(row=1,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="black",fg="white")
        btnAddData.grid(row=1,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="black",fg="white")
        btnAddData.grid(row=1,column=4)
        
        btnBookBank = Button(Framebutton, command=self.book_bank, text="Book Bank", font=("arial", 12, "bold"), width=23, bg="black", fg="white")
        btnBookBank.grid(row=1, column=5)

        btnValidatePayment=Button(Framebutton,command=self.validate_payment,text="Pay",font=("arial",12,"bold"),width=15,bg="black",fg="white")
        btnValidatePayment.grid(row=1,column=6)

        btnOnlinePay = Button(Framebutton, command=self.online_payment, text="Online Pay", font=("arial", 12, "bold"), width=17, bg="black", fg="white")
        btnOnlinePay.grid(row=1, column=7)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=18,bg="black",fg="white")
        btnAddData.grid(row=1,column=8)


        # =====Infos=======
        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#3B2623")
        Framedetails.place(x=0,y=637,width=1920,height=445)

        Table_frame=Frame(Framedetails,bd=6,relief=RIDGE,bg="#3B2623")
        Table_frame.place(x=0,y=2,width=1860,height=417)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)   

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","name","address","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","fine","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PID No")
        self.library_table.heading("name",text="Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile No")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrow")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("fine",text="Return Fine")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("name",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("fine",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def book_bank(self):
        book_bank_window = Toplevel(self.root)
        book_bank_window.title("Book Bank")
        txt_books = Text(book_bank_window, font=("arial", 12))
        txt_books.pack(fill=BOTH, expand=True)
        txt_books.insert(END, "List of Books:\n")
        for book in listBoooks:
            txt_books.insert(END, f"- {book}\n")
        txt_books.config(state=DISABLED)


    def validate_mobile(self, mobile_number):
        pattern = r"^\d{10}$"
        if re.match(pattern, mobile_number):
            return True
        else:
            return False
        

    def validate_pid(self, pid_number):
        pattern = r"^\d{6}$"
        if re.match(pattern, pid_number):
            return True
        else:
            return False
        

    def validate_name(self, name):
        pattern = r"^[a-zA-Z\s]+$"
        if re.match(pattern, name):
            return True
        else:
            return False


    def add_data(self):
        if (self.validate_mobile(self.mobile_var.get()) and
            self.validate_pid(self.prn_var.get()) and
            self.validate_name(self.name_var.get())):
            conn=mysql.connector.connect(host="localhost",username="root",password="@Vansh2004",database="librarymanagementsystem")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.name_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.auther_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.fine_var.get(),
                                                                                                            self.finalprice_var.get()
        ))
        else:
            error_message = "Please fix the following issues:\n"
            if not self.validate_mobile(self.mobile_var.get()):
                error_message += "- Invalid mobile number (must be 10 digits)\n"
            if not self.validate_pid(self.prn_var.get()):
                error_message += "- Invalid PID number (must be 4 digits)\n"
            if not self.validate_name(self.name_var.get()):
                error_message += "- Invalid Name (only alphabets and spaces allowed)\n"
            messagebox.showerror("Validation Error", error_message)


        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success", "Member has been inserted")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Vansh2004",database="librarymanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set membertype=%s,prnno=%s,name=%s,address=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,fine=%s,finalprice=%s WHERE prnno=%s",(
                                                                                                        self.member_var.get(),
                                                                                                        self.prn_var.get(),
                                                                                                        self.name_var.get(),
                                                                                                        self.address_var.get(),
                                                                                                        self.postcode_var.get(),
                                                                                                        self.mobile_var.get(),
                                                                                                        self.bookid_var.get(),
                                                                                                        self.booktitle_var.get(),
                                                                                                        self.auther_var.get(),
                                                                                                        self.dateborrowed_var.get(),
                                                                                                        self.datedue_var.get(),
                                                                                                        self.fine_var.get(),
                                                                                                        self.finalprice_var.get(),
                                                                                                        self.prn_var.get()
    ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success", "Member has been Updated")

        
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Vansh2004",database="librarymanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
            conn.close()


    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        values = self.library_table.item(cursor_row, 'values')
        if values:
            self.member_var.set(values[0])
            self.prn_var.set(values[1])
            self.name_var.set(values[2])
            self.address_var.set(values[3])
            self.postcode_var.set(values[4])
            self.mobile_var.set(values[5])
            self.bookid_var.set(values[6])
            self.booktitle_var.set(values[7])
            self.auther_var.set(values[8])
            self.dateborrowed_var.set(values[9])
            self.datedue_var.set(values[10])
            self.fine_var.set(values[11])
            self.finalprice_var.set(values[12])


    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "PIN No: \t\t"+ self.prn_var.get() + "\n")
        self.txtBox. insert (END, "FirstName: \t\t"+ self.name_var.get () +"\n")
        self.txtBox. insert (END,"Address1: \t\t"+ self.address_var.get() + "\n")
        self.txtBox. insert (END, "Post Code: \t\t"+ self.postcode_var.get() + "\n")
        self.txtBox. insert (END, "Mobile No: \t\t"+ self.mobile_var.get () +"\n")
        self.txtBox.insert (END, "Book ID: \t\t"+ self.bookid_var.get() + "\n")
        self.txtBox. insert (END, "Book Title:\t\t"+ self.booktitle_var.get () + "\n")
        self.txtBox. insert (END, "Auther: \t\t"+ self.auther_var.get () + "\n")
        self.txtBox.insert (END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert (END, "DateDue: \t\t"+ self.datedue_var.get() + "\n")
        self.txtBox. insert(END, "LateRateFine: \t\t"+ self.fine_var.get() + "\n")
        self.txtBox. insert(END, "FinalIPrice: \t\t"+ self.finalprice_var.get()+"\n")
        self.txtBox. insert(END, "Payment: \t\t"+ self.payment_var.get()+"\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.name_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.fine_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("BookLoom","Do You Really Want To Exit !!!!")
        if iExit>0:
            self.root.destroy()
            return
        

    def delete (self):
        if self.prn_var.get()=="":
            messagebox.showerror("Error","First Select Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Vansh2004",database="librarymanagementsystem")
            my_cursor=conn.cursor()
            query="delete from library where prnno=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")


    def validate_payment(self):
        final_price_str = self.finalprice_var.get()
        payment_str = self.payment_var.get()

        if "Rs " in final_price_str:
            try:
                if payment_str and "Rs " in payment_str:
                    entered_payment = float(payment_str.split("Rs ")[1])
                    conn = mysql.connector.connect(host="localhost", username="root", password="@Vansh2004", database="librarymanagementsystem")
                    cursor = conn.cursor()
        
                    cursor.execute("UPDATE library SET finalprice = %s WHERE prnno = %s", (f"Rs {entered_payment}", self.prn_var.get()))
                    cursor.execute("INSERT INTO payment_details (prnno, payment_amount, payment_date) VALUES (%s, %s, %s)", (self.prn_var.get(), entered_payment, datetime.datetime.now()))
                    conn.commit()
                    conn.close()
        
                    messagebox.showinfo("Payment Successful", f"Payment of Rs {entered_payment} accepted.")
                else:
                    messagebox.showerror("Error", "Payment field cannot be empty. Please enter a valid payment amount.")
            except ValueError:
                messagebox.showerror("Error", "Invalid payment amount. Please enter a valid number.")
        else:
            messagebox.showerror("Error", "Actual price format is incorrect. Please check.")


    def process_payment(self, payment_amount):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="@Vansh2004", database="librarymanagementsystem")
            cursor = conn.cursor()

            cursor.execute("UPDATE library SET finalprice = %s WHERE prnno = %s", (f"Rs {payment_amount}", self.prn_var.get()))
            conn.commit()
            conn.close()

            self.fatch_data()

            messagebox.showinfo("Payment Successful", f"Payment of Rs {payment_amount} accepted.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occurred while processing payment: {e}")


    def online_payment(self):
        payment_window = Toplevel(self.root)
        payment_window.title("Online Payment")
        payment_window.attributes("-fullscreen", True)

        def exit_payment_window():
            payment_window.destroy()

        payment_image = PhotoImage(file="C:\\Users\\ivans\\OneDrive\\Desktop\\assets\\2.png")

        lbl_payment_image = Label(payment_window, image=payment_image)
        lbl_payment_image.place(relx=0.5, rely=0.5, anchor="center")

        lbl_payment_image.image = payment_image

        btn_exit = Button(payment_window, text="Exit", command=exit_payment_window, font=("arial", 12, "bold"), width=10)
        btn_exit.place(relx=0.9, rely=0.05, anchor="ne")

        btn_exit.lift()


if __name__ == "__main__":
    root = Tk()
    obj = StartPage(root)
    root.mainloop()