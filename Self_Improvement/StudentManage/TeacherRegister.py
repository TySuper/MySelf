from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
from Common.OperateMysql import UseMysql


class TeacherRegister:
    """
    （销毁上一个窗口）初始化一个根窗口window；
    添加Label标签控件，用于单行文本显示"教师注册页面"，“输入账号”、“输入密码”、“确认账号”；
    添加三个Entry输入控件，用于显示用户输入文本，添加两个Button按钮控件，将其分别与关联函数register、back绑定；
    在主事件循环中等待用户触发事件响应。
    """
    username = input()
    password = input()
    repassword = input()

    def register(self):
        """
        教室注册
        :return:
        """

        # 数据库的方式后期加入从配置文件读取账户,密码,地址等
        db = UseMysql("192.168.170.138", 'root', "abc@123")
        sql = f"select * from teacher_login where username = {self.username}"
        res = db.fetchone("sql")

