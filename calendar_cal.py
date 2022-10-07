from asyncio.windows_events import NULL
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QComboBox
from calculator_ui import Ui_MainWindow
from CustomDialog import CustomDialog
from calendar_ui import Ui_Form
from PyQt5 import QtCore,Qt
from datetime import date, time, datetime, timedelta
import sqlite3
advmin = {"0分钟前":0,"5分钟前":5,"15分钟前":15,"30分钟前":30,"1小时前":60,"12小时前":12*60,"1天前":24*60,"3天前":3*24*60,"1周前":7*24*60}
freqDic = {"1次":1,"2次":2,"3次":3}
class cwindow(QWidget,Ui_Form):
    def __init__(self):
        # 实现父类函数的构造
        super().__init__()
        self.setupUi(self)
        #当提醒时间选择从不时，禁止编辑提醒次数
        self.advEdit.activated.connect(self.neverInform)
        self.confirm.clicked.connect(self.confirms)
        
    def neverInform(self):
        if self.advEdit.currentText() in ['从不','0分钟前']:
            self.freqEdit.setDisabled(True)
        else:
            self.freqEdit.setDisabled(False)
        
    def confirms(self):
        _event = self.lineEdit.text().strip()
        if _event == "":
            dlg = CustomDialog("事项不能为空！")
            dlg.exec_()
            return

        _date = datetime.strptime(self.lineEdit_2.text(),"开始:%Y年%m月%d日").strftime("%Y-%m-%d")
        _time = self.timeEdit.time().toPyTime().strftime("%H:%M")
        _datetimeList = self.getDatetimeList(_date,_time,self.advEdit.currentText(),self.freqEdit.currentText())
        
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        sql = "INSERT INTO Data (event,date,Time,completed,frequency,advance) VALUES (?,?,?,?,?,?)"
        row = (_event,_date,_time,'0',_datetimeList,self.advEdit.currentText(),)
        
        cursor.execute(sql,row)
        cursor.close()
        con.commit()
        con.close()
        self.close()

    #算出所有需要发通知的时间，组成字符串
    def getDatetimeList(self, d, t, adv, freq):
        if adv == "从不":
            return ""
        ddl = datetime.strptime(d+t,"%Y-%m-%d%H:%M")
        t_delta = timedelta(minutes = advmin[adv])
        start_time = ddl - t_delta
        if freqDic[freq] == 1:
            return start_time.strftime("%Y-%m-%d %H:%M")
        elif freqDic[freq] == 2:
            second_time = ddl - timedelta(minutes = advmin[adv] / 2)
            return ','.join([start_time.strftime("%Y-%m-%d %H:%M"),second_time.strftime("%Y-%m-%d %H:%M")])
        else:
            second_time = ddl - timedelta(minutes = advmin[adv] / 3 * 2)
            third_time = ddl - timedelta(minutes = advmin[adv] / 3)
            return ','.join([start_time.strftime("%Y-%m-%d %H:%M"),second_time.strftime("%Y-%m-%d %H:%M"),third_time.strftime("%Y-%m-%d %H:%M")])