# -*- coding: cp936 -*-
from tkinter import *

# root = Tk()
# root.title("hello world")
# root.geometry('200x100')  # ��x ����*
# root.resizable(width=True, height=True)  # ���ɱ�, �߿ɱ�,Ĭ��ΪTrue
# root.title("hello world")
# root.geometry('300x200')
# l = Label(root, text="show", bg="black", font=("Arial", 12), width=5, height=2)
# l.pack(side=TOP)  # �����side���Ը�ֵΪLEFT  RTGHT TOP  BOTTOM
# root.mainloop()
# root.mainloop()

from tkinter import *


# root = Tk()
# root.title("hello world")
# root.geometry('300x200')
#
# Label(root, text='Уѵ', font=('Arial', 20)).pack()
#
#
# frm = Frame(root)
# #left
# frm_L = Frame(frm)
# Label(frm_L, text='���', font=('Arial', 15)).pack(side=TOP)
# Label(frm_L, text='��ѧ', font=('Arial', 15)).pack(side=TOP)
# frm_L.pack(side=LEFT)
#
# #right
# frm_R = Frame(frm)
# Label(frm_R, text='��ҵ', font=('Arial', 15)).pack(side=TOP)
# Label(frm_R, text='��Ⱥ', font=('Arial', 15)).pack(side=TOP)
# frm_R.pack(side=RIGHT)
#
# frm.pack()
#
# root.mainloop()


# -*- coding: cp936 -*-

root = Tk()
root.title("hello world")
root.geometry()
var = StringVar()
e = Entry(root, textvariable=var)
var.set("hello")
e.pack()

root.mainloop()