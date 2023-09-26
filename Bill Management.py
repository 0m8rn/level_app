from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

# def
def Reset():
    Entry_C.delete(0,END)
    Entry_HTML.delete(0,END)
    Entry_CSS.delete(0,END)
    Entry_JS.delete(0,END)
    Entry_GO.delete(0,END)
    Entry_PHP.delete(0,END)
    Entry_SQL.delete(0,END)
    Entry_JAVA.delete(0,END)

def Total():
    try:a1= int(HTML.get())
    except: a1=0

    try:a2= int(CSS.get())
    except: a2=0

    try:a3= int(JS.get())
    except: a3=0

    try:a4= int(GO.get())
    except: a4=0

    try:a5= int(PHP.get())
    except: a5=0

    try:a6= int(SQL.get())
    except: a6=0

    try:a7= int(JAVA.get())
    except: a7=0
    try:a8= int(C.get())
    except: a8=0

    c1 = 10*a1
    c2 = 10*a2
    c3 = 30*a3
    c4 = 20*a4
    c5 = 40*a5
    c6 = 20*a6
    c7 = 50*a7
    c8 = 70*a8
    
    lbl_total =Label(f2,font=('aria',20,'bold')
                     ,text="TOTAL",
                     width=16,
                     fg="#eee",
                     bg="black")
    
    lbl_total.place(x=0, y=50)

    Entry_total = Entry(f2,font=('aria',20,'bold'),
                        textvariable=total_bill,
                        bd=6,width=15,
                        bg="#eee")
    Entry_total.place(x=20, y=100)

#    f"${total_cost:.2f}"
#    f"$.",str('%.2f'%total_cost)

    total_cost = c1+c2+c3+c4+c5+c6+c7+c8
    string_bill = f"${total_cost:.2f}"
    total_bill.set(string_bill)

Label(text="MANAGEMENT SYSTEM"
      ,bg="black",
      fg="white",
      font=("calibri",33),
      width="300",
      height="2").pack()

# MENU card
f = Frame(root,bg="#eee",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)
Label(f,text="Courses",font=("Gabriola",40,"bold"),fg="black",bg="#eee").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="C ==> 70$/month",fg="black",bg="#eee").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="HTML ==> 10$/month",fg="black",bg="#eee").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="CSS ==> 10$/month",fg="black",bg="#eee").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="JS ==> 30$/month",fg="black",bg="#eee").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="GO ==> 20$/month",fg="black",bg="#eee").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="PHP ==> 40$/month",fg="black",bg="#eee").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="SQL ==> 20$/month",fg="black",bg="#eee").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="JAVA ==> 50$/month",fg="black",bg="#eee").place(x=10,y=290)

# BILL
f2 = Frame(root,bg="#eee",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690, y=118)
BILL = Label(f2,text="BILL",font=('calibri',20),bg='#eee')
BILL.place(x=120, y=10)

# ENTER WORK
f1 = Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

C = StringVar()
HTML = StringVar()
CSS = StringVar()
JS = StringVar()
GO = StringVar()
PHP = StringVar()
SQL = StringVar()
JAVA = StringVar()
total_bill = StringVar()

# lable
lbl_C = Label(f1,font=("aria",20,"bold"),text="C",width=12,fg="black")
lbl_HTML = Label(f1,font=("aria",20,"bold"),text="HTML",width=12,fg="black")
lbl_CSS = Label(f1,font=("aria",20,"bold"),text="CSS",width=12,fg="black")
lbl_JS = Label(f1,font=("aria",20,"bold"),text="JS",width=12,fg="black")
lbl_GO = Label(f1,font=("aria",20,"bold"),text="GO",width=12,fg="black")
lbl_PHP = Label(f1,font=("aria",20,"bold"),text="PHP",width=12,fg="black")
lbl_SQL = Label(f1,font=("aria",20,"bold"),text="SQL",width=12,fg="black")
lbl_JAVA = Label(f1,font=("aria",20,"bold"),text="JAVA",width=12,fg="black")

lbl_C.grid(row=1,column=0)
lbl_HTML.grid(row=2,column=0)
lbl_CSS.grid(row=3,column=0)
lbl_JS.grid(row=4,column=0)
lbl_GO.grid(row=5,column=0)
lbl_PHP.grid(row=6,column=0)
lbl_SQL.grid(row=7,column=0)
lbl_JAVA.grid(row=8,column=0)

# Entry
Entry_C = Entry(f1, font=("aria",20,'bold'),textvariable=C,bd=6,width=8,bg="#eee")
Entry_HTML = Entry(f1, font=("aria",20,'bold'),textvariable=HTML,bd=6,width=8,bg="#eee")
Entry_CSS = Entry(f1, font=("aria",20,'bold'),textvariable=CSS,bd=6,width=8,bg="#eee")
Entry_JS = Entry(f1, font=("aria",20,'bold'),textvariable=JS,bd=6,width=8,bg="#eee")
Entry_GO = Entry(f1, font=("aria",20,'bold'),textvariable=GO,bd=6,width=8,bg="#eee")
Entry_PHP = Entry(f1, font=("aria",20,'bold'),textvariable=PHP,bd=6,width=8,bg="#eee")
Entry_SQL = Entry(f1, font=("aria",20,'bold'),textvariable=SQL,bd=6,width=8,bg="#eee")
Entry_JAVA = Entry(f1, font=("aria",20,'bold'),textvariable=JAVA,bd=6,width=8,bg="#eee")

Entry_C.grid(row=1,column=1)
Entry_HTML.grid(row=2,column=1)
Entry_CSS.grid(row=3,column=1)
Entry_JS.grid(row=4,column=1)
Entry_GO.grid(row=5,column=1)
Entry_PHP.grid(row=6,column=1)
Entry_SQL.grid(row=7,column=1)
Entry_JAVA.grid(row=8,column=1)

# BUTTONS

btn_reset = Button(f1,bd=5,fg="black",bg="#eee",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total = Button(f1,bd=5,fg="black",bg="#eee",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()