# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
'''
time:4-10  10:15
功能：简易的，没有进行渲染，没有关闭窗口的功能
'''
'文档分离UI和主程序窗口'   #4-10 10：39完成
'改进页面，字体效果等'
from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from calc_interface import Ui_MainWindow
import os,sys

global e_view    
'这个全局变量的作用我真的不太懂'
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.e_view = QtWidgets.QTextEdit(self.centralwidget)
        self.e_view.setObjectName("e_view")
        self.verticalLayout_3.addWidget(self.e_view)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.b_close = QtWidgets.QPushButton(self.centralwidget)
        self.b_close.setMinimumSize(QtCore.QSize(50, 50))
        self.b_close.setObjectName("b_close")
        self.gridLayout_2.addWidget(self.b_close, 0, 0, 1, 1)
        self.b_7 = QtWidgets.QPushButton(self.centralwidget)
        self.b_7.setMinimumSize(QtCore.QSize(50, 50))
        self.b_7.setObjectName("b_7")
        self.gridLayout_2.addWidget(self.b_7, 1, 0, 1, 1)
        self.b_4 = QtWidgets.QPushButton(self.centralwidget)
        self.b_4.setMinimumSize(QtCore.QSize(50, 50))
        self.b_4.setObjectName("b_4")
        self.gridLayout_2.addWidget(self.b_4, 2, 0, 1, 1)
        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setMinimumSize(QtCore.QSize(50, 50))
        self.b_1.setObjectName("b_1")
        self.gridLayout_2.addWidget(self.b_1, 3, 0, 1, 1)
        self.b_0 = QtWidgets.QPushButton(self.centralwidget)
        self.b_0.setMinimumSize(QtCore.QSize(50, 50))
        self.b_0.setObjectName("b_0")
        self.gridLayout_2.addWidget(self.b_0, 4, 0, 1, 1)
        self.b_pt = QtWidgets.QPushButton(self.centralwidget)
        self.b_pt.setMinimumSize(QtCore.QSize(50, 50))
        self.b_pt.setObjectName("b_pt")
        self.gridLayout_2.addWidget(self.b_pt, 4, 1, 1, 1)
        self.b_eq = QtWidgets.QPushButton(self.centralwidget)
        self.b_eq.setMinimumSize(QtCore.QSize(50, 50))
        self.b_eq.setObjectName("b_eq")
        self.gridLayout_2.addWidget(self.b_eq, 4, 2, 1, 1)
        self.b_add = QtWidgets.QPushButton(self.centralwidget)
        self.b_add.setMinimumSize(QtCore.QSize(50, 50))
        self.b_add.setObjectName("b_add")
        self.gridLayout_2.addWidget(self.b_add, 4, 3, 1, 1)
        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setMinimumSize(QtCore.QSize(50, 50))
        self.b_2.setObjectName("b_2")
        self.gridLayout_2.addWidget(self.b_2, 3, 1, 1, 1)
        self.b_5 = QtWidgets.QPushButton(self.centralwidget)
        self.b_5.setMinimumSize(QtCore.QSize(50, 50))
        self.b_5.setObjectName("b_5")
        self.gridLayout_2.addWidget(self.b_5, 2, 1, 1, 1)
        self.b_8 = QtWidgets.QPushButton(self.centralwidget)
        self.b_8.setMinimumSize(QtCore.QSize(50, 50))
        self.b_8.setObjectName("b_8")
        self.gridLayout_2.addWidget(self.b_8, 1, 1, 1, 1)
        self.b_delete = QtWidgets.QPushButton(self.centralwidget)
        self.b_delete.setMinimumSize(QtCore.QSize(50, 50))
        self.b_delete.setObjectName("b_delete")
        self.gridLayout_2.addWidget(self.b_delete, 0, 1, 1, 1)
        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setMinimumSize(QtCore.QSize(50, 50))
        self.b_3.setObjectName("b_3")
        self.gridLayout_2.addWidget(self.b_3, 3, 2, 1, 1)
        self.b_sub = QtWidgets.QPushButton(self.centralwidget)
        self.b_sub.setMinimumSize(QtCore.QSize(50, 50))
        self.b_sub.setObjectName("b_sub")
        self.gridLayout_2.addWidget(self.b_sub, 3, 3, 1, 1)
        self.b_6 = QtWidgets.QPushButton(self.centralwidget)
        self.b_6.setMinimumSize(QtCore.QSize(50, 50))
        self.b_6.setObjectName("b_6")
        self.gridLayout_2.addWidget(self.b_6, 2, 2, 1, 1)
        self.b_mul = QtWidgets.QPushButton(self.centralwidget)
        self.b_mul.setMinimumSize(QtCore.QSize(50, 50))
        self.b_mul.setObjectName("b_mul")
        self.gridLayout_2.addWidget(self.b_mul, 2, 3, 1, 1)
        self.b_9 = QtWidgets.QPushButton(self.centralwidget)
        self.b_9.setMinimumSize(QtCore.QSize(50, 50))
        self.b_9.setObjectName("b_9")
        self.gridLayout_2.addWidget(self.b_9, 1, 2, 1, 1)
        self.b_div = QtWidgets.QPushButton(self.centralwidget)
        self.b_div.setMinimumSize(QtCore.QSize(50, 50))
        self.b_div.setObjectName("b_div")
        self.gridLayout_2.addWidget(self.b_div, 1, 3, 1, 1)
        self.b_clear = QtWidgets.QPushButton(self.centralwidget)
        self.b_clear.setMinimumSize(QtCore.QSize(50, 50))
        self.b_clear.setObjectName("b_clear")
        self.gridLayout_2.addWidget(self.b_clear, 0, 2, 1, 1)
        self.b_baifenhao = QtWidgets.QPushButton(self.centralwidget)
        self.b_baifenhao.setMinimumSize(QtCore.QSize(50, 50))
        self.b_baifenhao.setObjectName("b_baifenhao")
        self.gridLayout_2.addWidget(self.b_baifenhao, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_close.setText(_translate("MainWindow", "close"))
        self.b_7.setText(_translate("MainWindow", "7"))
        self.b_4.setText(_translate("MainWindow", "4"))
        self.b_1.setText(_translate("MainWindow", "1"))
        self.b_0.setText(_translate("MainWindow", "0"))
        self.b_pt.setText(_translate("MainWindow", "."))
        self.b_eq.setText(_translate("MainWindow", "="))
        self.b_add.setText(_translate("MainWindow", "+"))
        self.b_2.setText(_translate("MainWindow", "2"))
        self.b_5.setText(_translate("MainWindow", "5"))
        self.b_8.setText(_translate("MainWindow", "8"))
        self.b_delete.setText(_translate("MainWindow", "delete"))
        self.b_3.setText(_translate("MainWindow", "3"))
        self.b_sub.setText(_translate("MainWindow", "-"))
        self.b_6.setText(_translate("MainWindow", "6"))
        self.b_mul.setText(_translate("MainWindow", "*"))
        self.b_9.setText(_translate("MainWindow", "9"))
        self.b_div.setText(_translate("MainWindow", "/"))
        self.b_clear.setText(_translate("MainWindow", "clear"))
        self.b_baifenhao.setText(_translate("MainWindow", "%"))
pluginsPath='PyQt5/Qt/plugins'
if os.path.exists(pluginsPath):#指定插件路径。源码运行时不会生效，打包后运行检测到路径，加载插件
 QApplication.addLibraryPath(pluginsPath)

class MyMainWindow(QMainWindow, Ui_MainWindow):

 def forge_link(self):                                    ###########################
  self.b_0.clicked.connect(self.button_event(0))
  self.b_1.clicked.connect(self.button_event(1))
  self.b_2.clicked.connect(self.button_event(2))
  self.b_3.clicked.connect(self.button_event(3))
  self.b_4.clicked.connect(self.button_event(4))
  self.b_5.clicked.connect(self.button_event(5))
  self.b_6.clicked.connect(self.button_event(6))
  self.b_7.clicked.connect(self.button_event(7))
  self.b_8.clicked.connect(self.button_event(8))
  self.b_9.clicked.connect(self.button_event(9))
  self.b_add.clicked.connect(self.button_event('+'))
  self.b_sub.clicked.connect(self.button_event('-'))
  self.b_mul.clicked.connect(self.button_event('*'))
  self.b_div.clicked.connect(self.button_event('/'))
  #self.b_pow.clicked.connect(self.button_event('**'))
  #self.b_bra_l.clicked.connect(self.button_event('('))
  #self.b_bra_r.clicked.connect(self.button_event(')'))
  self.b_baifenhao.clicked.connect(self.button_event('%'))
  #self.b_pai.clicked.connect(self.button_event('3.1415926'))
  self.b_pt.clicked.connect(self.button_event('.'))
  self.b_delete.clicked.connect(self.delete_event)
  self.b_clear.clicked.connect(self.clear_event)
  self.b_eq.clicked.connect(self.calc_complish)

 def __init__(self, parent=None):
  super(MyMainWindow, self).__init__(parent)
  self.setupUi(self)
  self.forge_link() #连接槽函数

 def button_event(self,arg):
  # print(dir(self.e_view))
  global e_view
  e_view=self.e_view
  def fun():  #返回一个自定义的槽函数
   global e_view
   txt = e_view.toPlainText()
   e_view.setText(txt + str(arg))
  return fun

 def calc_complish(self):
  txt=self.e_view.toPlainText()
  ans=''
  try:
   ans=str(eval(txt))
  except BaseException:
   ans='MathError'
  # print(ans)
  self.clear_event()
  self.e_view.setText(ans)
  #self.l_hist.addItem(txt+'='+ans)

 def clear_event(self):
  self.e_view.setText('')

 def delete_event(self):
  txt = self.e_view.toPlainText()
  txt=txt[:len(txt)-1]
  self.e_view.setText(txt)

if __name__ == '__main__':
 app=QApplication(sys.argv)
 myWin=MyMainWindow()
 myWin.show()
 sys.exit(app.exec())