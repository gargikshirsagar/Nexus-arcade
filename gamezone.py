from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import MySQLdb

Window=Tk()
Window.geometry('1350x700+0+0')
Window.title("Gamezone management system")

title=Label(Window,text='GameZone Management System',font=('arial',23,'bold'),border=10,relief=GROOVE,bg='#9e8de3')
title.pack(side=TOP,fill=BOTH)

frame1=LabelFrame(Window,text='Enter Details',font=('arial',14),border=8,bg='#9e8de3')
frame1.place(x=20,y=90,width=420,height=570)

frame2=LabelFrame(Window,font=('arial',14),border=8,bg='#9e8de3',relief=GROOVE)
frame2.place(x=470,y=90,width=810,height=570)


# Logic
def fetch_data():
    conn = MySQLdb.connect(host="localhost", user="root", password="root", database="gamezone")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', END, values=row)
        conn.commit()
        conn.close()

def add_func():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_value = Id.get()
    name_value = Name.get()
    contact_value = Contact.get()
    email_value = Email.get()
    console_id_value = ConsoleId.get()
    console_value = Console.get()
    payment_value = Payment.get()
    if id_value=="":
        messagebox.showerror("Error!", "Please fill all the fields!")
    else:
        conn = MySQLdb.connect(host="localhost", user="root", password="root", database="gamezone")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (id_value, name_value,current_time, contact_value, email_value, console_id_value, console_value, payment_value))
        conn.commit()
        conn.close()

        fetch_data()

def get_cursor(event):
    cursor_row=table.focus()
    content=table.item(cursor_row)
    row=content['values']
    Id.set(row[0])  
    Name.set(row[1])
    Contact.set(row[3])
    Email.set(row[4])
    ConsoleId.set(row[5])
    Console.set(row[6])
    Payment.set(row[7])
            
def clear():
    Id.set("")
    Name.set("")
    Contact.set("")
    Email.set("")
    ConsoleId.set("")
    Console.set("")
    Payment.set("")

def update_func():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_value = Id.get()
    name_value = Name.get()
    contact_value = Contact.get()
    email_value = Email.get()
    console_id_value = ConsoleId.get()
    console_value = Console.get()
    payment_value = Payment.get()
    conn = MySQLdb.connect(host="localhost", user="root", password="root", database="gamezone")
    curr = conn.cursor()
    curr.execute("UPDATE data SET name_value=%s, contact_value=%s, email_value=%s, console_id_value=%s, console_value=%s, payment_value=%s  WHERE id_value=%s",
                    (name_value, contact_value, email_value, console_id_value, console_value, payment_value,id_value))
    conn.commit()
    conn.close()

    fetch_data()

def delete_func():
    id_value = Id.get()
    #console_id_value = ConsoleId.get()
    conn = MySQLdb.connect(host="localhost", user="root", password="root", database="gamezone")
    curr = conn.cursor()
    curr.execute("DELETE FROM data WHERE id_value=%s", (id_value))
    conn.commit()
    conn.close()

    fetch_data()

def perform_database_search():
    search_by_value = search_by.get()  # Retrieve the search term from the StringVar
    conn = MySQLdb.connect(host="localhost", user="root", password="root", database="gamezone")
    curr = conn.cursor()
    query = "SELECT * FROM data WHERE "
    columns = ["id_value", "name_value", "contact_value", "email_value", "console_id_value", "console_value", "payment_value"]
    conditions = ["{} LIKE %s".format(column) for column in columns]
    full_query = query + " OR ".join(conditions)
    # Execute the query with the search term
    curr.execute(full_query, tuple(["%" + search_by_value + "%"] * len(columns)))
    results = curr.fetchall()  # Fetch all matching rows
    for row in table.get_children():
        table.delete(row)
            
    # Insert the retrieved rows into the Treeview
    for row in results:
        table.insert('', 'end', values=row)
    curr.close()
    conn.close()





#####----------------------------------------
#----Variables-----#
Id=StringVar()
Name=StringVar()
Contact=StringVar()
Email=StringVar()
ConsoleId=StringVar()
Console=StringVar()
Payment=StringVar()

search_by=StringVar()

 #-------------------#

userId=Label(frame1,text='ID',bg='#9e8de3',font=('arial',14))
userId.grid(row=0,column=0,padx=2,pady=12)

userId_ent=Entry(frame1,width=31,border=5,font=('arial',10),textvariable=Id)
userId_ent.grid(row=0,column=1,padx=2,pady=12)


username=Label(frame1,text='Name',bg='#9e8de3',font=('arial',14))
username.grid(row=1,column=0,padx=2,pady=12)

username_ent=Entry(frame1,width=31,border=5,font=('arial',10),textvariable=Name)
username_ent.grid(row=1,column=1,padx=2,pady=12)


contact=Label(frame1,text='Contact',bg='#9e8de3',font=('arial',14))
contact.grid(row=2,column=0,padx=2,pady=12)

