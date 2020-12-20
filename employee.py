from tkinter import *
def save():
    teext='Name is : '+name1.get()+'\n'+'Employee Salary is :'+name2.get()+'\n'+'Allowance is : '+name3.get()+'\n'+'Tax Deduction is : '+name4.get()+'\n'+'Net Salary is : '+name5.get()
    with open('teext.txt','w')as f:
        f.writelines(teext)
def isequal():
 salary=float(name2.get())
 allowance=float(name3.get())
 tax=(salary+allowance)/float(name4.get())
 net=salary+allowance-tax
 text_Input.set(str(net))
cal=Tk()
cal.title("Salary Calculate")
cal.geometry("800x400")
operator=""
text_Input=StringVar()
heading=Label(cal,font=("arial",25,'bold'),text="Employee Salary",fg="blue")
heading.pack()
name=Label(cal,font=("arial",15,"bold"),text="Employee Name").place(x=10,y=45)
salary=Label(cal,font=("arial",15,"bold"),text="Employee Salary").place(x=10,y=95)
allo=Label(cal,font=("arial",15,"bold"),text="Allowance").place(x=10,y=150)
tax=Label(cal,font=("arial",15,"bold"),text="Tax Deduction").place(x=10,y=205)
net=Label(cal,font=("arial",15,"bold"),text="Net Salary").place(x=10,y=260)
#=================================================================================
name1=Entry(cal,font=(15))
name1.place(x=250,y=50)
name2=Entry(cal,font=(15))
name2.place(x=250,y=100)
name3=Entry(cal,font=(15))
name3.place(x=250,y=150)
name4=Entry(cal,font=(15))
name4.place(x=250,y=200)
name5=Entry(cal,font=(15), textvariable=text_Input)
name5.place(x=250,y=265)
#=================================================================================
save=Button(cal,font=("arial",15,'bold'),text="Save",bg="black",fg="white",command=save).place(x=10,y
=300)
net=Button(cal,font=("arial",15,'bold'),text="Net Salary",bg="black",fg="white",command=isequal).place(x=320,y=300)
cal.mainloop()
