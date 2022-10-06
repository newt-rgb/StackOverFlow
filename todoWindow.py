
import sys
from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from CustomDialog import CustomDialog
from calendar_ui import Ui_addmenu
from PyQt5.QtCore import QDateTime,QDate,QTime
from datetime import date,time,datetime,timedelta

class todoWindow(QWidget, Ui_addmenu):
    def __init__(self, parent, curtime = datetime.today()):
        #设置ui
        super().__init__()
        self.setupUi(self)
        
        #设置存储结构
        self.todolist = []
        self.load()
        #设置父窗口，父窗口关闭，子窗口同时关闭
        self.setParent(parent)
        self.setWindowFlags(Qt.Window)
        
        #设置待办事项：内容
        self.content = ""
        self.todoText.textChanged.connect(self.todoTextEdit)
        
        #设置待办事项：截止时间
        self.ddl = curtime
        self.ddlText.setDateTime(curtime)
        self.ddlText.setCurrentSectionIndex(2)
        self.ddlText.setMinimumDateTime(datetime.today())
        self.ddlText.dateTimeChanged.connect(self.ddlTextEdit)
        
        #设置待办事项：是否提醒
        self.alarmflag = False
        self.alarm.stateChanged.connect(self.alarmEdit)
        
        #设置提醒周期：提前m天，每隔n小时一次
        self.advanceDay = 0
        self.altHour = 24
        self.advDay.setMaximum(0)
        self.altDay.setValue(24)
        self.advDay.textChanged.connect(self.advDayEdit)
        self.altDay.textChanged.connect(self.altDayEdit)
        
        #计算截止时间
        self.delta_1 = timedelta(days = 0,hours = 0)
        self.delta_2 = timedelta(days = 0,hours = 0)
        self.nextalarm = self.ddl
        self.deltaDay_1.setText("0")
        self.deltaHour_1.setText("0")
        self.deltaDay_2.setText("0")
        self.deltaHour_2.setText("0")
        
        #确认添加日程
        self.confirmButton.clicked.connect(self.confirm)
        
    #待办事项内容管理
    def todoTextEdit(self):
        self.content = self.todoText.toPlainText()
        self.content = self.content.strip()

    #待办事项截止时间处理
    def ddlTextEdit(self):
        self.ddl = self.ddlText.dateTime().toPyDateTime() 
        self.delta_1 = self.ddl - datetime.today()
        d_d = str(self.delta_1.days)
        d_h = str(int(self.delta_1.seconds / 3600))
        self.deltaDay_1.setText(d_d)
        self.deltaHour_1.setText(d_h)
        
        self.nextalarm = self.ddl - timedelta(days = self.advanceDay)
        self.delta_2 = self.nextalarm - datetime.today()
        d2_d = str(self.delta_2.days)
        d2_h = str(int(self.delta_2.seconds / 3600))
        self.deltaDay_2.setText(d2_d)
        self.deltaHour_2.setText(d2_h)
        #处理提前几天信息，不能超过当前时间
        self.advDay.setMaximum(self.delta_1.days if self.delta_1.days >= 0 else 0)
        
    #待办事项提醒处理
    def alarmEdit(self):
        self.alarmflag = self.alarm.isChecked()

    #处理提前多少天
    def advDayEdit(self):
        self.advanceDay = self.advDay.value()
        adv_d = timedelta(days = self.advanceDay)
        self.nextalarm = self.ddl - adv_d
        self.delta_2 = self.nextalarm - datetime.today()
        d2_d = str(self.delta_2.days)
        d2_h = str(int(self.delta_2.seconds / 3600))
        self.deltaDay_2.setText(d2_d)
        self.deltaHour_2.setText(d2_h)
    
    #处理每隔多少小时
    def altDayEdit(self):
        self.altHour = self.altDay.value()
    
    #完成添加，存入data.json
    def confirm(self):
        if self.content:
            todos = [self.content,datetime.strftime(self.ddl,"%Y-%m-%d %H:%M"),self.alarmflag,self.advanceDay,self.altHour]
            self.todolist.append(todos)
            with open("data.json", "w") as f:
                json.dump(self.todolist, f)
            self.close()
        else:
            dlg = CustomDialog("待办事项内容不能为空！请重新输入。")
            dlg.exec_()
        
    #加载data.json
    def load(self):
        try:
            with open("data.json","r") as f:
                self.todolist = json.load(f)
        except Exception:
            pass
