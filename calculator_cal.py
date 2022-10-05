#主要完成在计算器中点击事件的信号和事件函数的连接


import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from calculator_ui import Ui_MainWindow
from CustomDialog import CustomDialog
#创建mywindow类，继承于UI设计中的UI_MainWindow类

class mywindow(QMainWindow, Ui_MainWindow):

    #构造函数
    def __init__(self):
        #实现父类函数的构造
        super().__init__()
        self.setupUi(self)
        
        #以下为对UI中的按钮的同事件函数的连接
        #回退按钮
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
        #取余
        self.percentButton.clicked.connect(self.percentage)
        #等于
        self.equalButton.clicked.connect(self.calculate)
        # 清空缓存
        self.cButton.clicked.connect(self.clear_all)
        #三角函数
        self.sinButton.clicked.connect(self.Sin)
        self.cosButton.clicked.connect(self.Cos)
        self.tanButton.clicked.connect(self.Tan)
        self.piButton.clicked.connect(self.Pi)
        #左右括号
        self.leftButton.clicked.connect(self.leftBkt)
        self.rightButton.clicked.connect(self.rightBkt)
        #阶乘、平方、立方、n次方
        self.factButton.clicked.connect(self.Factorial)
        self.sqrtButton.clicked.connect(self.Sqrt)
        self.squareButton.clicked.connect(self.Square)
        self.cubeButton.clicked.connect(self.Cube)

    #以下为事件函数具体实现部分
    #text用来记录计算机真正计算的表达式，利用eval(self.text)函数完成实现
    text =""

    #回退函数
    def backspace(self):
        self.lineEdit.backspace()
        self.text = self.text[:-1]
    
    #按键0-9
    def one(self):
        self.lineEdit.insert('1')
        self.text += "1"
        
    def two(self):
        self.lineEdit.insert('2')
        self.text += "2"
    def three(self):
        self.lineEdit.insert('3')
        self.text += "3"
    def four(self):
        self.lineEdit.insert('4')
        self.text += "4"
    def five(self):
        self.lineEdit.insert('5')
        self.text += "5"
    def six(self):
        self.lineEdit.insert('6')
        self.text += "6"
    def seven(self):
        self.lineEdit.insert('7')
        self.text += "7"
    def eight(self):
        self.text += "8"
        self.lineEdit.insert('8')
    def nine(self):
        self.text += "9"
        self.lineEdit.insert('9')
    def zero(self):
        self.text += "0"
        self.lineEdit.insert('0')

    #运算符按键
    def plus(self):
        self.text += "+"
        self.lineEdit.insert('+')
    def minus(self):
        self.text += "-"
        self.lineEdit.insert('-')
    def multiply(self):
        self.text += "*"
        self.lineEdit.insert('*')
    def divide(self):
        self.text += "/"
        self.lineEdit.insert('/')

    #点按键
    def dot(self):
        self.text += "."
        self.lineEdit.insert('.')
    #百分号按键
    def percentage(self):
        self.lineEdit.insert('%')
        self.text += "* 0.01"

    #清除按键
    def lineEdit_clear(self):
        self.text =""
        self.lineEdit.clear()
    def clear_all(self):
        self.text = ""
        self.lineEdit.clear()
    #等号按键
    
    def calculate(self):
        try:
            self.lineEdit.clear()
            result = eval(self.text)
            self.lineEdit.insert(str(result))
            self.text = str(result)
        except:
            dlg = CustomDialog()
            dlg.exec_()
            self.text = ""
            self.lineEdit.clear()
        
    #三角函数按键
    def Sin(self):
        self.text += "math.sin("
        self.lineEdit.insert("sin(")
    def Cos(self):
        self.text += "math.cos("
        self.lineEdit.insert("cos(")
    def Tan(self):
        self.text += "math.tan("
        self.lineEdit.insert("tan(")
    def Pi(self):
        self.text += "math.pi"
        self.lineEdit.insert("π")

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
    
    def Sqrt(self):
        self.text += "math.sqrt("
        self.lineEdit.insert("√(")
    
    
    def Square(self):
        # self.Power()
        self.lineEdit.insert(")^2")
        self.text += ") ** 2"
        
    def Cube(self):
        # self.Power()
        self.lineEdit.insert(")^3")
        self.text += ") ** 3"