from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import StudentPage
import TeacherPage
import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_username = self.__tk_label_username()
        self.tk_label_password = self.__tk_label_password()
        self.tk_input_username = self.__tk_input_username()
        self.tk_input_password = self.__tk_input_password()
        self.tk_button_login = self.__tk_button_login()
        self.tk_button_reset = self.__tk_button_reset()

    def __win(self):
        self.title("登录")
        # 设置窗口大小、居中
        width = 400
        height = 200
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.iconbitmap('logo.ico')

    def __tk_label_username(self):
        label = Label(self, text="账号")
        label.place(x=90, y=30, width=50, height=24)
        return label

    def __tk_label_password(self):
        label = Label(self, text="密码")
        label.place(x=90, y=80, width=50, height=24)
        return label

    def __tk_input_username(self):
        self.username_value = StringVar(self)
        ipt = Entry(self, text=self.username_value)
        ipt.place(x=160, y=30, width=150, height=24)
        return ipt

    def __tk_input_password(self):
        self.password_value = StringVar(self)
        ipt = Entry(self, text=self.password_value, show='*')
        ipt.place(x=160, y=80, width=150, height=24)
        return ipt

    def __tk_button_login(self):
        btn = Button(self, text="登录")
        btn.place(x=120, y=130, width=50, height=30)
        return btn

    def __tk_button_reset(self):
        btn = Button(self, text="重置")
        btn.place(x=230, y=130, width=50, height=30)
        return btn


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def login(self, evt):
        __uid = self.tk_input_username.get()
        __pwd = self.tk_input_password.get()
        __data = Dao.getUserByIdAndPwd(__uid, __pwd).get("data")
        if __data:
            messagebox.showwarning('提示', '登录成功！')
            self.destroy()
            if __data.get("urole") == 1:
                student = StudentPage.Win(__data)
                student.mainloop()
            elif __data.get("urole") == 0:
                teacher = TeacherPage.Win(__data)
                teacher.mainloop()
            else:
                print("未获取到用户角色！")
        else:
            messagebox.showwarning('提示', '账号或密码错误')

    def reset(self, evt):
        self.username_value.set("")
        self.password_value.set("")
        self.tk_input_username.focus_set()

    def __event_bind(self):
        self.tk_button_login.bind('<Button-1>', self.login)
        self.tk_input_username.bind('<Return>', self.login)
        self.tk_input_password.bind('<Return>', self.login)
        self.tk_button_reset.bind('<Button-1>', self.reset)

