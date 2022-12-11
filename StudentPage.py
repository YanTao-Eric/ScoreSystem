from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_title = self.__tk_label_title()
        self.tk_label_current_user = self.__tk_label_current_user()
        self.tk_label_title = self.__tk_label_title()
        self.tk_label_current_user = self.__tk_label_current_user()
        self.tk_tabs_content = Frame_content(self)
        self.tk_button_logout = self.__tk_button_logout()

    def __win(self):
        self.title("成绩查询")
        # 设置窗口大小、居中
        width = 1000
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.iconbitmap('logo.ico')

    def __tk_label_title(self):
        label = Label(self, text="学生成绩管理系统", anchor="center")
        label.place(x=0, y=0, width=800, height=100)
        return label

    def __tk_label_current_user(self):
        label = Label(self, text="当前用户：admin", anchor="center")
        label.place(x=800, y=70, width=150, height=30)
        return label

    def __tk_button_logout(self):
        btn = Button(self, text="退出")
        btn.place(x=950, y=70, width=50, height=30)
        return btn


class Frame_content(Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.tk_tabs_content_0 = Frame_content_0(self)
        self.add(self.tk_tabs_content_0, text="个人资料")

        self.tk_tabs_content_1 = Frame_content_1(self)
        self.add(self.tk_tabs_content_1, text="成绩查询")

        self.tk_tabs_content_2 = Frame_content_2(self)
        self.add(self.tk_tabs_content_2, text="成绩分析")

        self.tk_tabs_content_3 = Frame_content_3(self)
        self.add(self.tk_tabs_content_3, text="修改密码")

        self.place(x=0, y=100, width=1000, height=500)


class Frame_content_0(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_stu_number = self.__tk_label_stu_number()
        self.tk_input_stu_number = self.__tk_input_stu_number()
        self.tk_label_stu_name = self.__tk_label_stu_name()
        self.tk_input_stu_name = self.__tk_input_stu_name()
        self.tk_label_stu_age = self.__tk_label_stu_age()
        self.tk_input_stu_age = self.__tk_input_stu_age()
        self.tk_label_stu_identity = self.__tk_label_stu_identity()
        self.tk_input_stu_identity = self.__tk_input_stu_identity()
        self.tk_label_stu_tel = self.__tk_label_stu_tel()
        self.tk_input_stu_tel = self.__tk_input_stu_tel()
        self.tk_button_stu_update = self.__tk_button_stu_update()
        self.tk_button_stu_reset = self.__tk_button_stu_reset()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_label_stu_number(self):
        label = Label(self, text="学号", anchor="e")
        label.place(x=360, y=40, width=100, height=30)
        return label

    def __tk_input_stu_number(self):
        ipt = Entry(self)
        ipt.place(x=490, y=40, width=150, height=30)
        return ipt

    def __tk_label_stu_name(self):
        label = Label(self, text="姓名", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_stu_name(self):
        ipt = Entry(self)
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_stu_age(self):
        label = Label(self, text="年龄", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_input_stu_age(self):
        ipt = Entry(self)
        ipt.place(x=490, y=180, width=150, height=30)
        return ipt

    def __tk_label_stu_identity(self):
        label = Label(self, text="身份证号", anchor="e")
        label.place(x=360, y=250, width=100, height=30)
        return label

    def __tk_input_stu_identity(self):
        ipt = Entry(self)
        ipt.place(x=490, y=250, width=150, height=30)
        return ipt

    def __tk_label_stu_tel(self):
        label = Label(self, text="电子邮箱", anchor="e")
        label.place(x=360, y=320, width=100, height=30)
        return label

    def __tk_input_stu_tel(self):
        ipt = Entry(self)
        ipt.place(x=490, y=320, width=150, height=30)
        return ipt

    def __tk_button_stu_update(self):
        btn = Button(self, text="修改")
        btn.place(x=400, y=390, width=80, height=30)
        return btn

    def __tk_button_stu_reset(self):
        btn = Button(self, text="重置")
        btn.place(x=520, y=390, width=80, height=30)
        return btn


class Frame_content_1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_table_stu_score = self.__tk_table_stu_score()
        self.tk_select_box_course_nature = self.__tk_select_box_course_nature()
        self.tk_select_box_course_department = self.__tk_select_box_course_department()
        self.tk_select_box_exam_method = self.__tk_select_box_exam_method()
        self.tk_button_search = self.__tk_button_search()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_table_stu_score(self):
        # 表头字段 表头宽度
        columns = {"ID": 50, "字段#1": 100, "字段#2": 100}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        # 插入数据示例
        # data = [
        #     [1, "github", "https://github.com/iamxcd/tkinter-helper"],
        #     [2, "演示地址", "https://www.pytk.net/tkinter-helper"]
        # ]
        #
        # # 导入初始数据
        # for values in data:
        #     tk_table.insert('', END, values=values)

        tk_table.place(x=0, y=55, width=1000, height=420)
        return tk_table

    def __tk_select_box_course_nature(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("列表框", "Python", "Tkinter Helper")
        cb.place(x=180, y=10, width=150, height=30)
        return cb

    def __tk_select_box_course_department(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("列表框", "Python", "Tkinter Helper")
        cb.place(x=370, y=10, width=150, height=30)
        return cb

    def __tk_select_box_exam_method(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("列表框", "Python", "Tkinter Helper")
        cb.place(x=560, y=10, width=150, height=30)
        return cb

    def __tk_button_search(self):
        btn = Button(self, text="搜索")
        btn.place(x=750, y=10, width=75, height=30)
        return btn


class Frame_content_2(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)


class Frame_content_3(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_original_password = self.__tk_label_original_password()
        self.tk_input_original_password = self.__tk_input_original_password()
        self.tk_label_new_password = self.__tk_label_new_password()
        self.tk_input_new_password = self.__tk_input_new_password()
        self.tk_label_confirm_password = self.__tk_label_confirm_password()
        self.tk_input_confirm_password = self.__tk_input_confirm_password()
        self.tk_button_update_stu_password = self.__tk_button_update_stu_password()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_label_original_password(self):
        label = Label(self, text="原密码", anchor="e")
        label.place(x=360, y=40, width=100, height=30)
        return label

    def __tk_input_original_password(self):
        ipt = Entry(self)
        ipt.place(x=490, y=40, width=150, height=30)
        return ipt

    def __tk_label_new_password(self):
        label = Label(self, text="新密码", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_new_password(self):
        ipt = Entry(self)
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_confirm_password(self):
        label = Label(self, text="确认密码", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_input_confirm_password(self):
        ipt = Entry(self)
        ipt.place(x=490, y=180, width=150, height=30)
        return ipt

    def __tk_button_update_stu_password(self):
        btn = Button(self, text="修改")
        btn.place(x=460, y=250, width=100, height=30)
        return btn


class Win(WinGUI):
    def __init__(self, current_user):
        super().__init__()
        self.__event_bind()
        self.tk_label_current_user['text'] = "当前用户：" + Dao.getUserInfoById(current_user)[1]

    def logout(self):
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()


    def updateUserInfo(self, evt):
        print("<Button-1>事件未处理", evt)

    def resetUserInfo(self, evt):
        print("<Button-1>事件未处理", evt)

    def updateStudentInfo(self, evt):
        print("<Button-1>事件未处理", evt)

    def stu_reset(self, evt):
        print("<Button-1>事件未处理", evt)

    def searchStudentScore(self, evt):
        print("<Button-1>事件未处理", evt)

    def updateStudentPassword(self, evt):
        print("<Button-1>事件未处理", evt)

    def logout_user(self, evt):
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()

    def __event_bind(self):
        self.protocol('WM_DELETE_WINDOW', self.logout)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_update.bind('<Button-1>', self.updateUserInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_reset.bind('<Button-1>', self.resetUserInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_update.bind('<Button-1>', self.updateStudentInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_reset.bind('<Button-1>', self.stu_reset)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_search.bind('<Button-1>', self.searchStudentScore)
        self.tk_tabs_content.tk_tabs_content_3.tk_button_update_stu_password.bind('<Button-1>',
                                                                                  self.updateStudentPassword)
        self.tk_button_logout.bind('<Button-1>', self.logout_user)

