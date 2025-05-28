import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter
win=tkinter.Tk()
wi=win.winfo_screenwidth()
print(wi)
hi=win.winfo_screenheight()
print(hi)
win.configure(width=wi,height=hi,bg="blue")
img1=Image.open("C:/Users/dell/Pictures/student pic.png")
img2=ImageTk.PhotoImage(img1)
imglbl=tkinter.Label(win,image=img2)
imglbl.place(x=700,y=50)

def clearfun():
    
    rnotb.delete(0,"end")
    snametb.delete(0,"end")
    saddtb.delete(0,"end")
    smarktb.delete(0,"end")
    sranktb.delete(0,"end")    
    

def insertfun():
    rno=int(rnotb.get())
    sname=snametb.get()
    sadd=saddtb.get()
    smark=float(smarktb.get())
    srank=int(sranktb.get())    
    con=mysql.connector.connect(host="localhost",user="root",password="123456",database="detstd")
    cur=con.cursor()
    cur.execute("insert into detst values(%d,'%s','%s',%f,%d)"%(rno,sname,sadd,smark,srank))
    con.commit()
    messagebox.showinfo("success","successfully inserted")
  
rnolbl=tkinter.Label(win,text="Enter rno:")
snamelbl=tkinter.Label(win,text="Enter sname:")
saddlbl=tkinter.Label(win,text="Enter sadd:")
smarklbl=tkinter.Label(win,text="Enter smark:")
sranklbl=tkinter.Label(win,text="Enter srank:")
 

rnotb=tkinter.Entry(win)
snametb=tkinter.Entry(win)
saddtb=tkinter.Entry(win)
smarktb=tkinter.Entry(win)
sranktb=tkinter.Entry(win)

rnolbl.place(x=100,y=100)
snamelbl.place(x=100,y=200)
saddlbl.place(x=100,y=300)
smarklbl.place(x=100,y=400)
sranklbl.place(x=100,y=500)

rnotb.place(x=500,y=100)
snametb.place(x=500,y=200)
saddtb.place(x=500,y=300)
smarktb.place(x=500,y=400)
sranktb.place(x=500,y=500)


but1=tkinter.Button(win,text="Insert/Save",command=insertfun)
but1.place(x=500,y=600)
but2=tkinter.Button(win,text="clear",command=clearfun)
but2.place(x=580,y=600)
win.mainloop()
