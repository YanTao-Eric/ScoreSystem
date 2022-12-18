from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import *

import numpy as np
import openpyxl
from matplotlib import pyplot as plt

import Dao
import Login

global current_uid

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
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
        self.tk_label_stu_gender = self.__tk_label_stu_gender()
        self.tk_tk_select_stu_gender = self.__tk_select_stu_gender()
        self.tk_label_stu_identity = self.__tk_label_stu_identity()
        self.tk_input_stu_identity = self.__tk_input_stu_identity()
        self.tk_label_stu_email = self.__tk_label_stu_email()
        self.tk_input_stu_email = self.__tk_input_stu_email()
        self.tk_button_stu_update = self.__tk_button_stu_update()
        self.tk_button_stu_reset = self.__tk_button_stu_reset()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_label_stu_number(self):
        label = Label(self, text="学号", anchor="e")
        label.place(x=360, y=40, width=100, height=30)
        return label

    def __tk_input_stu_number(self):
        self.student_number = StringVar(self)
        ipt = Entry(self, text=self.student_number)
        ipt.place(x=490, y=40, width=150, height=30)
        ipt.config(stat='disable')
        return ipt

    def __tk_label_stu_name(self):
        label = Label(self, text="姓名", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_stu_name(self):
        self.student_name = StringVar(self)
        ipt = Entry(self, text=self.student_name)
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_stu_gender(self):
        label = Label(self, text="性别", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_select_stu_gender(self):
        cb = Combobox(self, state='readonly')
        cb['values'] = ("男", "女")
        cb.place(x=490, y=180, width=150, height=30)
        return cb

    def __tk_label_stu_identity(self):
        label = Label(self, text="身份证号", anchor="e")
        label.place(x=360, y=250, width=100, height=30)
        return label

    def __tk_input_stu_identity(self):
        self.student_identify = StringVar(self)
        ipt = Entry(self, text=self.student_identify)
        ipt.place(x=490, y=250, width=150, height=30)
        return ipt

    def __tk_label_stu_email(self):
        label = Label(self, text="电子邮箱", anchor="e")
        label.place(x=360, y=320, width=100, height=30)
        return label

    def __tk_input_stu_email(self):
        self.student_email = StringVar(self)
        ipt = Entry(self, text=self.student_email)
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
        self.tk_button_analysis = self.__tk_button_analysis()
        self.tk_table_stu_score = self.__tk_table_stu_score()
        self.tk_select_box_course_nature = self.__tk_select_box_course_nature()
        self.tk_select_box_course_department = self.__tk_select_box_course_department()
        self.tk_select_box_exam_method = self.__tk_select_box_exam_method()
        self.tk_button_search = self.__tk_button_search()
        self.tk_button_export = self.__tk_button_export()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_table_stu_score(self):
        # 表头字段 表头宽度
        self.tk_table_stu_score_columns = {"#": 50, "课程名称": 200, "课程性质": 150, "开课学院": 300, "考试方式": 100, "学分": 100, "成绩": 100}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(self.tk_table_stu_score_columns))
        for text, width in self.tk_table_stu_score_columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        # 插入数据示例
        # self.tk_score_table_dataset = Dao.getScoreByUid(8888)
        # # 导入初始数据
        # if self.tk_score_table_dataset.get("code") == 0 and self.tk_score_table_dataset.get("data"):
        #     for data in self.tk_score_table_dataset.get("data"):
        #         tk_table.insert('', END, values=list(data.values()))

        tk_table.place(x=0, y=55, width=1000, height=420)
        return tk_table

    def __tk_button_analysis(self):
        btn = Button(self, text="分析")
        btn.place(x=65, y=10, width=75, height=30)
        return btn

    def __tk_select_box_course_nature(self):
        cb = Combobox(self, state="readonly")
        values = ["请选择课程性质"]
        for i in Dao.getDataDictByType("nature").get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=180, y=10, width=150, height=30)
        return cb

    def __tk_select_box_course_department(self):
        cb = Combobox(self, state="readonly")
        values = ["请选择开课学院"]
        for i in Dao.getAllDepartments().get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=370, y=10, width=150, height=30)
        return cb

    def __tk_select_box_exam_method(self):
        cb = Combobox(self, state="readonly")
        values = ["请选择考试方式"]
        for i in Dao.getDataDictByType("exammethod").get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=560, y=10, width=150, height=30)
        return cb

    def __tk_button_search(self):
        btn = Button(self, text="搜索")
        btn.place(x=750, y=10, width=75, height=30)
        return btn

    def __tk_button_export(self):
        btn = Button(self, text="导出")
        btn.place(x=840, y=10, width=75, height=30)
        return btn


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
        ipt = Entry(self, show='*')
        ipt.place(x=490, y=40, width=150, height=30)
        return ipt

    def __tk_label_new_password(self):
        label = Label(self, text="新密码", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_new_password(self):
        ipt = Entry(self, show='*')
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_confirm_password(self):
        label = Label(self, text="确认密码", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_input_confirm_password(self):
        ipt = Entry(self, show='*')
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
        self.uid = current_user.get("uid")
        self.uclid = current_user.get("uclid")
        self.tk_label_current_user['text'] = "当前用户：" + current_user.get("uname")
        self.tk_tabs_content.tk_tabs_content_0.student_number.set(current_user.get("uid"))
        self.tk_tabs_content.tk_tabs_content_0.student_name.set(current_user.get("uname"))
        self.tk_tabs_content.tk_tabs_content_0.tk_tk_select_stu_gender.current(0 if current_user.get("ugender") == '男' else 1)
        self.tk_tabs_content.tk_tabs_content_0.student_identify.set(current_user.get("uidentify"))
        self.tk_tabs_content.tk_tabs_content_0.student_email.set(current_user.get("uemail"))

        # 插入数据示例
        self.score_table_dataset = Dao.getScoreByUid(self.uid)
        # 导入初始数据
        if self.score_table_dataset.get("code") == 0 and self.score_table_dataset.get("data"):
            for data in self.score_table_dataset.get("data"):
                self.tk_tabs_content.tk_tabs_content_1.tk_table_stu_score.insert('', END, values=list(data.values()))

    def logout(self):
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()
        login = Login.Win()
        login.mainloop()

    def updateStudentInfo(self, evt):
        __stu_name = self.tk_tabs_content.tk_tabs_content_0.tk_input_stu_name.get()
        __stu_gender = self.tk_tabs_content.tk_tabs_content_0.tk_tk_select_stu_gender.get()
        __stu_identify = self.tk_tabs_content.tk_tabs_content_0.tk_input_stu_identity.get()
        __stu_email = self.tk_tabs_content.tk_tabs_content_0.tk_input_stu_email.get()
        if not __stu_name or not __stu_gender or not __stu_identify or not __stu_email:
            messagebox.showinfo("提示", "必填项不能为空！")
            return
        if not re.match(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', __stu_identify):
            messagebox.showinfo("提示", "身份证格式不合法！")
            return
        if not re.match(r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$', __stu_email):
            messagebox.showinfo("提示", "电子邮箱格式不合法！")
            return
        res = Dao.updateUser(self.uid, __stu_name, __stu_gender, __stu_identify, self.uclid, __stu_email)
        messagebox.showinfo("提示", res.get("msg"))
        self.tk_label_current_user['text'] = "当前用户：" + __stu_name
        print("更新学生信息", evt)

    def stu_reset(self, evt):
        self.tk_tabs_content.tk_tabs_content_0.student_number.set(self.userInfo[0])
        self.tk_tabs_content.tk_tabs_content_0.student_name.set(self.userInfo[1])
        self.tk_tabs_content.tk_tabs_content_0.tk_tk_select_stu_gender.current(0 if self.userInfo[2] else 1)
        self.tk_tabs_content.tk_tabs_content_0.student_identify.set(self.userInfo[3])
        self.tk_tabs_content.tk_tabs_content_0.student_email.set(self.userInfo[5])

    def analysisStudentScore(self, evt):
        result = Dao.getScoreByUid(self.uid).get("data")
        plt.title('成绩统计图')
        # 设置x轴数据
        x = [i.get("cname") for i in result]
        # 每组数据n有3个类型
        total_width, n = 0.6, 3
        width = total_width / n
        y1 = [i.get("score") for i in result]
        y2 = [i.get("avg_score") for i in Dao.getAllCourseAvgScore(self.uid).get("data")]
        plt.bar(x, y1, color="b", width=width, label='我的成绩')
        plt.plot(x, y2, color="g", label='科目平均成绩')
        # x和y轴标题
        plt.xlabel("课程")
        plt.ylabel("分数")
        plt.legend(loc="best")
        plt.ylim((0, 100))
        # 设置纵轴起始,终止和间距
        my_y_ticks = np.arange(0, 100, 10)
        plt.yticks(my_y_ticks)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文显示
        plt.show()
        print("成绩分析图表绘制")

    def searchStudentScore(self, evt):
        __score_query = self.tk_tabs_content.tk_tabs_content_1
        __nature = __score_query.tk_select_box_course_nature.get()
        __department = __score_query.tk_select_box_course_department.get()
        __exammethod = __score_query.tk_select_box_exam_method.get()
        if __score_query.tk_select_box_course_nature.current() == 0:
            __nature = ''
        if __score_query.tk_select_box_course_department.current() == 0:
            __department = ''
        if __score_query.tk_select_box_exam_method.current() == 0:
            __exammethod = ''
        for _ in map(__score_query.tk_table_stu_score.delete, __score_query.tk_table_stu_score.get_children("")):
            pass
        self.score_table_dataset = Dao.getScoreByUid(self.uid, __nature, __department, __exammethod)
        # 导入初始数据
        if self.score_table_dataset.get("code") == 0 and self.score_table_dataset.get("data"):
            for data in self.score_table_dataset.get("data"):
                __score_query.tk_table_stu_score.insert('', END, values=list(data.values()))
        __score_query.tk_select_box_course_nature.current(0)
        __score_query.tk_select_box_course_department.current(0)
        __score_query.tk_select_box_exam_method.current(0)
        print(f"查询学生{self.uid}的成绩！")

    def exportStudentScore(self, evt):
        path = filedialog.askdirectory()
        try:
            book = openpyxl.Workbook()
            sheet = book.active
            fff = list(self.tk_tabs_content.tk_tabs_content_1.tk_table_stu_score_columns.keys())  # 获取表头信息
            sheet.append(fff)
            dataset = [list(data_item.values()) for data_item in
                       self.score_table_dataset.get("data")]
            print(dataset)
            for i in dataset:
                sheet.append(i)
            book.save(f"{path}/{self.uid}.xlsx")
            messagebox.showinfo("提示", "导出成功！")
        except Exception as e:
            messagebox.showinfo("提示", "导出失败！")
            print(e)
        print("<Button-1>事件未处理", evt)

    def updateStudentPassword(self, evt):
        __original_pwd = self.tk_tabs_content.tk_tabs_content_3.tk_input_original_password.get()
        __new_pwd = self.tk_tabs_content.tk_tabs_content_3.tk_input_new_password.get()
        __confirm_pwd = self.tk_tabs_content.tk_tabs_content_3.tk_input_confirm_password.get()
        if __original_pwd == '' or __new_pwd == '' or __confirm_pwd == '':
            messagebox.showwarning("提示", "必填项未填写！")
            return
        if not re.match(r"^[0-9a-zA-Z~!@#$%^&*._?]{6,18}$", __original_pwd) \
                or not re.match(r"^[0-9a-zA-Z~!@#$%^&*._?]{6,18}$", __new_pwd) \
                or not re.match(r"^[0-9a-zA-Z~!@#$%^&*._?]{6,18}$", __confirm_pwd):
            messagebox.showwarning("提示", "密码格式应为6-18位数字、字母、特殊字符的组合！")
            return
        if __new_pwd != __confirm_pwd:
            messagebox.showwarning("提示", "两次密码输入不一致")
            return
        res = Dao.updatePassword(self.uid, __original_pwd, __new_pwd)
        messagebox.showinfo("提示", res.get("msg"))
        if res.get("code") == 0:
            self.destroy()
            login = Login.Win()
            login.mainloop()
        print("修改密码", evt)

    def logout_user(self, evt):
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()
        login = Login.Win()
        login.mainloop()

    def __event_bind(self):
        self.protocol('WM_DELETE_WINDOW', self.logout)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_update.bind('<Button-1>', self.updateStudentInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_stu_reset.bind('<Button-1>', self.stu_reset)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_analysis.bind('<Button-1>', self.analysisStudentScore)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_search.bind('<Button-1>', self.searchStudentScore)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_export.bind('<Button-1>', self.exportStudentScore)
        self.tk_tabs_content.tk_tabs_content_3.tk_button_update_stu_password.bind('<Button-1>',
                                                                                  self.updateStudentPassword)
        self.tk_button_logout.bind('<Button-1>', self.logout_user)

