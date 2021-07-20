import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random as rn
import time as tm

main=tk.Tk()
main.geometry('600x365')
main.title('Snake & Ladder')
main.config(bg='#F1F1F2')
main.resizable(0,0)
main.iconbitmap('logo.ico')

load = Image.open('img.png')
render = ImageTk.PhotoImage(load)
img = tk.Label(image=render)
img.place(x=5,y=5)

rad_var=tk.StringVar()
fn1=tk.StringVar()
fn2=tk.StringVar()
fn3=tk.StringVar()
fn4=tk.StringVar()
fn5=tk.StringVar()

def glob():
    global r
    global g
    global b
    global y
    r=g=b=y=0
    fn1.set('0')
    fn2.set('0')
    fn3.set('0')
    fn4.set('0')
    rad_var.set('R')
    fn5.set('Roll')

def chk(p):
    switcher={
        '5': '25',
        '10': '29',
        '22': '41',
        '28': '55',
        '31': '14',
        '37': '17',
        '44': '95',
        '70': '89',
        '73': '53',
        '78': '39',
        '79': '81',
        '92': '35',
        '99': '7'
            }
    func = switcher.get(p,p)
    return func

def forward(p,val):
    a=int(p.get())
    a=a+val
    if(a>100):
        a=a-val
    elif(a==100):
        p.set('Winner')
    else:
        p.set(chk(str(a)))

def rotate():
    global r,g,b,y
    val = rn.randint(1,6)
    fn5.set(val)
    if ((rad_var.get()=='R') and (val>1) and (r==0)):
        rad_var.set('B')
    elif ((rad_var.get()=='B') and (val>1) and (b==0)):
        rad_var.set('G')
    elif ((rad_var.get()=='G') and (val>1) and (g==0)):
        rad_var.set('Y')
    elif ((rad_var.get()=='Y') and (val>1) and (y==0)):
        rad_var.set('R')
    elif ((rad_var.get()=='R') and (val==1) and (r==0)):
        r=1
        forward(fn1,val)
        rad_var.set('R')
    elif ((rad_var.get()=='B') and (val==1) and (b==0)):
        b=1
        forward(fn2,val)
        rad_var.set('B')
    elif ((rad_var.get()=='G') and (val==1) and (g==0)):
        g=1
        forward(fn3,val)
        rad_var.set('G')
    elif ((rad_var.get()=='Y') and (val==1) and (y==0)):
        y=1
        forward(fn4,val)
        rad_var.set('Y')
    elif ((rad_var.get()=='R') and (val==1) and (r==1)):
        forward(fn1,val)
        rad_var.set('R')
    elif ((rad_var.get()=='R') and (val>1) and (r==1)):
        forward(fn1,val)
        rad_var.set('B')
    elif ((rad_var.get()=='B') and (val==1) and (b==1)):
        forward(fn2,val)
        rad_var.set('B')
    elif ((rad_var.get()=='B') and (val>1) and (b==1)):
        forward(fn2,val)
        rad_var.set('G')
    elif ((rad_var.get()=='G') and (val==1) and (g==1)):
        forward(fn3,val)
        rad_var.set('G')
    elif ((rad_var.get()=='G') and (val>1) and (g==1)):
        forward(fn3,val)
        rad_var.set('Y')
    elif ((rad_var.get()=='Y') and (val==1) and (y==1)):
        forward(fn4,val)
        rad_var.set('Y')
    elif ((rad_var.get()=='Y') and (val>1) and (y==1)):
        forward(fn4,val)
        rad_var.set('R')

fm = tk.Frame(main,bd=2,relief=tk.RIDGE,height=355,width=220)
fm.place(x=370,y=5)
lbf1 = tk.LabelFrame(main,text='Score Board',height=200,width=200)
lbf1.place(x=380,y=45)
lbf2 = tk.LabelFrame(main,text='Play Area',height=100,width=200)
lbf2.place(x=380,y=245)

ttk.Radiobutton(lbf1,text="RED",variable=rad_var,value='R').place(x=10,y=10)
ttk.Radiobutton(lbf1,text="BLUE",variable=rad_var,value='B').place(x=10,y=40)
ttk.Radiobutton(lbf1,text="GREEN",variable=rad_var,value='G').place(x=10,y=70)
ttk.Radiobutton(lbf1,text="YELLOW",variable=rad_var,value='Y').place(x=10,y=100)

tk.Label(lbf1,text='-- Alik Dey creation\nAshirwad TechnoCraft',fg='#1995AD',relief=tk.FLAT,font=('Times New Roman',10,'italic')).place(x=60,y=140)

ttk.Entry(lbf1,textvariable=fn1,width=8,justify=tk.CENTER,state=tk.DISABLED).place(x=100,y=10)
ttk.Entry(lbf1,textvariable=fn2,width=8,justify=tk.CENTER,state=tk.DISABLED).place(x=100,y=40)
ttk.Entry(lbf1,textvariable=fn3,width=8,justify=tk.CENTER,state=tk.DISABLED).place(x=100,y=70)
ttk.Entry(lbf1,textvariable=fn4,width=8,justify=tk.CENTER,state=tk.DISABLED).place(x=100,y=100)

ttk.Entry(lbf2,textvariable=fn5,width=8,justify=tk.CENTER,state=tk.DISABLED).place(x=10,y=10)

st=ttk.Style()
st.configure("ab.TButton",background='#BCBABE',foreground='black',width=10,borderwidth=1,focusthickness=3,focuscolor='none')
ttk.Button(lbf2,text='DICE',style='ab.TButton',command=rotate).place(x=80,y=8)
st.configure("bc.TButton",background='#BCBABE',foreground='black',width=31,borderwidth=1,focusthickness=3,focuscolor='none')
ttk.Button(fm,text='New Game',style='bc.TButton',command=glob).place(x=9,y=9)

glob()
main.mainloop()
