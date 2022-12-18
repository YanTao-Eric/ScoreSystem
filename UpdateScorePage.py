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
        self.tk_label_stu_course = self.__tk_label_stu_course()
        self.tk_select_box_stu_course = self.__tk_select_box_stu_course()
        self.tk_label_stu_score = self.__tk_label_stu_score()
        self.tk_input_stu_score = self.__tk_input_stu_score()
        self.tk_button_add_score = self.__tk_button_add_score()
        self.tk_button_cancel_score = self.__tk_button_cancel_score()

    def __win(self):
        self.title("修改成绩")
        # 设置窗口大小、居中
        width = 400
        height = 280
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_stu_number(self):
        label = Label(self, text="学号", anchor="center")
        label.place(x=60, y=30, width=100, height=30)
        return label

    def __tk_input_stu_number(self):
        self.student_number = StringVar(self)
        ipt = Entry(self, state='disable', text=self.student_number)
        ipt.place(x=190, y=30, width=150, height=30)
        return ipt

    def __tk_label_stu_course(self):
        label = Label(self, text="课程", anchor="center")
        label.place(x=60, y=90, width=100, height=30)
        return label

    def __tk_select_box_stu_course(self):
        cb = Combobox(self, state="disable")
        values = []
        for i in Dao.getAllCourses().get("data"):
            values.append(i.get("cname"))
        cb['values'] = values
        cb.place(x=190, y=90, width=150, height=30)
        return cb

    def __tk_label_stu_score(self):
        label = Label(self, text="成绩", anchor="center")
        label.place(x=60, y=150, width=100, height=30)
        return label

    def __tk_input_stu_score(self):
        self.student_score = StringVar(self)
        ipt = Entry(self, text=self.student_score)
        ipt.place(x=190, y=150, width=150, height=30)
        return ipt

    def __tk_button_add_score(self):
        btn = Button(self, text="确定")
        btn.place(x=100, y=210, width=80, height=30)
        return btn

    def __tk_button_cancel_score(self):
        btn = Button(self, text="取消")
        btn.place(x=210, y=210, width=80, height=30)
        return btn


class Win(WinGUI):
    def __init__(self, data):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()
        self.student_number.set(data.get("uid"))
        self.tk_select_box_stu_course.set(data.get("cname"))
        self.student_score.set(data.get("score"))

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def updateStuScore(self, evt):
        __stu_number = self.tk_input_stu_number.get()
        __course_name = self.tk_select_box_stu_course.get()
        __stu_score = self.tk_input_stu_score.get()
        if __stu_score == '':
            messagebox.showinfo("提示", "成绩不能为空！")
            return
        if float(__stu_score) > 100 or float(__stu_score) < 0:
            messagebox.showinfo("提示", "成绩应在0~100之间！")
            return
        res = Dao.updateStudentScore(__stu_number, __course_name, __stu_score)
        messagebox.showinfo("提示", res.get("msg"))
        if res.get("code") == 0:
            self.destroy()
        print(f"修改{__stu_number}学生成绩", evt)

    def cancelStuScore(self, evt):
        self.destroy()
        print("取消修改成绩", evt)

    def __event_bind(self):
        self.tk_button_add_score.bind('<Button-1>', self.updateStuScore)
        self.tk_button_cancel_score.bind('<Button-1>', self.cancelStuScore)

