from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_course_name = self.__tk_label_course_name()
        self.tk_input_course_name = self.__tk_input_course_name()
        self.tk_label_course_nature = self.__tk_label_course_nature()
        self.tk_label_course_credit = self.__tk_label_course_credit()
        self.tk_input_course_credit = self.__tk_input_course_credit()
        self.tk_label_course_department = self.__tk_label_course_department()
        self.tk_label_course_exam_method = self.__tk_label_course_exam_method()
        self.tk_button_add_course = self.__tk_button_add_course()
        self.tk_button_reset_course = self.__tk_button_reset_course()
        self.tk_select_box_course_nature = self.__tk_select_box_course_nature()
        self.tk_select_box_course_department = self.__tk_select_box_course_department()
        self.tk_select_box_course_exam_method = self.__tk_select_box_course_exam_method()

    def __win(self):
        self.title("添加课程")
        # 设置窗口大小、居中
        width = 600
        height = 430
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_course_name(self):
        label = Label(self, text="课程名称", anchor="center")
        label.place(x=160, y=50, width=100, height=30)
        return label

    def __tk_input_course_name(self):
        self.course_name = StringVar(self)
        ipt = Entry(self, text=self.course_name)
        ipt.place(x=290, y=50, width=150, height=30)
        return ipt

    def __tk_label_course_nature(self):
        label = Label(self, text="课程性质", anchor="center")
        label.place(x=160, y=110, width=100, height=30)
        return label

    def __tk_label_course_credit(self):
        label = Label(self, text="课程学分", anchor="center")
        label.place(x=160, y=170, width=100, height=30)
        return label

    def __tk_input_course_credit(self):
        self.course_credit = StringVar(self)
        ipt = Entry(self, text=self.course_credit)
        ipt.place(x=290, y=170, width=150, height=30)
        return ipt

    def __tk_label_course_department(self):
        label = Label(self, text="开课学院", anchor="center")
        label.place(x=160, y=230, width=100, height=30)
        return label

    def __tk_label_course_exam_method(self):
        label = Label(self, text="考试方式", anchor="center")
        label.place(x=160, y=290, width=100, height=30)
        return label

    def __tk_button_add_course(self):
        btn = Button(self, text="添加")
        btn.place(x=200, y=360, width=80, height=30)
        return btn

    def __tk_button_reset_course(self):
        btn = Button(self, text="重置")
        btn.place(x=320, y=360, width=80, height=30)
        return btn

    def __tk_select_box_course_nature(self):
        cb = Combobox(self, state="readonly")
        values = []
        for i in Dao.getDataDictByType("nature").get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=290, y=110, width=150, height=30)
        return cb

    def __tk_select_box_course_department(self):
        cb = Combobox(self, state="readonly")
        values = []
        for i in Dao.getAllDepartments().get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=290, y=230, width=150, height=30)
        return cb

    def __tk_select_box_course_exam_method(self):
        cb = Combobox(self, state="readonly")
        values = []
        for i in Dao.getDataDictByType("exammethod").get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=290, y=290, width=150, height=30)
        return cb


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def addCourse(self, evt):
        __course_name = self.tk_input_course_name.get()
        __course_nature = self.tk_select_box_course_nature.get()
        __course_credit = self.tk_input_course_credit.get()
        __course_department = self.tk_select_box_course_department.get()
        __course_exam_method = self.tk_select_box_course_exam_method.get()
        if not __course_name:
            messagebox.showerror("错误", "课程名称为空！")
        elif not re.findall(r'^(0\.5)|(8\.0)|[1-7](\.[0,5])?$', __course_credit):
            messagebox.showerror("错误", "学分格式不合法(0.5-8.0)！")
        else:
            res = Dao.addCourse(__course_name, __course_nature, __course_credit, __course_department, __course_exam_method)
            if res.get("code") == 0:
                messagebox.showwarning("提示", res.get("msg"))
                self.destroy()
            else:
                messagebox.showwarning("提示", res.get("msg"))

    def resetCourse(self, evt):
        self.course_name.set('')
        self.tk_select_box_course_nature.current(0)
        self.course_credit.set('')
        self.tk_select_box_course_department.current(0)
        self.tk_select_box_course_exam_method.current(0)
        print("重置成功！", evt)

    def __event_bind(self):
        self.tk_button_add_course.bind('<Button-1>', self.addCourse)
        self.tk_button_reset_course.bind('<Button-1>', self.resetCourse)


