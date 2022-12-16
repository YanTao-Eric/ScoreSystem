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
        self.title("综合成绩评定")
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
        cb['values'] =[i.get("uclid") for i in Dao.getAllClasses().get("data")]
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
        result = Dao.getOverallGradeLevelByCLid(value).get("data")
        fig = plt.figure(figsize=(8, 8))
        a = fig.add_subplot(111)
        a.set_title('{} 班综合成绩评定'.format(value))
        labels = '优秀', '良好', '及格', '不及格'
        sizes = np.array(list(result[0].values()))
        # 设置分离的距离，0表示不分离
        explode = (0.1, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文
        plt.show()

    def __event_bind(self):
        self.tk_button_sure.bind('<Button-1>', self.sureSelect)


if __name__ == "__main__":
    win = Win()
    win.mainloop()