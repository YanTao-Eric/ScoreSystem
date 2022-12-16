from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import *

import openpyxl as openpyxl

import AddCoursePage
import ClassGradeAnalysis
import ComprehensivePerformanceEvaluation
import CourseScoreAnalysis
import Dao
import DeleteCoursePage
import Login
import UpdateCoursePage

import AddStudentPage
import DeleteStudentPage
import UpdateStudentPage

import numpy as np
import matplotlib.pyplot as plt

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_title = self.__tk_label_title()
        self.tk_label_current_user = self.__tk_label_current_user()
        self.tk_tabs_content = Frame_content(self)
        self.tk_button_logout_user = self.__tk_button_logout_user()

    def __win(self):
        self.title("教师端")
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

    def __tk_button_logout_user(self):
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
        self.add(self.tk_tabs_content_1, text="学生查询")

        self.tk_tabs_content_2 = Frame_content_2(self)
        self.add(self.tk_tabs_content_2, text="成绩查询")

        self.tk_tabs_content_3 = Frame_content_3(self)
        self.add(self.tk_tabs_content_3, text="成绩分析")

        self.tk_tabs_content_4 = Frame_content_4(self)
        self.add(self.tk_tabs_content_4, text="修改密码")

        self.tk_tabs_content_5 = Frame_content_5(self)
        self.add(self.tk_tabs_content_5, text="课程管理")

        self.place(x=0, y=100, width=1000, height=500)


