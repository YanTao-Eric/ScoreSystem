from tkinter import *
from tkinter.ttk import *

import Dao
import numpy as np
import matplotlib.pyplot as plt

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_select_box_select = self.__tk_select_box_select()
        self.tk_button_sure = self.__tk_button_sure()

    def __win(self):
        self.title("课程成绩分析")
        # 设置窗口大小、居中
        width = 261
        height = 262
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_select_box_select(self):
        cb = Combobox(self, state="readonly")

        cb['values'] = [i.get("cname") for i in Dao.getAllCourses().get("data")]
        cb.current(0)
        cb.place(x=10, y=20, width=173, height=30)
        return cb

    def __tk_button_sure(self):
        btn = Button(self, text="确定")
        btn.place(x=200, y=20, width=50, height=30)
        return btn


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def sureSelect(self, evt):
        value = self.tk_select_box_select.get()
        result = Dao.getScoreBandByCName(value).get("data")
        x = np.array(["90-100", "80-89", "70-79", "60-69", "0-59"])
        y = np.array(list(result[0].values()))
        y_pos = np.arange(len(x))
        plt.xlabel("分数区间")
        plt.ylabel("人数")
        # x轴标签
        plt.xticks(y_pos, x)
        # 创建条形图
        plt.bar(x, y, color=["blue", "blue", "blue", "blue", "red"])
        plt.title('{} 成绩'.format(value))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文显示

        self.destroy()
        # 显示
        plt.show()

    def __event_bind(self):
        self.tk_button_sure.bind('<Button-1>', self.sureSelect)

