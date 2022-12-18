import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import Dao
import re
import time


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_input_uname = self.__tk_input_uname()
        self.tk_input_uidentify = self.__tk_input_uidentify()
        self.tk_input_uclid = self.__tk_input_uclid()
        self.tk_label_lbkplxeu = self.__tk_label_lbkplxeu()
        self.tk_label_lbkplz5f = self.__tk_label_lbkplz5f()
        self.tk_radio_button_nan = self.__tk_radio_button_nan()
        self.tk_radio_button_nv = self.__tk_radio_button_nv()
        self.tk_button_submitp = self.__tk_button_submitp()
        self.tk_button_reset = self.__tk_button_reset()
        self.tk_label_lbkps8tn = self.__tk_label_lbkps8tn()
        self.tk_label_lbkpsbfq = self.__tk_label_lbkpsbfq()
        self.tk_label_uemail = self.__tk_label_uemail()
        self.tk_input_email = self.__tk_input_email()

    def __win(self):
        self.title("添加学生")
        # 设置窗口大小、居中
        width = 495
        height = 410
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.gender = tkinter.IntVar()

    def __tk_input_uname(self):
        self.uname_value = StringVar(self)
        ipt = Entry(self, text=self.uname_value)
        ipt.place(x=230, y=140, width=150, height=30)
        return ipt

    def __tk_input_uidentify(self):
        self.uidentify_value = StringVar(self)
        ipt = Entry(self, text=self.uidentify_value)
        ipt.place(x=230, y=220, width=150, height=30)
        return ipt

    def __tk_input_uclid(self):
        self.uclid_value = StringVar(self)
        ipt = Entry(self, text=self.uclid_value)
        ipt.place(x=230, y=260, width=150, height=30)
        return ipt

    def __tk_label_lbkplxeu(self):
        label = Label(self, text="性别", anchor="center")
        label.place(x=120, y=180, width=100, height=30)
        return label

    def __tk_label_lbkplz5f(self):
        label = Label(self, text="身份证号:", anchor="center")
        label.place(x=120, y=220, width=100, height=30)
        return label

    def __tk_radio_button_nan(self):
        rb = Radiobutton(self, text="男", variable=self.gender, value=1)
        rb.place(x=240, y=180, width=80, height=24)
        return rb

    def __tk_radio_button_nv(self):
        rb = Radiobutton(self, text="女", variable=self.gender, value=0)
        rb.place(x=320, y=180, width=80, height=24)
        return rb

    def __tk_button_submitp(self):
        btn = Button(self, text="提交")
        btn.place(x=160, y=350, width=72, height=34)
        return btn

    def __tk_button_reset(self):
        btn = Button(self, text="重置")
        btn.place(x=270, y=350, width=72, height=34)
        return btn

    def __tk_label_lbkps8tn(self):
        label = Label(self, text="班级:", anchor="center")
        label.place(x=120, y=260, width=100, height=30)
        return label

    def __tk_label_lbkpsbfq(self):
        label = Label(self, text="姓名:", anchor="center")
        label.place(x=120, y=140, width=100, height=30)
        return label

    def __tk_label_uemail(self):
        label = Label(self, text="邮件:", anchor="center")
        label.place(x=120, y=300, width=100, height=30)
        return label

    def __tk_input_email(self):
        self.email_value = StringVar(self)
        ipt = Entry(self, text=self.email_value)
        ipt.place(x=230, y=300, width=150, height=30)
        return ipt


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def submit(self, evt):
        global idnumber
        flag = 0
        uname = self.tk_input_uname.get()
        print(uname)
        usex = self.gender.get()
        if usex == 1:
            usex = '男'
        else:
            usex = '女'
        print(usex)
        identityId = self.tk_input_uidentify.get()
        uclid = self.tk_input_uclid.get()
        uEmail = self.tk_input_email.get()
        # 检验身份证号码的正确性
        ret = re.match(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',
                       identityId)
        # 检验是否为正确的班级号码
        uclidRet = re.match(r'^[0-9]*$', uclid)
        # 检验邮箱是否正确
        uEmailRet = re.match(r'(^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)', uEmail)
        if ret is None:
            flag = 1
        if uclidRet is None:
            flag = 2
        if uEmailRet is None:
            flag = 3
        if flag == 1:
            messagebox.showerror(title='错误', message='身份证不合法')
        elif flag == 2:
            messagebox.showerror(title='错误', message='请输入正确的班级')
        elif flag == 3:
            messagebox.showerror(title='错误', message='邮件不合法')
        else:
            localtime = time.localtime(time.time())
            if int(uclid) < 10:
                idnumber = str(localtime[0])[2:] + "0" + uclid
            else:
                idnumber = str(localtime[0])[2:] + uclid
            result = Dao.getMaxStuNumber(idnumber)
            if result.get("code") == 0:
                if result.get("data"):
                    if not result.get("data")[0].get('max_id'):
                        idnumber = int(idnumber) * 100
                    else:
                        idnumber = result.get("data")[0].get('max_id')
                    idnumber = idnumber + 1
            if Dao.addStudent(idnumber, uname, usex, identityId, int(uclid), uEmail).get("code") == 0:
                messagebox.showwarning(title='提示', message='插入成功')

    def reset(self, evt):
        self.uname_value.set("")
        self.uidentify_value.set("")
        self.uclid_value.set("")
        self.email_value.set("")
        print("<Button-1>事件未处理", evt)

    def radioNan(self, evt):
        self.gender.set(1)

    def radioNv(self, evt):
        self.gender.set(0)

    def __event_bind(self):
        self.tk_button_submitp.bind('<Button-1>', self.submit)
        self.tk_button_reset.bind('<Button-1>', self.reset)
        self.tk_radio_button_nan.bind('<Button-1>', self.radioNan)
        self.tk_radio_button_nv.bind('<Button-1>', self.radioNv)