class Frame_content_0(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_tea_number = self.__tk_label_tea_number()
        self.tk_input_tea_number = self.__tk_input_tea_number()
        self.tk_label_tea_name = self.__tk_label_tea_name()
        self.tk_input_tea_name = self.__tk_input_tea_name()
        self.tk_label_tea_gender = self.__tk_label_tea_gender()
        self.tk_select_tea_gender = self.__tk_select_tea_gender()
        self.tk_label_tea_identity = self.__tk_label_tea_identity()
        self.tk_input_tea_identity = self.__tk_input_tea_identity()
        self.tk_label_tea_email = self.__tk_label_tea_email()
        self.tk_input_tea_email = self.__tk_input_tea_email()
        self.tk_button_tea_update = self.__tk_button_tea_update()
        self.tk_button_tea_reset = self.__tk_button_tea_reset()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_label_tea_number(self):
        label = Label(self, text="工号", anchor="e")
        label.place(x=360, y=40, width=100, height=30)
        return label

    def __tk_input_tea_number(self):
        self.tea_number = StringVar(self)
        ipt = Entry(self,  text=self.tea_number)
        ipt.place(x=490, y=40, width=150, height=30)
        ipt.config(stat='disable')
        return ipt

    def __tk_label_tea_name(self):
        label = Label(self, text="姓名", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_tea_name(self):
        self.tea_name = StringVar(self)
        ipt = Entry(self,  text=self.tea_name)
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_tea_gender(self):
        label = Label(self, text="性别", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_select_tea_gender(self):
        cb = Combobox(self, state='readonly')
        cb['values'] = ("男", "女")
        cb.place(x=490, y=180, width=150, height=30)
        return cb

    def __tk_label_tea_identity(self):
        label = Label(self, text="身份证号", anchor="e")
        label.place(x=360, y=250, width=100, height=30)
        return label

    def __tk_input_tea_identity(self):
        self.tea_identify = StringVar(self)
        ipt = Entry(self,  text=self.tea_identify)
        ipt.place(x=490, y=250, width=150, height=30)
        return ipt

    def __tk_label_tea_email(self):
        label = Label(self, text="电子邮箱", anchor="e")
        label.place(x=360, y=320, width=100, height=30)
        return label

    def __tk_input_tea_email(self):
        self.tea_email = StringVar(self)
        ipt = Entry(self,  text=self.tea_email)
        ipt.place(x=490, y=320, width=150, height=30)
        return ipt

    def __tk_button_tea_update(self):
        btn = Button(self, text="修改")
        btn.place(x=400, y=390, width=80, height=30)
        return btn

    def __tk_button_tea_reset(self):
        btn = Button(self, text="重置")
        btn.place(x=520, y=390, width=80, height=30)
        return btn


class Frame_content_1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_table_student_query = self.__tk_table_student_query()
        self.tk_input_stu_name = self.__tk_input_stu_name()
        self.tk_select_box_stu_gender = self.__tk_select_box_stu_gender()
        self.tk_button_stu_search = self.__tk_button_stu_search()
        self.tk_button_addStudent = self.__tk_button_addStudent()
        self.tk_button_delete_student = self.__tk_button_delete_student()
        self.tk_button_stu_refresh = self.__tk_button_stu_refresh()
        self.tk_button_studentinfo_export = self.__tk_button_studentinfo_export()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_table_student_query(self):
        # 表头字段 表头宽度
        self.tk_table_student_manage_columns = {"ID": 50, "学号": 100, "姓名": 150, '性别': 100, '身份证号': 300, '班级': 100, '邮箱': 200}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(self.tk_table_student_manage_columns))
        for text, width in self.tk_table_student_manage_columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        # 插入数据示例
        # data = [
        #     [1, "github", "https://github.com/iamxcd/tkinter-helper"],
        #     [2, "演示地址", "https://www.pytk.net/tkinter-helper"]
        # ]
        #
        # # 导入初始数据
        self.tk_student_table_dataset = Dao.getAllStudents()
        if self.tk_student_table_dataset.get("code") == 0:
            if self.tk_student_table_dataset.get("data"):
                print(self.tk_student_table_dataset.get("data"))
                for values in self.tk_student_table_dataset.get("data"):
                    tk_table.insert('', END, values=list(values.values()))
            else:
                print("未查询到数据！")
        else:
            print("数据查询异常！")

        tk_table.place(x=0, y=60, width=1000, height=415)
        return tk_table

    def __tk_input_stu_name(self):
        ipt = Entry(self)
        ipt.place(x=360, y=10, width=150, height=30)
        return ipt

    def __tk_select_box_stu_gender(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("请选择性别", "男", "女")
        cb.place(x=540, y=10, width=150, height=30)
        cb.current(0)
        return cb

    def __tk_button_stu_search(self):
        btn = Button(self, text="搜索")
        btn.place(x=720, y=10, width=70, height=30)
        return btn

    def __tk_button_stu_refresh(self):
        btn = Button(self, text="刷新")
        btn.place(x=820, y=10, width=70, height=30)
        return btn

    def __tk_button_addStudent(self):
        btn = Button(self, text="添加学生")
        btn.place(x=50, y=10, width=100, height=30)
        return btn

    def __tk_button_delete_student(self):
        btn = Button(self, text="删除学生")
        btn.place(x=180, y=10, width=100, height=30)
        return btn

    def __tk_button_studentinfo_export(self):
        btn = Button(self, text="导出")
        btn.place(x=920, y=10, width=50, height=30)
        return btn


class Frame_content_2(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_table_stu_score = self.__tk_table_stu_score()
        self.tk_input_stu_name_score = self.__tk_input_stu_name_score()
        self.tk_select_box_stu_major_course = self.__tk_select_box_stu_major_course()
        self.tk_button_stu_score_search = self.__tk_button_stu_score_search()
        self.tk_button_add_score = self.__tk_button_add_score()
        self.tk_button_delete_score = self.__tk_button_delete_score()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_table_stu_score(self):
        # 表头字段 表头宽度
        columns = {"ID": 200, "字段#1": 300, "字段#2": 500}
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

        tk_table.place(x=0, y=60, width=1000, height=415)
        return tk_table

    def __tk_input_stu_name_score(self):
        ipt = Entry(self)
        ipt.place(x=360, y=10, width=150, height=30)
        return ipt

    def __tk_select_box_stu_major_course(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("Java", "Python", "C++")
        cb.place(x=540, y=10, width=150, height=30)
        return cb

    def __tk_button_stu_score_search(self):
        btn = Button(self, text="搜索")
        btn.place(x=720, y=10, width=100, height=30)
        return btn

    def __tk_button_add_score(self):
        btn = Button(self, text="添加成绩")
        btn.place(x=50, y=10, width=100, height=30)
        return btn

    def __tk_button_delete_score(self):
        btn = Button(self, text="删除成绩")
        btn.place(x=180, y=10, width=100, height=30)
        return btn


class Frame_content_3(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_button_pieChart = self.__tk_button_pieChart()
        self.tk_button_columnChart = self.__tk_button_columnChart()
        self.tk_button_paratacticColumnChart = self.__tk_button_paratacticColumnChart()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_button_columnChart(self):
        btn = Button(self, text="课程成绩分析")
        btn.place(x=80, y=50, width=150, height=70)
        return btn

    def __tk_button_paratacticColumnChart(self):
        btn = Button(self, text="班级成绩分析")
        btn.place(x=420, y=50, width=150, height=70)
        return btn

    def __tk_button_pieChart(self):
        btn = Button(self, text="综合成绩评定")
        btn.place(x=760, y=50, width=150, height=70)
        return btn


class Frame_content_4(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_original_pwd = self.__tk_label_original_pwd()
        self.tk_input_original_pwd = self.__tk_input_original_pwd()
        self.tk_label_new_pwd = self.__tk_label_new_pwd()
        self.tk_input_new_pwd = self.__tk_input_new_pwd()
        self.tk_label_confirm_pwd = self.__tk_label_confirm_pwd()
        self.tk_input_confirm_pwd = self.__tk_input_confirm_pwd()
        self.tk_button_update_tea_pwd = self.__tk_button_update_tea_pwd()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_label_original_pwd(self):
        label = Label(self, text="原密码", anchor="e")
        label.place(x=360, y=40, width=100, height=30)
        return label

    def __tk_input_original_pwd(self):
        ipt = Entry(self, show='*')
        ipt.place(x=490, y=40, width=150, height=30)
        return ipt

    def __tk_label_new_pwd(self):
        label = Label(self, text="新密码", anchor="e")
        label.place(x=360, y=110, width=100, height=30)
        return label

    def __tk_input_new_pwd(self):
        ipt = Entry(self, show='*')
        ipt.place(x=490, y=110, width=150, height=30)
        return ipt

    def __tk_label_confirm_pwd(self):
        label = Label(self, text="确认密码", anchor="e")
        label.place(x=360, y=180, width=100, height=30)
        return label

    def __tk_input_confirm_pwd(self):
        ipt = Entry(self, show='*')
        ipt.place(x=490, y=180, width=150, height=30)
        return ipt

    def __tk_button_update_tea_pwd(self):
        btn = Button(self, text="修改")
        btn.place(x=450, y=260, width=100, height=30)
        return btn


class Frame_content_5(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()
        self.tk_table_course_manage = self.__tk_table_course_manage()
        self.tk_button_add_course = self.__tk_button_add_course()
        self.tk_button_delete_course = self.__tk_button_delete_course()
        self.tk_select_box_course_department = self.__tk_select_box_course_department()
        self.tk_select_box_course_exam_method = self.__tk_select_box_course_exam_method()
        self.tk_button_course_search = self.__tk_button_course_search()
        self.tk_button_course_export = self.__tk_button_course_export()

    def __frame(self):
        self.place(x=0, y=100, width=1000, height=500)

    def __tk_table_course_manage(self):
        # 表头字段 表头宽度
        self.tk_table_course_manage_columns = {"课程号": 100, "课程名称": 200, "学分": 100, "课程性质": 200, "开课学院": 300, "考试方式": 100}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(self.tk_table_course_manage_columns))
        for text, width in self.tk_table_course_manage_columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        # 插入数据示例
        self.tk_course_table_dataset = Dao.getAllCourses()
        # 导入初始数据
        if self.tk_course_table_dataset.get("code") == 0 and self.tk_course_table_dataset.get("data"):
            for data in self.tk_course_table_dataset.get("data"):
                tk_table.insert('', END, values=list(data.values()))

        tk_table.place(x=0, y=60, width=1000, height=415)
        return tk_table

    def __tk_button_add_course(self):
        btn = Button(self, text="添加课程")
        btn.place(x=50, y=10, width=100, height=30)
        return btn

    def __tk_button_delete_course(self):
        btn = Button(self, text="删除课程")
        btn.place(x=180, y=10, width=100, height=30)
        return btn

    def __tk_select_box_course_department(self):
        cb = Combobox(self, state="readonly")
        values = ["请选择开课学院"]
        for i in Dao.getAllDepartments().get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=310, y=10, width=150, height=30)
        return cb

    def __tk_select_box_course_exam_method(self):
        cb = Combobox(self, state="readonly")
        values = ["请选择考试方式"]
        for i in Dao.getDataDictByType("exammethod").get("data"):
            values.append(i.get("v"))
        cb['values'] = values
        cb.current(0)
        cb.place(x=490, y=10, width=150, height=30)
        return cb

    def __tk_button_course_search(self):
        btn = Button(self, text="搜索")
        btn.place(x=670, y=10, width=100, height=30)
        return btn

    def __tk_button_course_export(self):
        btn = Button(self, text="导出")
        btn.place(x=800, y=10, width=100, height=30)
        return btn


class Win(WinGUI):
    def __init__(self, current_user):
        super().__init__()
        self.__event_bind()
        self.current_user = current_user
        self.uid = current_user.get("uid")
        self.tk_label_current_user['text'] = "当前用户：" + current_user.get("uname")
        self.tk_tabs_content.tk_tabs_content_0.tea_number.set(current_user.get("uid"))
        self.tk_tabs_content.tk_tabs_content_0.tea_name.set(current_user.get("uname"))
        self.tk_tabs_content.tk_tabs_content_0.tk_select_tea_gender.current(0 if current_user.get("ugender") == '男' else 1)
        self.tk_tabs_content.tk_tabs_content_0.tea_identify.set(current_user.get("uidentify"))
        self.tk_tabs_content.tk_tabs_content_0.tea_email.set(current_user.get("uemail"))

    def logout(self):
        try:
            self.updateStudent.destroy()
            self.addInfo.destroy()
            self.delete.destroy()
        except Exception as e:
            print(e)
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()

    def updateStudentInfo(self, evt):
        current_focus = self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.focus()
        current_studentinfo = self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.set(current_focus)
        current_uid = current_studentinfo.get('学号')
        self.updateStudent = UpdateStudentPage.Win(current_uid)
        self.updateStudent.mainloop()
        print("<<TreeviewSelect>>事件未处理", evt)

    def updateTeacherInfo(self, evt):
        __tea_name = self.tk_tabs_content.tk_tabs_content_0.tk_input_tea_name.get()
        __tea_gender = self.tk_tabs_content.tk_tabs_content_0.tk_select_tea_gender.get()
        __tea_identify = self.tk_tabs_content.tk_tabs_content_0.tk_input_tea_identity.get()
        __tea_email = self.tk_tabs_content.tk_tabs_content_0.tk_input_tea_email.get()
        if not __tea_name or not __tea_gender or not __tea_identify or not __tea_email:
            messagebox.showinfo("提示", "必填项不能为空！")
            return
        if not re.match(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',
                        __tea_identify):
            messagebox.showinfo("提示", "身份证格式不合法！")
            return
        if not re.match(r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$', __tea_email):
            messagebox.showinfo("提示", "电子邮箱格式不合法！")
            return
        res = Dao.updateUser(self.uid, __tea_name, __tea_gender, __tea_identify, 0, __tea_email)
        messagebox.showinfo("提示", res.get("msg"))
        print("更新学生信息", evt)

    def resetTeacherInfo(self, evt):
        self.tk_tabs_content.tk_tabs_content_0.tea_name.set(self.current_user.get("uname"))
        self.tk_tabs_content.tk_tabs_content_0.tk_select_tea_gender.current(0 if self.current_user.get("ugender") == '男' else 1)
        self.tk_tabs_content.tk_tabs_content_0.tea_identify.set(self.current_user.get("uidentify"))
        self.tk_tabs_content.tk_tabs_content_0.tea_email.set(self.current_user.get("uemail"))
        print("重置教师信息", evt)

    def searchStudentInfo(self, evt):
        print("<Button-1>事件未处理", evt)

    def updateStudentScore(self, evt):
        print("<<TreeviewSelect>>事件未处理", evt)

    def searchStuScore(self, evt):
        print("<Button-1>事件未处理", evt)

    def addStudentInfo(self, evt):
        self.addInfo = AddStudentPage.Win()
        self.addInfo.mainloop()
        print("<Button-1>事件未处理", evt)

    def deleteStudentInfo(self, evt):
        self.delete = DeleteStudentPage.Win()
        self.delete.mainloop()
        print("<Button-1>事件未处理", evt)

    def addStudentScore(self, evt):
        print("<Button-1>事件未处理", evt)

    def deleteStudentScore(self, evt):
        print("<Button-1>事件未处理", evt)

    def updateTeacherPassword(self, evt):
        __original_pwd = self.tk_tabs_content.tk_tabs_content_4.tk_input_original_pwd.get()
        __new_pwd = self.tk_tabs_content.tk_tabs_content_4.tk_input_new_pwd.get()
        __confirm_pwd = self.tk_tabs_content.tk_tabs_content_4.tk_input_confirm_pwd.get()
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
        print("修改教师密码", evt)

    def addCourseInfo(self, evt):
        addCoursePage = AddCoursePage.Win()
        addCoursePage.mainloop()
        print("添加成绩！")

    def deleteCourseInfo(self, evt):
        deleteCoursePage = DeleteCoursePage.Win()
        deleteCoursePage.mainloop()
        print("删除课程！")

    def searchCourseInfo(self, evt):
        __course_manage = self.tk_tabs_content.tk_tabs_content_5
        __department = __course_manage.tk_select_box_course_department.get()
        __exammethod = __course_manage.tk_select_box_course_exam_method.get()
        if __course_manage.tk_select_box_course_department.current() == 0:
            __department = ''
        if __course_manage.tk_select_box_course_exam_method.current() == 0:
            __exammethod = ''
        for _ in map(__course_manage.tk_table_course_manage.delete, __course_manage.tk_table_course_manage.get_children("")):
            pass
        self.tk_tabs_content.tk_tabs_content_5.tk_course_table_dataset = Dao.searchCourses(__department, __exammethod)
        # 导入初始数据
        if self.tk_tabs_content.tk_tabs_content_5.tk_course_table_dataset.get("code") == 0 and self.tk_tabs_content.tk_tabs_content_5.tk_course_table_dataset.get("data"):
            for data in self.tk_tabs_content.tk_tabs_content_5.tk_course_table_dataset.get("data"):
                __course_manage.tk_table_course_manage.insert('', END, values=list(data.values()))
        __course_manage.tk_select_box_course_department.current(0)
        __course_manage.tk_select_box_course_exam_method.current(0)
        print("查询课程！")

    def updateCourseInfo(self, evt):
        __focus = self.tk_tabs_content.tk_tabs_content_5.tk_table_course_manage.focus()
        current_item = self.tk_tabs_content.tk_tabs_content_5.tk_table_course_manage.set(__focus)
        __cid = current_item.get("课程号")
        self.updateCoursePage = UpdateCoursePage.Win(__cid)
        self.updateCoursePage.mainloop()
        print("更新课程信息！")

    def exportCourseInfo(self, evt):
        path = filedialog.askdirectory()
        try:
            book = openpyxl.Workbook()
            sheet = book.active
            fff = list(self.tk_tabs_content.tk_tabs_content_5.tk_table_course_manage_columns.keys())  # 获取表头信息
            sheet.append(fff)
            dataset = [list(data_item.values()) for data_item in self.tk_tabs_content.tk_tabs_content_5.tk_course_table_dataset.get("data")]
            print(dataset)
            for i in dataset:
                sheet.append(i)
            book.save(path + "/course_info.xlsx")
            messagebox.showinfo("提示", "导出成功！")
        except Exception as e:
            messagebox.showinfo("提示", "导出失败！")
            print(e)

    def logout_user(self, evt):
        messagebox.showwarning('提示', '欢迎下次使用！')
        self.destroy()

    def studentinfo_refresh(self, evt):
        # 删除原结点，加入新结点
        for _ in map(self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.delete,
                     self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.get_children("")):
            pass
        result = Dao.getAllStudents()
        if result.get("code") == 0:
            if result.get("data"):
                # print(result.get("data"))
                for values in result.get("data"):
                    self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.insert('', END,
                                                                                         values=list(values.values()))
            else:
                print("未查询到数据！")
        else:
            print("数据查询异常！")

    def studentinfo_search(self, evt):
        for _ in map(self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.delete,
                     self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.get_children("")):
            pass
        value = self.tk_tabs_content.tk_tabs_content_1.tk_input_stu_name.get()
        num = self.tk_tabs_content.tk_tabs_content_1.tk_select_box_stu_gender.get()
        print(num, value)
        if num == '请选择性别':
            result = Dao.searchStudents(value, '')
        else:
            result = Dao.searchStudents(value, num)
        if result.get("code") == 0:
            if result.get("data"):
                # print(result.get("data"))
                for values in result.get("data"):
                    self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.insert('', END, values=list(values.values()))
            else:
                print("未查询到数据！")
        else:
            print("数据查询异常！")

    def studentinfo_export(self, evt):
        path = filedialog.askdirectory()
        try:
            book = openpyxl.Workbook()
            sheet = book.active
            fff = list(self.tk_tabs_content.tk_tabs_content_1.tk_table_student_manage_columns.keys())  # 获取表头信息
            sheet.append(fff)
            dataset = [list(data_item.values()) for data_item in
                       self.tk_tabs_content.tk_tabs_content_1.tk_student_table_dataset.get("data")]
            print(dataset)
            for i in dataset:
                sheet.append(i)
            book.save(path + "/student_info.xlsx")
            messagebox.showinfo("提示", "导出成功！")
        except Exception as e:
            messagebox.showinfo("提示", "导出失败！")
            print(e)

    def columnChart(self, evt):
        courseScoreAnalysis = CourseScoreAnalysis.Win()
        courseScoreAnalysis.mainloop()
        pass

    def paratacticColumnChart(self, evt):
        classGradeAnalysis = ClassGradeAnalysis.Win()
        classGradeAnalysis.mainloop()
        pass

    def pieChart(self, evt):
        comprehensivePerformanceEvaluation = ComprehensivePerformanceEvaluation.Win()
        comprehensivePerformanceEvaluation.mainloop()
        pass


    def __event_bind(self):
        self.protocol('WM_DELETE_WINDOW', self.logout)
        self.tk_tabs_content.tk_tabs_content_1.tk_table_student_query.bind('<<TreeviewSelect>>', self.updateStudentInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_tea_update.bind('<Button-1>', self.updateTeacherInfo)
        self.tk_tabs_content.tk_tabs_content_0.tk_button_tea_reset.bind('<Button-1>', self.resetTeacherInfo)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_stu_search.bind('<Button-1>', self.searchStudentInfo)
        self.tk_tabs_content.tk_tabs_content_2.tk_table_stu_score.bind('<<TreeviewSelect>>', self.updateStudentScore)
        self.tk_tabs_content.tk_tabs_content_2.tk_button_stu_score_search.bind('<Button-1>', self.searchStuScore)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_addStudent.bind('<Button-1>', self.addStudentInfo)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_delete_student.bind('<Button-1>', self.deleteStudentInfo)
        self.tk_tabs_content.tk_tabs_content_2.tk_button_add_score.bind('<Button-1>', self.addStudentScore)
        self.tk_tabs_content.tk_tabs_content_2.tk_button_delete_score.bind('<Button-1>', self.deleteStudentScore)

        self.tk_tabs_content.tk_tabs_content_3.tk_button_columnChart.bind('<Button-1>', self.columnChart)
        self.tk_tabs_content.tk_tabs_content_3.tk_button_paratacticColumnChart.bind('<Button-1>', self.paratacticColumnChart)
        self.tk_tabs_content.tk_tabs_content_3.tk_button_pieChart.bind('<Button-1>', self.pieChart)

        self.tk_tabs_content.tk_tabs_content_4.tk_button_update_tea_pwd.bind('<Button-1>', self.updateTeacherPassword)
        self.tk_tabs_content.tk_tabs_content_5.tk_button_add_course.bind('<Button-1>', self.addCourseInfo)
        self.tk_tabs_content.tk_tabs_content_5.tk_button_delete_course.bind('<Button-1>', self.deleteCourseInfo)
        self.tk_tabs_content.tk_tabs_content_5.tk_button_course_search.bind('<Button-1>', self.searchCourseInfo)
        self.tk_tabs_content.tk_tabs_content_5.tk_button_course_export.bind('<Button-1>', self.exportCourseInfo)
        self.tk_tabs_content.tk_tabs_content_5.tk_table_course_manage.bind('<<TreeviewSelect>>', self.updateCourseInfo)
        self.tk_button_logout_user.bind('<Button-1>', self.logout_user)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_stu_refresh.bind('<Button-1>', self.studentinfo_refresh)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_stu_search.bind('<Button-1>', self.studentinfo_search)
        self.tk_tabs_content.tk_tabs_content_1.tk_button_studentinfo_export.bind('<Button-1>', self.studentinfo_export)
