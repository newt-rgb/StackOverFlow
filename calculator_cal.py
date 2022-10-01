#主要完成在计算器中点击事件的信号和事件函数的连接


import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calculator_ui import Ui_MainWindow

#创建mywindow类，继承于UI设计中的UI_MainWindow类

class mywindow(QWidget, Ui_MainWindow):

    #构造函数
    def __init__(self):
        #实现父类函数的构造
        super().__init__()
        self.setupUi(self)

        #以下为对UI中的按钮的同事件函数的连接
        #回退按钮
        self.pushButton_6.clicked.connect(self.backspace)
        # 1-0按钮
        self.pushButton_19.clicked.connect(self.ps_bt)
        self.pushButton_21.clicked.connect(self.ps_bt2)
        self.pushButton_24.clicked.connect(self.ps_bt3)
        self.pushButton_13.clicked.connect(self.ps_bt4)
        self.pushButton_15.clicked.connect(self.ps_bt5)
        self.pushButton_18.clicked.connect(self.ps_bt6)
        self.pushButton_7.clicked.connect(self.ps_bt7)
        self.pushButton_9.clicked.connect(self.ps_bt8)
        self.pushButton_12.clicked.connect(self.ps_bt9)
        self.pushButton_27.clicked.connect(self.ps_bt10)
        # 运算符
        self.pushButton_17.clicked.connect(self.ps_bt11)
        self.pushButton_11.clicked.connect(self.ps_bt12)
        self.pushButton_5.clicked.connect(self.ps_bt13)
        self.pushButton_4.clicked.connect(self.ps_bt14)
        # 点
        self.pushButton_30.clicked.connect(self.ps_bt15)
        #取余
        self.pushButton_25.clicked.connect(self.ps_btre)
        #等于
        self.pushButton_29.clicked.connect(self.calculate)
        # 清空缓存
        self.pushButton_3.clicked.connect(self.clear_all)
        #三角函数
        self.pushButton_2.clicked.connect(self.Sin)
        self.pushButton_10.clicked.connect(self.Cos)
        self.pushButton_16.clicked.connect(self.Tan)
        self.pushButton_8.clicked.connect(self.Pi)
        #左右括号
        self.pushButton_26.clicked.connect(self.leftBkt)
        self.pushButton_28.clicked.connect(self.rightBkt)
        #阶乘、平方、立方、n次方
        self.pushButton.clicked.connect(self.Factorial)
        self.pushButton_14.clicked.connect(self.Power)
        self.pushButton_20.clicked.connect(self.Square)
        self.pushButton_22.clicked.connect(self.Cube)

    #以下为事件函数具体实现部分
    #text用来记录计算机真正计算的表达式，利用eval(self.text)函数完成实现
    text =""

    #回退函数
    def backspace(self):
        self.lineEdit.backspace()
        self.text = self.text[:-1]
    #按键0-9
    def ps_bt(self):
        self.lineEdit.insert('1')
        self.text += "1"
    def ps_bt2(self):
        self.lineEdit.insert('2')
        self.text += "2"
    def ps_bt3(self):
        self.lineEdit.insert('3')
        self.text += "3"
    def ps_bt4(self):
        self.lineEdit.insert('4')
        self.text += "4"
    def ps_bt5(self):
        self.lineEdit.insert('5')
        self.text += "5"
    def ps_bt6(self):
        self.lineEdit.insert('6')
        self.text += "6"
    def ps_bt7(self):
        self.lineEdit.insert('7')
        self.text += "7"
    def ps_bt8(self):
        self.text += "8"
        self.lineEdit.insert('8')
    def ps_bt9(self):
        self.text += "9"
        self.lineEdit.insert('9')
    def ps_bt10(self):
        self.text += "0"
        self.lineEdit.insert('0')

    #运算符按键
    def ps_bt11(self):
        self.text += "+"
        self.lineEdit.insert('+')
    def ps_bt12(self):
        self.text += "-"
        self.lineEdit.insert('-')
    def ps_bt13(self):
        self.text += "*"
        self.lineEdit.insert('*')
    def ps_bt14(self):
        self.text += "/"
        self.lineEdit.insert('/')

    #点按键
    def ps_bt15(self):
        self.text += "."
        self.lineEdit.insert('.')
    #%按键完成取余操作
    def ps_btre(self):
        self.lineEdit.insert('%')
        self.text += "%"

    #清除按键
    def lineEdit_clear(self):
        self.text =""
        self.lineEdit.clear()
    def clear_all(self):
        self.text = ""
        self.lineEdit.clear()
    #等号按键
    def calculate(self):
        self.lineEdit.clear()
        result = eval(self.text)
        self.lineEdit.insert(str(result))
        self.text = str(result)
    #三角函数按键
    def Sin(self):
        self.text += "math.sin"
        self.lineEdit.insert("sin")
    def Cos(self):
        self.text += "math.cos"
        self.lineEdit.insert("cos")
    def Tan(self):
        self.text += "math.tan"
        self.lineEdit.insert("tan")
    def Pi(self):
        self.text += "math.pi"
        self.lineEdit.insert("Π")

    #左右括号按键
    def leftBkt(self):
        self.text += "("
        self.lineEdit.insert('(')
    def rightBkt(self):
        self.text += ")"
        self.lineEdit.insert(')')

    #次方按键
    def Factorial(self):
        self.lineEdit.insert("!")
        for i in range(len(self.text)):
            if(self.text[len(self.text)-1-i:][0].isdigit() & len(self.text)-1-i!=0):
                continue
            if (i == len(self.text)-1):
                self.text = "math.factorial(" + self.text + ")"
                break
            else:
                text_tmp = "math.factorial("+self.text[0-i:]+")"
                self.text = self.text[:0-i]
                self.text += text_tmp
                break
    def Power(self):
        self.lineEdit.insert("^(")
        for i in range(len(self.text)):
            if(self.text[len(self.text)-1-i:][0].isdigit() & len(self.text)-1-i!=0):
                continue
            if (i == len(self.text)-1):
                self.text = "pow(" + self.text + ","
                break
            else:
                text_tmp = "pow("+self.text[0-i:]+","
                self.text = self.text[:0-i]
                self.text += text_tmp
                break
    def Square(self):
        self.Power()
        self.lineEdit.insert("2)")
        self.text += "2)"
    def Cube(self):
        self.Power()
        self.lineEdit.insert("3)")
        self.text += "3)"