#calculator
from tkinter import *
x = Tk()
x.minsize(width=330,height=440)
x.title("Calculator")

eq =""
var=StringVar()

def btn(no):
    global eq
    eq = eq+str(no)
    var.set(eq)

def clear1():
    global eq
    eq=""
    e1.delete(0,END)
    var.set(eq)
def show():
    global eq
    s=var.get()
    # print(s)
    s=eval(s)
    eq=str(s)
    var.set(eq)


e1 = Entry(x,font=5,textvariable=var)
e1.place(x=25,y=25)

b1 = Button(x,text="1",font=8,command=lambda:btn(1))
b1.place(x=35,y=75)
 
b2 = Button(x,text="2",font=8,command=lambda:btn(2))
b2.place(x=75,y=75)
 
b3 = Button(x,text="3",font=8,command=lambda:btn(3))
b3.place(x=115,y=75)

b_add = Button(x,text=" +",font=8,command=lambda:btn("+"))
b_add.place(x=155,y=75)

 
b4 = Button(x,text="4",font=8,command=lambda:btn(4))
b4.place(x=35,y=115)
 
b5 = Button(x,text="5",font=8,command=lambda:btn(5))
b5.place(x=75,y=115)
 
b6 = Button(x,text="6",font=8,command=lambda:btn(6))
b6.place(x=115,y=115)

b_sub = Button(x,text=" - ",font=8,command=lambda:btn("-"))
b_sub.place(x=155,y=115)

 
b7 = Button(x,text="7",font=8,command=lambda:btn(7))
b7.place(x=35,y=155)
 
b8 = Button(x,text="8",font=8,command=lambda:btn(8))
b8.place(x=75,y=155)
 
b9 = Button(x,text="9",font=8,command=lambda:btn(9))
b9.place(x=115,y=155)

b_multi = Button(x,text=" * ",font=8,command=lambda:btn("*"))
b_multi.place(x=155,y=155)

bc = Button(x,text="C",font=8,command=clear1)
bc.place(x=35,y=195)

b0 =Button(x,text="0",font=8,command=lambda:btn(0) )
b0.place(x=75,y=195)

bequal = Button(x,text="=",font=8,command=show)
bequal.place(x=115,y=195)

b_div = Button(x,text=" / ",font=8,command=lambda:btn("/"))
b_div.place(x=155,y=195)

x.mainloop()