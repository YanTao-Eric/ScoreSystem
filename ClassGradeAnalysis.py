from tkinter import *
from tkinter.ttk import *

import numpy as np
from matplotlib import pyplot as plt

import Dao


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_sure = self.__tk_button_sure()
        self.tk_select_box_classSelect = self.__tk_select_box_classSelect()

    def __win(self):
        self.title("班级成绩分析")
        # 设置窗口大小、居中
        width = 261
        height = 262
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_button_sure(self):
        btn = Button(self, text="确定")
        btn.place(x=200, y=20, width=50, height=24)
        return btn

    def __tk_select_box_classSelect(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = [i.get("uclid") for i in Dao.getAllClasses().get("data")]
        cb.current(0)
        cb.place(x=10, y=20, width=173, height=25)
        return cb


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        return menu

    def sureSelect(self, evt):
        value = self.tk_select_box_classSelect.get()
        result = Dao.getMaxAndMinAndAvgScoreByCLid(value).get("data")
        plt.title('{} 班学生各个科目的最高分、最低分、平均分'.format(value))
        # 每个课程的的最高分数
        max = [i.get("max_score") for i in result]
        # 每个课程的最小分数
        min = [i.get("min_score") for i in result]
        # 每个课程的平均分
        avg = [i.get("avg_score") for i in result]
        # 设置x轴数据
        x = np.arange(len(max))
        # 每组数据n有3个类型
        total_width, n = 0.6, 3
        width = total_width / n
        x = x - (total_width - width) / 2
        plt.bar(x, max, color="b", width=width, label='max')
        plt.bar(x + width, min, color="r", width=width, label='min')
        plt.bar(x + 2 * width, avg, color="gray", width=width, label='avg')
        # x和y轴标题
        plt.xlabel("课程")
        plt.ylabel("分数")
        plt.legend(loc="best")
        # x轴命名
        plt.xticks([i for i in range(len(max))], [i.get("cname") for i in result])
        plt.ylim((0, 100))
        # 设置纵轴起始,终止和间距
        my_y_ticks = np.arange(0, 100, 10)
        plt.yticks(my_y_ticks)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文显示
        plt.show()

    def __event_bind(self):
        self.tk_button_sure.bind('<Button-1>', self.sureSelect)


if __name__ == "__main__":
    win = Win()
    win.mainloop()