contact_ent=Entry(frame1,width=31,border=5,font=('arial',10),textvariable=Contact)
contact_ent.grid(row=2,column=1,padx=2,pady=12)

email=Label(frame1,text='Email',bg='#9e8de3',font=('arial',14))
email.grid(row=3,column=0,padx=2,pady=12)

email_ent=Entry(frame1,width=31,border=5,font=('arial',10),textvariable=Email)
email_ent.grid(row=3,column=1,padx=2,pady=12)

consoleId=Label(frame1,text='Console Id',bg='#9e8de3',font=('arial ',14))
consoleId.grid(row=4,column=0,padx=2,pady=12)

consoleId_ent=ttk.Combobox(frame1,font=('arial',10),state="readonly",width=30,textvariable=ConsoleId)
consoleId_ent['values']=("1","2","3","4","5","6","7")

consoleId_ent.grid(row=4,column=1,padx=2,pady=12)

console=Label(frame1,text='Console',bg='#9e8de3',font=('arial ',14))
console.grid(row=5,column=0,padx=2,pady=12)

console_ent=Entry(frame1,width=31,border=5,font=('arial',10),textvariable=Console)
console_ent.grid(row=5,column=1,padx=2,pady=12)


payment=Label(frame1,text='Payment',bg='#9e8de3',font=('arial',14))
payment.grid(row=6,column=0,padx=2,pady=12)

payment_ent=ttk.Combobox(frame1,font=('arial',10),state="readonly",width=30,textvariable=Payment)
payment_ent['values']=("Paid","Unpaid")
payment_ent.grid(row=6,column=1,padx=2,pady=12)
#####----------------------------------------
#####----------------------------------------
btn_frame=Frame(frame1,bg='#beb3ed',bd=10,relief=GROOVE)
btn_frame.place(x=20,y=390,width=340,height=110)

btn1=Button(btn_frame,bg='#ffffff',width=15,text='Add',font=('arial',11),border=5,command=add_func)
btn1.grid(row=0,column=0,padx=3,pady=2)

btn2=Button(btn_frame,bg='#ffffff',width=15,text='Update',font=('arial',11),border=5,command=update_func)
btn2.grid(row=0,column=1,padx=3,pady=2)

btn3=Button(btn_frame,bg='#ffffff',width=15,text='Delete',font=('arial',11),border=5,command=delete_func)
btn3.grid(row=1,column=0,padx=3,pady=2)

btn4=Button(btn_frame,bg='#ffffff',width=15,text='Clear',font=('arial',11),border=5,command=clear)
btn4.grid(row=1,column=1,padx=3,pady=2)

#####----------------------------------------
#--------Search-------#
search_frame=Frame(frame2,bg='#9e8de3',bd=10,relief=GROOVE)
search_frame.pack(side=TOP,fill=X)
                  
lbl=Label(search_frame,text="Search",bg="#9e8de3",font=("Arial",12))
lbl.grid(row=0,column=0,padx=10,pady=2)
         
search_in=Entry(search_frame,width=31,bd=5,font=("arial",11),textvariable=search_by)
#search_in["values"]=("Id","Name","Contact","Email","Console Id","Console","Payment")
search_in.grid(row=0,column=1,padx=10,pady=2)
               
btn5=Button(search_frame,text="Search",font=("arial",11),bd=5,width=10,bg="#ffffff",command=perform_database_search)
btn5.grid(row=0,column=2,padx=14,pady=2)
          
btn6=Button(search_frame,text="Show All",font=("arial",11),bd=5,width=10,bg="#ffffff",command=fetch_data)
btn6.grid(row=0,column=3,padx=14,pady=2)
#####----------------------------------------
#---Database--#
main_frame=Frame(frame2,bg='lightgrey',bd=11,relief=GROOVE)
main_frame.pack(fill=BOTH,expand=TRUE)
                
y_scroll=Scrollbar(main_frame,orient=VERTICAL)
x_scroll=Scrollbar(main_frame,orient=HORIZONTAL)
                   
table=ttk.Treeview(main_frame,columns=("Id","Name","Time","Contact","Email","Console Id","Console","Payment"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=table.yview)
x_scroll.config(command=table.xview)

y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)
              
table.heading("Id",text="Id")
table.heading("Name",text="Name")
table.heading("Time",text="Time")
table.heading("Contact",text="Contact")
table.heading("Email",text="Email")
table.heading("Console Id",text="Console Id")
table.heading("Console",text="Console")
table.heading("Payment",text="Payment")
              
table['show']='headings'
table.column("Id",width=150)
table.column("Name",width=150)
table.column("Time",width=150)
table.column("Contact",width=150)
table.column("Email",width=150)
table.column("Console Id",width=150)
table.column("Console",width=150)
table.column("Payment",width=150)
             
table.pack(fill=BOTH,expand=TRUE)

table.bind("<ButtonRelease-1>",get_cursor)
           
Window.mainloop()