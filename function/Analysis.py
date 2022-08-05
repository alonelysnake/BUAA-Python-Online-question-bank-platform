# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 16:30
# @Author  : Kazeya
# @File    : Analysis.py
# @Description :

from user.User import CUR_USER
from user.User import UserUtil


# 图表绘制模块
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
matplotlib.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

matplotlib.use("Qt5Agg")  # 声明使用QT5


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = None

    # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plot_sin(self):
        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plot_cos(self):
        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plot_2d(self,logs):
        self.axes = self.fig.add_subplot(111)
        times = np.arange(1, len(logs) + 1)
        acc = []
        for log in logs:
            num = log[4].split(',')
            acc.append((log[2] - len(num)) / log[2])
        avg = sum(acc) / len(acc)
        self.axes.plot(times, acc, "go-")
        self.axes.set_xlabel('练习次数')
        self.axes.set_ylabel('正确率')
        self.axes.set_xticks(np.arange(1, len(logs) + 1))
        self.axes.axhline(y=avg, color="gray", ls='--')
        self.axes.legend(labels=('正确率', '平均正确率'))

    def plot_3d(self):
        self.axes = self.fig.add_subplot(111, projection='3d')

        x_edges = np.array([[10, 20], [10, 20], [10, 20], [10, 20],
                            [20, 30], [20, 30], [20, 30], [20, 30],
                            [30, 40], [30, 40], [30, 40], [30, 40],
                            [40, 50], [40, 50], [40, 50], [40, 50]])
        # 设置y轴取值
        y_edges = np.array([[10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50],
                            [10, 20], [20, 30], [30, 40], [40, 50]])

        # 设置X,Y对应点的值。即原始数据。
        hist = np.array([[3.0], [0.0], [8.0], [4.0],
                         [2.0], [4.0], [5.0], [7.0],
                         [9.0], [2.0], [6.0], [3.0],
                         [0.0], [3.0], [1.0], [0.0]])
        color_list = ['skyblue', 'lightgreen', 'bisque', 'gold',
                      'lightgreen', 'bisque', 'gold', 'lightpink',
                      'bisque', 'gold', 'lightpink', 'plum',
                      'gold', 'lightpink', 'plum', 'lightgray']

        for i in range(len(x_edges)):
            # 设置作图点的坐标
            xpos, ypos = np.meshgrid(x_edges[i][:-1] - 2.5, y_edges[i][:-1] - 2.5)
            xpos = xpos.flatten('F')
            ypos = ypos.flatten('F')
            zpos = np.zeros_like(xpos)

            # 设置柱形图大小
            dx = 5 * np.ones_like(zpos)
            dy = dx.copy()
            dz = hist[i].flatten()

            # 设置坐标轴标签
            self.axes.set_xlabel('front')
            self.axes.set_ylabel('side')
            self.axes.set_zlabel('height')
            self.axes.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color_list[i], zsort='average')

# 运行模块
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.WyyAnalysis import Ui_matplot_demo

class myWindow(QWidget, Ui_matplot_demo):
    def __init__(self,logs):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0, 0)
        self.logs = logs

        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=10, height=6, dpi=100)
        self.F.plot_cos()

        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        # 在容器中添加一个groupbox对象，在groupbox对象中创建布局
        self.groupBox = QGroupBox(self.plt3d_module)
        self.groupBox.setMinimumSize(QSize(1100, 610))
        self.groupBox.setTitle("画图demo")

        def connect_bind():
            self.bt_open.clicked.connect(self.open_pic)
            self.bt_close.clicked.connect(self.close_pic)
        connect_bind()

        self.glo_plt_figure = QGridLayout(self.groupBox)

    def open_pic(self):
        self.F = MyFigure(width=10, height=6, dpi=100)
        # self.F.plot_3d()
        self.F.plot_2d(self.logs)
        self.glo_plt_figure.addWidget(self.F, 0, 0)
        print("here")
        self.show()
        self.glo_plt_figure.addWidget(self.F, 0, 0)

    def close_pic(self):
        self.glo_plt_figure.removeWidget(self.F)
        self.show()


def main():
    app = QApplication(sys.argv)
    UserUtil.login('123','123')
    win = myWindow(CUR_USER.getLogs(1))
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()