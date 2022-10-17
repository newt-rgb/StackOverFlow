# 主要完成在计算器中点击事件的信号和事件函数的连接
from pickle import TRUE
import sqlite3
import frozen_dir
import sys
import math
from PyQt5.QtCore import Qt, QFileSystemWatcher, QDate, QPoint,QTimer
from PyQt5 import QtCore
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QListWidget, QMessageBox, QListWidgetItem, QPushButton
from calculator_ui import Ui_MainWindow
from CustomDialog import CustomDialog
from calendar_cal import cwindow
from math import *
from datetime import datetime, date, time, timedelta
from win10toast import ToastNotifier
import threading
toast = ToastNotifier()
# 创建mywindow类，继承于UI设计中的UI_MainWindow类

class mywindow(QMainWindow, Ui_MainWindow):

    # 构造函数
    def __init__(self):
        # 实现父类函数的构造
        super().__init__()
        self.setupUi(self)

        self.base = frozen_dir.app_path()
        # 以下为对UI中的按钮的同事件函数的连接
        # 回退按钮
        self.delButton.clicked.connect(self.backspace)
        # 1-0按钮
        self.oneButton.clicked.connect(self.one)
        self.twoButton.clicked.connect(self.two)
        self.threeButton.clicked.connect(self.three)
        self.fourButton.clicked.connect(self.four)
        self.fiveButton.clicked.connect(self.five)
        self.sixButton.clicked.connect(self.six)
        self.sevenButton.clicked.connect(self.seven)
        self.eightButton.clicked.connect(self.eight)
        self.nineButton.clicked.connect(self.nine)
        self.zeroButton.clicked.connect(self.zero)
        # 运算符
        self.plusButton.clicked.connect(self.plus)
        self.minusButton.clicked.connect(self.minus)
        self.mutiButton.clicked.connect(self.multiply)
        self.divdButton.clicked.connect(self.divide)
        # 点
        self.dotButton.clicked.connect(self.dot)
        # 取余
        self.percentButton.clicked.connect(self.percentage)
        # 等于
        self.equalButton.clicked.connect(self.calculate)
        # 清空缓存
        self.cButton.clicked.connect(self.clear_all)
        # 三角函数
        self.sinButton.clicked.connect(self.Sin)
        self.cosButton.clicked.connect(self.Cos)
        self.tanButton.clicked.connect(self.Tan)
        self.piButton.clicked.connect(self.Pi)
        # 左右括号
        self.leftButton.clicked.connect(self.leftBkt)
        self.rightButton.clicked.connect(self.rightBkt)
        # 阶乘、平方、立方、n次方
        self.factButton.clicked.connect(self.Factorial)
        self.sqrtButton.clicked.connect(self.Sqrt)
        self.squareButton.clicked.connect(self.Square)
        self.cubeButton.clicked.connect(self.Cube)

        #日历控件
        #单击查看当日日程情况
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        #双击添加新日程
        self.table = self.calendarWidget.findChild(QtWidgets.QTableView)
        self.table.viewport().installEventFilter(self)
        #按键添加新日程
        self.addButton.clicked.connect(self.addevent)
        #按键删除新日程
        self.deleteButton.clicked.connect(self.deleteEvent)
        #跟踪数据库变化
        self.fs_watcher = QFileSystemWatcher()
        self.fs_watcher.addPath('{}\database.db'.format(self.base))
        self.fs_watcher.fileChanged.connect(lambda : self.updateTasklist(self.calendarWidget.selectedDate().toPyDate()))
        #更新完成状态
        self.tasklist.itemChanged.connect(self.isComplete)
        #以下实现闹铃功能
        # self.thread = threading.Thread(target = self.checkInform)
        # self.thread.start()
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkInform)
        self.timer.start(60000)
        self.checkInform()
    # 以下为事件函数具体实现部分
    result = 0
    #回退按钮
    def backspace(self):
        self.lineEdit.backspace()
    #数字1-9
    def one(self):
        self.lineEdit.insert('1')

    def two(self):
        self.lineEdit.insert('2')

    def three(self):
        self.lineEdit.insert('3')

    def four(self):
        self.lineEdit.insert('4')

    def five(self):
        self.lineEdit.insert('5')

    def six(self):
        self.lineEdit.insert('6')

    def seven(self):
        self.lineEdit.insert('7')

    def eight(self):
        self.lineEdit.insert('8')

    def nine(self):
        self.lineEdit.insert('9')

    def zero(self):
        self.lineEdit.insert('0')

    #加减乘除
    def plus(self):
        self.lineEdit.insert('+')

    def minus(self):
        self.lineEdit.insert('-')

    def multiply(self):
        self.lineEdit.insert('*')

    def divide(self):
        self.lineEdit.insert('/')
    #小数点
    def dot(self):
        self.lineEdit.insert('.')

    # 百分号按键
    def percentage(self):
        self.lineEdit.insert('%')

    # 清除按键
    def lineEdit_clear(self):
        self.lineEdit.clear()

    def clear_all(self):
        self.lineEdit.clear()

    #三角函数按键
    def Sin(self):
        self.lineEdit.insert("sin(")

    def Cos(self):
        self.lineEdit.insert("cos(")

    def Tan(self):
        self.lineEdit.insert("tan(")

    def Pi(self):
        self.lineEdit.insert("π")

    #左右括号按键
    def leftBkt(self):
        self.lineEdit.insert('(')

    def rightBkt(self):
        self.lineEdit.insert(')')

    #阶乘、平方、立方、开方按键
    def Factorial(self):
        self.lineEdit.insert("!")

    def Sqrt(self):
        self.lineEdit.insert("√(")

    def Square(self):
        self.lineEdit.insert(")^2")

    def Cube(self):
        self.lineEdit.insert(")^3")

    #搜寻对应左括号并返回其位置
    def position(self, n):
        texttmp = self.lineEdit.text()
        postmp = 0
        for i in range(n - 1, -1, -1):
            if (texttmp[i] == ")"):
                postmp += 1
            if (texttmp[i] == "("):
                postmp -= 1
            if (postmp == 0):
                return i

    #对运算结果进行优化
    def trans(self):
        res = str(self.result)
        for i in range(len(res)):
            if (res[i] == '.'):
                if (len(res) - i >= 6):
                    self.result = round(self.result, 2)
                self.result = round(self.result,10)
                res = str(self.result)
                if(i == len(res)-2):
                    if(res[-1] == '0'):
                       self.result= round(self.result)
                break
    def change(self):
        res = str(self.result)
        for i in range(len(res)):
            if(res[i] == '.'):
                self.result = round(self.result,12)
                if (i == len(res) - 2):
                    if (res[-1] == '0'):
                        self.result = round(self.result)
                break

    #每次根据显示板上的公式进行计算
    def calculate(self):
        try:
            self.labelpi = 0
            text = self.lineEdit.text()
            # 计算判断
            for n in range(len(text)):

                # 解决阶乘问题
                if (text[n] == "!"):
                    if (text[n - 1] != ')'):
                        for i in range(n):
                            m = n - i - 1
                            if (m > 0 and text[m].isdigit()):
                                continue
                            else:
                                if (m != 0):
                                    text = text[:n - i] + "factorial(" + text[n - i:n] + ")" + text[n + 1:]
                                    break
                                else:
                                    text = "factorial(" + text[:n] + ")" + text[n + 1:]
                                    break
                    else:
                        # 判断当需要计算括号里面的阶乘值
                        pos = self.position(n)
                        text = text[:pos] + "factorial" + text[pos:n] + text[n + 1:]
                # 计算次方
                if (text[n] == "^"):
                    text = text[:n] + "**" + text[n + 1:]
                # 计算π值
                if (text[n] == "π"):
                    text = text[:n] + "math.pi" + text[n + 1:]
                    self.labelpi = 1
                # 计算%
                if (text[n] == "%"):
                    text = text[:n] + "*0.01" + text[n + 1:]
                # 计算开方值
                if (text[n] == "√"):
                    text = text[:n] + "math.sqrt" + text[n + 1:]
            # 计算判断结束
            self.lineEdit.clear()
            self.result = eval(text)
            # 优化结果
            if(self.labelpi == 1):
                self.trans()
            else:
                self.change()
            self.lineEdit.insert(str(self.result))
        except:
            dlg = CustomDialog()
            dlg.exec_()
            self.text = ""
            self.lineEdit.clear()

    #得到当前的日期
    def getdate(self):
        date = QtCore.QDate(self.calendarWidget.selectedDate())
        self.year = date.year()
        self.month = date.month()
        self.day = date.day()

    #添加新日程界面
    def addevent(self):
        self.addw = cwindow()
        _date = self.calendarWidget.selectedDate().toPyDate().strftime("开始:%Y年%m月%d日")
        self.addw.lineEdit_2.setText(_date)
        self.addw.lineEdit_2.setReadOnly(True)
        curDate = date.today()
        selcDate = self.calendarWidget.selectedDate().toPyDate()

        ddllist = ["从不","0分钟前","5分钟前","15分钟前","30分钟前","1小时前","12小时前","1天前","3天前","1周前"]
        freqlist = ["1次","2次","3次"]
        self.addw.advEdit.addItems(ddllist)
        self.addw.freqEdit.addItems(freqlist)
        self.addw.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addw.neverInform()
        self.addw.show() 
    
    #双击判断
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
            source is self.table.viewport()):
            self.addevent()
        return super().eventFilter(source, event)

    #日历选择变化，事项清单改变
    def calendarDateChanged(self):
        dateselected = self.calendarWidget.selectedDate().toPyDate()
        self.updateTasklist(dateselected)
    
    #更新事项清单
    def updateTasklist(self, _date):
        self.tasklist.clear()
        #关联数据库
        db = sqlite3.connect('{}\database.db'.format(self.base))
        cursor = db.cursor()
        strdate = _date.strftime("%Y-%m-%d")
        query = "SELECT event,date,time,completed,frequency,advance FROM Data WHERE date = ?"
        row = (strdate,)
        curdatetime = datetime.today()
        
        results = cursor.execute(query, row).fetchall()
        
        for result in results:
            #计算距离截止时间和下次提醒时间还有多久
            stamp_1,stamp_2 = self.CalcStamp(result)
            _datetime = result[1] + ' ' + result[2]
            detail = "事件 : {:^}\n截止时间 : {:^}\n距离截止时间 : {:^}\n距离下次提醒时间 : {:^}".format(result[0],_datetime,stamp_1,stamp_2)
            item = QListWidgetItem(detail)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[3] == '1':
                item.setCheckState(QtCore.Qt.Checked)
            elif result[3] == "0":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.tasklist.addItem(item)
        self.tasklist.setCurrentRow(0)
        self.calendarWidget.updateCells()
    
    #根据查询结果返回距离截止时间和下一次提醒时间的时长
    def CalcStamp(self, calist):
        curdatetime = datetime.today()
        ddl = datetime.strptime(calist[1]+calist[2],"%Y-%m-%d%H:%M")
        
        if calist[3] == '0' and (ddl < curdatetime):
            return "任务已过时","任务已过时"
        
        if calist[3] == '1':
            return "任务已完成","任务已完成"
        
        delta = ddl - curdatetime
        
        stamp_1 = "{}天{}小时".format(delta.days, int(delta.seconds / 3600))
        
        if calist[5] == '从不':
            return stamp_1,"任务不需要提醒"
        
        
        inform_list = self.getInformDateTime(calist[4])
        delta_2 = []
        for i,_datetime in enumerate(inform_list):
            delta_2.append(inform_list[i]- curdatetime)
        
        for i,_delta in enumerate(delta_2):
            if _delta.days < 0 or _delta.seconds < 0 :
                continue
            else:
                stamp_2 = "{}天{}小时".format(_delta.days, int(_delta.seconds / 3600))
                return stamp_1,stamp_2

        return stamp_1,"提醒已过时"

    #将提醒几次转换成具体时间
    def getInformDateTime(self, datestr):
        datelist = []
        datestr = datestr.split(',')
        for dt in datestr:
            datelist.append(datetime.strptime(dt,"%Y-%m-%d %H:%M"))
        return datelist

    #删除事项
    def deleteEvent(self):
        try:
            _datetime_ = str(self.tasklist.currentItem().text().splitlines(False)[1][7:])
            _date = _datetime_.split(' ')[0]
            _time = _datetime_.split(' ')[1]

            db = sqlite3.connect('{}\database.db'.format(self.base))
            cursor = db.cursor()
            query = "DELETE FROM Data WHERE date = ? AND Time = ?"
            row = (_date,_time,)
            cursor.execute(query,row)
            db.commit()
            self.calendarWidget.updateCells()
        except:
            dlg = CustomDialog("这天没有事项！")
            dlg.exec_
    
    #更改数据库中的事项完成属性
    def isComplete(self):
        _datetime_ = str(self.tasklist.currentItem().text().splitlines(False)[1][7:])
        _date = _datetime_.split(' ')[0]
        _time = _datetime_.split(' ')[1]
        db = sqlite3.connect('{}\database.db'.format(self.base))
        cursor = db.cursor()

        if self.tasklist.currentItem().checkState() == Qt.Checked:
            query = "UPDATE Data  SET completed = '1' WHERE date = ? AND Time = ?"
        else:
            query = "UPDATE Data  SET completed = '0' WHERE date = ? AND Time = ?"
        row = (_date,_time,)
        cursor.execute(query,row)
        db.commit()
        self.calendarWidget.updateCells()
    
    #每分钟检查一次
    def checkInform(self):
        db = sqlite3.connect('{}\database.db'.format(self.base))
        cursor = db.cursor()
        curtime = datetime.today().strftime('%Y-%m-%d %H:%M')
        query = "SELECT event,frequency FROM Data WHERE completed = '0'"
        results = cursor.execute(query).fetchall()
        for _data in results:
            if _data[1] == '':
                continue
            else:
                all_date = _data[1].split(',')
            for _date in all_date:
                if curtime == _date:
                    toast.show_toast(
                        '提醒！',
                        _data[0],
                        icon_path='icon.ico',
                        duration=5,
                        threaded=True
                    )
                    self.updateTasklist(self.calendarWidget.selectedDate().toPyDate())
        cursor.close()
        db.close()
        