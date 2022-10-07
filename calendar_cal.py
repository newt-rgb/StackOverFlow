from importlib import import_module
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from calculator_ui import Ui_MainWindow
from CustomDialog import CustomDialog
from calendar_ui import Ui_Form
from PyQt5 import QtCore,Qt
from datetime import date, time, datetime
import sqlite3
advmin = {"0分钟前":0,"5分钟前":5,"15分钟前":15,"30分钟前":30,"1小时前":60,"12小时前":12*60,"1天前":24*60,"3天前":3*24*60,"1周前":7*24*60}
class cwindow(QWidget,Ui_Form):
    def __init__(self):
        # 实现父类函数的构造
        super().__init__()
        self.setupUi(self)
        self.confirm.clicked.connect(self.confirms)
        
    def confirms(self):
        date = self.dateEdit.text()
        self.year = date[:4]
        self.month = date[5:7]
        self.day = date[8:10]
        con = sqlite3.connect("database.db")
        sql = "insert into caldata (objname,ddlyear,ddlmonth,ddlday,reminder,gap) values ("+"'"+self.lineEdit.text()+"'"+","+self.year+","+self.month+","+self.day+","+str(self.comboBox.currentIndex())+","+str(self.comboBox_2.currentIndex())+")"
        cursor = con.cursor()
        cursor.execute(sql)
        cursor.close()
        con.commit()
        con.close()
