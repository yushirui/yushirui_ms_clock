# -*- coding: utf-8 -*-
# 20180513

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap, QPainter

sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')
sys.path.append('../../../../')

# ui
from ui import Ui_Dialog

# 图片
import image_rc


def yu_ms():
    import time
    t = time.time()
    nowTime = lambda: int(round(t * 1000))
    return nowTime()


class Yu(QDialog, Ui_Dialog):
    # 初始化
    def __init__(self, parent=None):
        super(Yu, self).__init__(parent)
        self.setupUi(self)

        # 窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 窗口图标
        self.setWindowIcon(QIcon(':yu/yu.ico'))

        # 标题
        self.setWindowTitle('余时锐毫秒计时器v1.0')

        # 滚动条
        # 设置最小值
        self.horizontalSlider.setMinimum(10)
        # 设置最大值
        self.horizontalSlider.setMaximum(400)
        # 步长
        self.horizontalSlider.setSingleStep(1)
        # 设置当前值
        self.horizontalSlider.setValue(20)
        # 刻度位置，刻度在下方
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.horizontalSlider.setTickInterval(20)

        # 标签居中
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)

        # 按钮点击槽函数
        self.btn.clicked.connect(self.yu_btnevent)

        # 设置无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        # 滑块值
        size = self.horizontalSlider.value()

        # 窗口大小
        self.resize(32, 24)

        # 设置字体、字号
        self.label1.setFont(QFont('Arial', size))
        self.label2.setFont(QFont('Arial', size))
        self.label3.setFont(QFont('Arial', size))
        # 设置颜色
        self.label1.setStyleSheet('color:skyblue')
        self.label2.setStyleSheet('color:yellow')
        self.label3.setStyleSheet('color:black')

    def yu_btnevent(self):
        yu_btn_name = self.btn.text()
        if yu_btn_name == '开始计时':
            # 按钮名称变化
            self.btn.setText('停止计时')

            # 初始时间
            self.yu_chushi = yu_ms()

            # 初始化一个定时器
            self.timer = QTimer(self)
            # 计时结束调用operate()方法
            self.timer.timeout.connect(self.operate)
            # 设置计时间隔并启动
            self.timer.start(1)

        if yu_btn_name == '停止计时':
            # 按钮名称变化
            self.btn.setText('开始计时')
            # 计时器停止
            self.timer.stop()

    def operate(self):
        # '%03d' % 1
        yu_shijian = '%.3f' % ((yu_ms() - self.yu_chushi) / 1000)
        self.label3.setText(str(yu_shijian))

    # 重写绘制事件
    def paintEvent(self, *args, **kwargs):
        # 设置画刷
        yu_painter = QPainter(self)
        # 设置背景图片
        yu_pixmap = QPixmap(r':yu/yu.ico')
        # 画刷.绘制背景图片
        yu_painter.drawPixmap(self.rect(), yu_pixmap)


# pyinstaller -F -w -i yu.ico main.py
if __name__ == "__main__":

    app = QApplication(sys.argv)
    yushirui = Yu()
    yushirui.show()
    sys.exit(app.exec_())
