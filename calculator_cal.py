# 主要完成在计算器中点击事件的信号和事件函数的连接


import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from calculator_ui import Ui_MainWindow
from CustomDialog import CustomDialog
from math import *


# 创建mywindow类，继承于UI设计中的UI_MainWindow类

class mywindow(QMainWindow, Ui_MainWindow):

    # 构造函数
    def __init__(self):
        # 实现父类函数的构造
        super().__init__()
        self.setupUi(self)

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

    #每次根据显示板上的公式进行计算
    def calculate(self):
        try:
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
            self.trans()
            self.lineEdit.insert(str(self.result))
        except:
            dlg = CustomDialog()
            dlg.exec_()
            self.text = ""
            self.lineEdit.clear()


