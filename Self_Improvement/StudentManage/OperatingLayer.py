from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
from Common.OperateMysql import UseMysql


class StartMenu():
    """
    根窗口window,首页展示
    """

    def __init__(self):
        # 创建主窗口
        win = tkinter.Tk()
        # 设置标题
        win.title("管理系统")
        # 设置大写和位置
        width, height = 900, 900
        # 进入消息循环，可以写控件
        # 窗口居中显示
        win.geometry('%dx%d+%d+%d' % (
            width, height, (win.winfo_screenwidth() - width) / 2, (win.winfo_screenheight() - height) / 2))
        # 窗口最大值
        win.maxsize(900, 900)
        win.minsize(600, 600)
        '''
        Labels标签控件，可以显示文本
        win：父窗口
        text：显示的文本内容
        bg：背景颜色
        fg：字体颜色
        font：字体
        wraplength：指定text文本中多宽后换行
        justify：设置换行后的对齐方式
        anchor：位置 n北，s,w,e,center居中：还可以写在一起：ne东北方向
        '''

        # 创建按钮
        def register():
            """登录,注册的函数"""
            print("注册")

        def login():
            """登录"""
            print("登录")

        Label(win, text="ASCII码查询", font=('Arial', 30)).place(x=430, y=300, anchor='center')

        button1 = tkinter.Button(win, text='注册', command=register, width=30, height=2, anchor='center')
        button1.place(x=430, y=360, anchor='center')

        button2 = tkinter.Button(win, text='登录', command=login, width=30, height=2, anchor='center')
        button2.place(x=430, y=410, anchor='center')

        button3 = tkinter.Button(win, text='退出', command=win.quit, width=30, height=2, anchor='center', )
        button3.place(x=430, y=460, anchor='center')

        # 进入消息循环，可以写控件
        win.mainloop()


if __name__ == '__main__':
    StartMenu()
