from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_stu_number = self.__tk_label_stu_number()
        self.tk_input_stu_number = self.__tk_input_stu_number()
        self.tk_button_delete_course = self.__tk_button_delete_course()
        self.tk_button_cancel_course = self.__tk_button_cancel_course()

    def __win(self):
        self.title("删除课程")
        # 设置窗口大小、居中
        width = 400
        height = 200
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_stu_number(self):
        label = Label(self, text="课程号", anchor="center")
        label.place(x=70, y=50, width=80, height=30)
        return label

    def __tk_input_stu_number(self):
        ipt = Entry(self)
        ipt.place(x=180, y=50, width=150, height=30)
        return ipt

    def __tk_button_delete_course(self):
        btn = Button(self, text="删除")
        btn.place(x=100, y=110, width=80, height=30)
        return btn

    def __tk_button_cancel_course(self):
        btn = Button(self, text="取消")
        btn.place(x=220, y=110, width=80, height=30)
        return btn


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def deleteCourse(self, evt):
        if len(Dao.getCourseByCid(self.tk_input_stu_number.get()).get("data")) != 0:
            messagebox.showwarning("提示", Dao.deleteCourse(self.tk_input_stu_number.get()).get("msg"))
            self.destroy()
        else:
            messagebox.showwarning("提示", "学号不存在！")

    def cancelCourse(self, evt):
        self.destroy()

    def __event_bind(self):
        self.tk_button_delete_course.bind('<Button-1>', self.deleteCourse)
        self.tk_button_cancel_course.bind('<Button-1>', self.cancelCourse)

