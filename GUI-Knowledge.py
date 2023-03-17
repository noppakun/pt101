from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')


L1= Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsaana New',30),fg='green')
L1.place(x=10,y=10)

def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showerror('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=100)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท2',command=Button2)
B2.pack(ipadx=20,ipady=20)
 

def Button3():
    text = 'python'
    messagebox.showerror('วิชา',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=200)
B3 = ttk.Button(FB2,text='วิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)
 








GUI.mainloop()


