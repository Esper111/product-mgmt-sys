from tkinter import *
import mysql.connector
from tkinter import messagebox
import operation as o

class loginto:
    def __init__(self, root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("380x380+0+0")
        self.user=StringVar()
        self.pwd=StringVar()
        self.ul=['veek','swati','ari']
        self.pl=['123','01234','1234']
        lg=LabelFrame(self.root,text="Login",font=("Times New Roman",15,"bold"))
        lg.place(x=60,y=80,width=250,height=280)
        u_l=Label(lg,text="Admin user name:",font=("Times New Roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        u_e=Entry(lg,textvariable=self.user,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=0,padx=5,pady=10)
        p_l=Label(lg,text="Admin password:",font=("Times New Roman",18,"bold")).grid(row=2,column=0,padx=20,pady=5)
        p_e=Entry(lg,width=15,textvariable=self.pwd,font="arial 15",bd=7,relief=SUNKEN,show='*').grid(row=3,column=0,padx=5,pady=10)
        log=Button(lg,text="Login",width=5,bd=7,font="arial 12 bold",command=self.verify).grid(row=4,column=0,padx=10)

    def verify(self):
        for i in range(len(self.ul)):
            if(self.user.get()==self.ul[i] and self.pwd.get()==self.pl[i]):
                messagebox.showinfo("Success!")
                ob=MgmtSys(root)
                root.mainloop()
                return
        messagebox.showinfo("You forgot your name or password....")
        exit(0)


class MgmtSys:
    def __init__(self, root):
        self.res=0
        self.root=root
        self.root.title("Product Management System")
        self.root.geometry("1550x800+0+0")
        bg_color="#074463"
        title=Label(self.root,text="Product Management System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)
        self.aname=StringVar()
        self.pname_e=StringVar()
        self.pno_e=StringVar()
        self.q_e=StringVar()
        self.price_e=StringVar()
        self.dis_e=StringVar()
        self.bar_e=StringVar()
        self.rname_e=StringVar()
        self.rno_e=StringVar()
        self.rq_e=StringVar()
        self.rbar_e=StringVar()
        self.rdis_e=StringVar()
        self.pname_e1=StringVar()
        self.pno_e1=StringVar()
        self.q_e1=StringVar()
        self.price_e1=StringVar()
        self.dis_e1=StringVar()
        self.bar_e1=StringVar()
        self.total_e=StringVar()
        self.tax_e=StringVar()
        self.gdis_e=StringVar()
        self.gtot_e=StringVar()


        l1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Admin Details",font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        l1.place(x=0,y=80,relwidth=1)
        aname_l=Label(l1,text="Admin name",bg=bg_color,fg="white",font=("Times New Roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        aname_e=Entry(l1,textvariable=self.aname,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        aid_l=Label(l1,text="Admin id",bg=bg_color,fg="white",font=("Times New Roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        aid_e=Entry(l1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
        # search=Button(l1,text="search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        l2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Shipped Product Details",font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        l2.place(x=5,y=170,width=330,height=420)
        pname_l=Label(l2,text="Product name",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        pname_e=Entry(l2,textvariable=self.pname_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        pno_l=Label(l2,text="Product id",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        pno_e=Entry(l2,textvariable=self.pno_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        q_l=Label(l2,text="Quantity",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        q_e=Entry(l2,textvariable=self.q_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        price_l=Label(l2,text="Price",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        price_e=Entry(l2,textvariable=self.price_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        dis_l=Label(l2,text="Discount %",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        dis_e=Entry(l2,textvariable=self.dis_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        bar_l=Label(l2,text="Barcode",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        bar_e=Entry(l2,textvariable=self.bar_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        enter=Button(l2,text="enter",width=5,bd=7,font="arial 12 bold", command=self.fun).grid(row=6,column=0)

        # 
        l3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Remove/update Product",font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        l3.place(x=340,y=170,width=325,height=420)
        rname_l=Label(l3,text="Product name",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rname_e=Entry(l3,textvariable=self.rname_e,width=10,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        rno_l=Label(l3,text="Product id",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        rno_e=Entry(l3,textvariable=self.rno_e,width=10,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        rq_l=Label(l3,text="Quantity",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        rq_e=Entry(l3,textvariable=self.rq_e,width=10,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        # price_l=Label(l2,text="Price",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        # price_e=Entry(l2,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        rdis_l=Label(l3,text="Discount",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        rdis_e=Entry(l3,textvariable=self.rdis_e,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        rbar_l=Label(l3,text="Barcode",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        rbar_e=Entry(l3,textvariable=self.rbar_e,width=10,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        enterr=Button(l3,text="enter",width=5,bd=7,font="arial 12 bold",command=self.fetch).grid(row=6,column=0,padx=10,pady=50)

        # 
        l4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Checkout Products",font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        l4.place(x=670,y=170,width=325,height=420)
        pname_l1=Label(l4,text="Product name",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        pname_e1=Entry(l4,textvariable=self.pname_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        pno_l1=Label(l4,text="Product id",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        pno_e1=Entry(l4,textvariable=self.pno_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        q_l1=Label(l4,text="Quantity",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        q_e1=Entry(l4,textvariable=self.q_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        price_l1=Label(l4,text="Price",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        price_e1=Entry(l4,textvariable=self.price_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        dis_l1=Label(l4,text="Discount",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        dis_e1=Entry(l4,textvariable=self.dis_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        bar_l1=Label(l4,text="Barcode",bg=bg_color,fg="white",font=("Times New Roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        bar_e1=Entry(l4,textvariable=self.bar_e1,width=9,font="arial 15 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        enter1=Button(l4,text="enter",width=5,bd=7,font="arial 12 bold",command=self.bill).grid(row=6,column=0)
        
        # 
        l5=Frame(self.root,bd=10,relief=GROOVE)
        l5.place(x=1010,y=170,width=350,height=380)
        b_title=Label(l5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        sc_y=Scrollbar(l5,orient=VERTICAL)
        self.txtarea=Text(l5,yscrollcommand=sc_y.set)
        sc_y.pack(side=RIGHT,fill=Y)
        sc_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # 
        l6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Checkout Products",font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        l6.place(x=0,y=600,relwidth=1,height=140)
        total=Label(l6,text="Total",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        total_e=Entry(l6,textvariable=self.total_e,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        tax=Label(l6,text="Tax",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        tax_e=Entry(l6,textvariable=self.tax_e,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        gdis=Label(l6,text="Discount",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        gdis_e=Entry(l6,textvariable=self.gdis_e,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        gtot=Label(l6,text="Grand Total",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        gtot_e=Entry(l6,textvariable=self.gtot_e,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        l7=Frame(l6,bd=7,relief=GROOVE)
        l7.place(x=750,width=580,height=100)
        tb=Button(l7,text="Total",bg="purple",bd=5,fg="white",pady=10,width=9,font="arial 15 bold",command=self.total1).grid(row=0,column=0,padx=5,pady=5)
        bill=Button(l7,text="Bill",bg="purple",bd=5,fg="white",pady=10,width=9,font="arial 15 bold",command=self.billamt).grid(row=0,column=1,padx=5,pady=5)
        clear=Button(l7,text="Clear",bg="purple",bd=5,fg="white",pady=10,width=9,font="arial 15 bold",command=self.clear1).grid(row=0,column=2,padx=5,pady=5)
        # exit=Button(l7,text="Logout",bg="purple",bd=5,fg="white",pady=10,width=9,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        # use total to calculate everything, in operation, use tat fr addition or tax calc
        # use the bill to do file write for bill and put same thing in display
        # use clear to make everything null

        # -----create table product(pname varchar(20), pid int primary key, quantity int, price decimal(10,2),dis int, barcode int);
    def fun(self):
            if self.aname.get()=="":
                messagebox.showerror("All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="sql123", database="prod")
                if(conn.is_connected()):
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(self.pname_e.get(),self.pno_e.get(),self.q_e.get(),self.price_e.get(),self.dis_e.get(),self.bar_e.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Product inserted")
                else:
                     messagebox.showinfo("error")
                    
    def fetch(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="sql123", database="prod")
         my_cursor=conn.cursor()
         my_cursor.execute("select pid from product where pname=%s",(self.rname_e.get(),))
         result_pid = my_cursor.fetchone()
         if result_pid:
            self.rno_e.set(result_pid[0]) 
         my_cursor.execute("select barcode from product where pname=%s",(self.rname_e.get(),))
         result_barcode = my_cursor.fetchone()
         if result_barcode:
            self.rbar_e.set(result_barcode[0]) 
         my_cursor.execute("select dis from product where pname=%s",(self.rname_e.get(),))
         result_d = my_cursor.fetchone()
         if result_d:
            self.rdis_e.set(result_d[0])
         my_cursor.execute("update product set quantity=%s where pname=%s",(self.rq_e.get(),self.rname_e.get()))
         conn.commit()
         conn.close()

    def bill(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sql123", database="prod")
        my_cursor=conn.cursor()
        my_cursor.execute("select pid from product where pname=%s",(self.pname_e1.get(),))
        result_pid = my_cursor.fetchone()
        if result_pid:
            self.pno_e1.set(result_pid[0]) 
        my_cursor.execute("select barcode from product where pname=%s",(self.pname_e1.get(),))
        result_barcode = my_cursor.fetchone()
        if result_barcode:
            self.bar_e1.set(result_barcode[0]) 
        my_cursor.execute("select price from product where pname=%s",(self.pname_e1.get(),))
        result_price = my_cursor.fetchone()
        if result_price:
            self.price_e1.set(result_price[0])
        my_cursor.execute("select dis from product where pname=%s",(self.pname_e1.get(),))
        result_d = my_cursor.fetchone()
        if result_d:
            res=o.disc(result_price[0],result_d[0])
            self.dis_e1.set(res) 
        my_cursor.execute("select quantity from product where pname=%s",(self.pname_e1.get(),))
        result_q = my_cursor.fetchone()
        q1=0
        if result_q:
            q1=result_q[0]-int(self.q_e1.get())
            print(q1)
        my_cursor.execute("update product set quantity=%s where pname=%s",(q1,self.pname_e1.get()))
        conn.commit()
        conn.close()
    
    def total1(self):
        t=o.tot(self.q_e1.get(),self.total_e.get(),self.price_e1.get())
        self.total_e.set(t)
        d=o.disc1(self.q_e1.get(),self.price_e1.get(),self.dis_e1.get())
        self.gdis_e.set(d)
        f=open("D:\\study\\nmit\\ccp\\p5.txt","a")
        f.write(self.pname_e1.get()+" "+self.price_e1.get()+" "+self.q_e1.get()+"\n")
        f.close()
    
    def clear1(self):
        self.aname.set(" ")
        self.pname_e.set(" ")
        self.pno_e.set(" ")
        self.q_e.set(" ")
        self.price_e.set(" ")
        self.dis_e.set(" ")
        self.bar_e.set(" ")
        self.rname_e.set(" ")
        self.rno_e.set(" ")
        self.rq_e.set(" ")
        self.rbar_e.set(" ")
        self.rdis_e.set(" ")
        self.pname_e1.set(" ")
        self.pno_e1.set(" ")
        self.q_e1.set(" ")
        self.price_e1.set(" ")
        self.dis_e1.set(" ")
        self.bar_e1.set(" ")
        self.total_e.set(" ")
        self.tax_e.set(" ")
        self.gdis_e.set(" ")
        self.gtot_e.set(" ")
        self.txtarea.insert(END,"")
        f=open("D:\\study\\nmit\\ccp\\p5.txt","w")
        f.write("")
        f.close()

    def billamt(self):
        t=o.tx(self.total_e.get())
        self.tax_e.set(t)
        d=o.amt(self.total_e.get(),self.gdis_e.get())
        self.gtot_e.set(d)
        f=open("D:\\study\\nmit\\ccp\\p5.txt","a")
        f.write("tax: "+str(t)+"\ndiscount: "+self.gdis_e.get()+"\nGrand Total: "+str(d)+"\n")
        f.close()
        f=open("D:\\study\\nmit\\ccp\\p5.txt","r")
        self.txtarea.insert(END,f.read())
        f.close()
        
        
if __name__== "__main__":
    root=Tk()
    ob=loginto(root)
    root.mainloop()