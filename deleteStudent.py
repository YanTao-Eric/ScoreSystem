from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lbn30yj2 = self.__tk_label_lbn30yj2()
        self.tk_input_studentid = self.__tk_input_studentid()
        self.tk_button_delete = self.__tk_button_delete()
        self.tk_button_reset = self.__tk_button_reset()

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 292
        height = 85
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_lbn30yj2(self):
        label = Label(self, text="请输入学号：", anchor="center")
        label.place(x=30, y=10, width=69, height=24)
        return label

    def __tk_input_studentid(self):
        ipt = Entry(self)
        ipt.place(x=100, y=10, width=150, height=24)
        return ipt

    def __tk_button_delete(self):
        btn = Button(self, text="删除")
        btn.place(x=60, y=50, width=50, height=24)
        return btn

    def __tk_button_reset(self):
        btn = Button(self, text="取消")
        btn.place(x=160, y=50, width=50, height=24)
        return btn


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def deleteStudent(self, evt):
        value = self.tk_input_studentid.get()
        result = Dao.deleteUser(value)
        print(value)
        if result.get("code") == 0:
            messagebox.showinfo(title='提示', message='删除成功！')
        else:
            messagebox.showerror(title='删除失败！', message='查无此人!')

    def reset(self, evt):
        self.destroy()

    def __event_bind(self):
        self.tk_button_delete.bind('<Button-1>', self.deleteStudent)
        self.tk_button_reset.bind('<Button-1>', self.reset)


