# -*- coding: utf-8 -*-
# 20180506

import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui,QtCore

# 图片
sys.path.append('../../')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # 窗口位置
        Dialog.move(10, 10)
        # 窗口尺寸
        Dialog.resize(320, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r'./image/image1/余时锐011毫秒钟.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)

        # 垂直布局
        buju = QVBoxLayout()
        # 左侧间隔
        buju.addStretch(1)

        # 标签一，显示余时锐
        self.label1 = QtWidgets.QLabel(Dialog)
        # 客户区左上角到屏幕宽高
        self.label1.setGeometry(QtCore.QRect(0, 0, 1900, 500))
        # 标签一对象名
        self.label1.setObjectName("label1")
        # 布局加入标签一
        buju.addWidget(self.label1)

        # 标签二，显示毫秒数
        self.label2 = QtWidgets.QLabel(Dialog)
        # 客户区左上角到屏幕宽高
        self.label2.setGeometry(QtCore.QRect(0, 450, 1900, 500))
        # 标签二对象名
        self.label2.setObjectName("label2")
        # 布局加入标签二
        buju.addWidget(self.label2)

        # 标签三，显示毫秒数
        self.label3 = QtWidgets.QLabel(Dialog)
        # 客户区左上角到屏幕宽高
        self.label3.setGeometry(QtCore.QRect(0, 900, 1900, 500))
        # 标签三对象名
        self.label3.setObjectName("label3")
        # 布局加入标签三
        buju.addWidget(self.label3)

        # 右侧间隔
        buju.addStretch(1)

        # 滑块
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        # 滑块在客户区位置
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 10, 150, 20))
        # 滑块设置为水平滑块
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        # 滑块对象名
        self.horizontalSlider.setObjectName("horizontalSlider")

        # 按钮
        self.btn = QPushButton('开始计时')
        # 可按
        self.btn.setCheckable(True)
        # 布局加入按钮控件
        buju.addWidget(self.btn)

        # ？？？
        self.retranslateUi(Dialog)
        # 信号连接到槽函数(重要)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 窗口加入布局
        self.setLayout(buju)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "余时锐_毫秒计时器"))
        self.label1.setText(_translate("Dialog", "余时锐"))
        self.label2.setText(_translate("Dialog", "毫秒计时器"))
        self.label3.setText(_translate("Dialog", "时间"))
        self.btn.setText(_translate("Dialog", '开始计时'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
