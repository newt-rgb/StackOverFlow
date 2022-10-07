# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.calc = QtWidgets.QWidget()
        self.calc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calc.setObjectName("calc")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.calc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.calc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.splitter = QtWidgets.QSplitter(self.calc)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttonGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.buttonGrid.setContentsMargins(0, 0, 5, 0)
        self.buttonGrid.setObjectName("buttonGrid")
        self.factButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.factButton.sizePolicy().hasHeightForWidth())
        self.factButton.setSizePolicy(sizePolicy)
        self.factButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.factButton.setFont(font)
        self.factButton.setStyleSheet("")
        self.factButton.setObjectName("factButton")
        self.buttonGrid.addWidget(self.factButton, 0, 0, 1, 1)
        self.rightButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy)
        self.rightButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.rightButton.setFont(font)
        self.rightButton.setStyleSheet("")
        self.rightButton.setObjectName("rightButton")
        self.buttonGrid.addWidget(self.rightButton, 4, 1, 1, 1)
        self.mutiButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutiButton.sizePolicy().hasHeightForWidth())
        self.mutiButton.setSizePolicy(sizePolicy)
        self.mutiButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.mutiButton.setFont(font)
        self.mutiButton.setStyleSheet("")
        self.mutiButton.setAutoRepeatInterval(101)
        self.mutiButton.setAutoDefault(False)
        self.mutiButton.setObjectName("mutiButton")
        self.buttonGrid.addWidget(self.mutiButton, 0, 4, 1, 1)
        self.squareButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.squareButton.sizePolicy().hasHeightForWidth())
        self.squareButton.setSizePolicy(sizePolicy)
        self.squareButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.squareButton.setFont(font)
        self.squareButton.setStyleSheet("")
        self.squareButton.setObjectName("squareButton")
        self.buttonGrid.addWidget(self.squareButton, 3, 1, 1, 1)
        self.twoButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        self.twoButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("")
        self.twoButton.setObjectName("twoButton")
        self.buttonGrid.addWidget(self.twoButton, 3, 3, 1, 1)
        self.sinButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinButton.sizePolicy().hasHeightForWidth())
        self.sinButton.setSizePolicy(sizePolicy)
        self.sinButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.sinButton.setFont(font)
        self.sinButton.setStyleSheet("")
        self.sinButton.setObjectName("sinButton")
        self.buttonGrid.addWidget(self.sinButton, 0, 1, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        self.sevenButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("")
        self.sevenButton.setObjectName("sevenButton")
        self.buttonGrid.addWidget(self.sevenButton, 1, 2, 1, 1)
        self.nineButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        self.nineButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("")
        self.nineButton.setObjectName("nineButton")
        self.buttonGrid.addWidget(self.nineButton, 1, 4, 1, 1)
        self.cosButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cosButton.sizePolicy().hasHeightForWidth())
        self.cosButton.setSizePolicy(sizePolicy)
        self.cosButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.cosButton.setFont(font)
        self.cosButton.setStyleSheet("")
        self.cosButton.setObjectName("cosButton")
        self.buttonGrid.addWidget(self.cosButton, 1, 1, 1, 1)
        self.dotButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy)
        self.dotButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.dotButton.setFont(font)
        self.dotButton.setStyleSheet("")
        self.dotButton.setObjectName("dotButton")
        self.buttonGrid.addWidget(self.dotButton, 4, 4, 1, 1)
        self.percentButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentButton.sizePolicy().hasHeightForWidth())
        self.percentButton.setSizePolicy(sizePolicy)
        self.percentButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.percentButton.setFont(font)
        self.percentButton.setStyleSheet("")
        self.percentButton.setObjectName("percentButton")
        self.buttonGrid.addWidget(self.percentButton, 4, 2, 1, 1)
        self.cubeButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cubeButton.sizePolicy().hasHeightForWidth())
        self.cubeButton.setSizePolicy(sizePolicy)
        self.cubeButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.cubeButton.setFont(font)
        self.cubeButton.setStyleSheet("")
        self.cubeButton.setObjectName("cubeButton")
        self.buttonGrid.addWidget(self.cubeButton, 3, 0, 1, 1)
        self.plusButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        self.plusButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("")
        self.plusButton.setObjectName("plusButton")
        self.buttonGrid.addWidget(self.plusButton, 2, 5, 1, 1)
        self.sixButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        self.sixButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("")
        self.sixButton.setObjectName("sixButton")
        self.buttonGrid.addWidget(self.sixButton, 2, 4, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("")
        self.zeroButton.setObjectName("zeroButton")
        self.buttonGrid.addWidget(self.zeroButton, 4, 3, 1, 1)
        self.piButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.piButton.sizePolicy().hasHeightForWidth())
        self.piButton.setSizePolicy(sizePolicy)
        self.piButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.piButton.setFont(font)
        self.piButton.setStyleSheet("")
        self.piButton.setObjectName("piButton")
        self.buttonGrid.addWidget(self.piButton, 1, 0, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        self.fiveButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("")
        self.fiveButton.setObjectName("fiveButton")
        self.buttonGrid.addWidget(self.fiveButton, 2, 3, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy)
        self.leftButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.leftButton.setFont(font)
        self.leftButton.setStyleSheet("")
        self.leftButton.setAutoDefault(False)
        self.leftButton.setObjectName("leftButton")
        self.buttonGrid.addWidget(self.leftButton, 4, 0, 1, 1)
        self.delButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.delButton.setFont(font)
        self.delButton.setStyleSheet("")
        self.delButton.setAutoRepeatInterval(101)
        self.delButton.setAutoDefault(False)
        self.delButton.setObjectName("delButton")
        self.buttonGrid.addWidget(self.delButton, 0, 5, 1, 1)
        self.equalButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy)
        self.equalButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("")
        self.equalButton.setObjectName("equalButton")
        self.buttonGrid.addWidget(self.equalButton, 3, 5, 2, 1)
        self.threeButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        self.threeButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("")
        self.threeButton.setObjectName("threeButton")
        self.buttonGrid.addWidget(self.threeButton, 3, 4, 1, 1)
        self.fourButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        self.fourButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("")
        self.fourButton.setObjectName("fourButton")
        self.buttonGrid.addWidget(self.fourButton, 2, 2, 1, 1)
        self.tanButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tanButton.sizePolicy().hasHeightForWidth())
        self.tanButton.setSizePolicy(sizePolicy)
        self.tanButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.tanButton.setFont(font)
        self.tanButton.setStyleSheet("")
        self.tanButton.setObjectName("tanButton")
        self.buttonGrid.addWidget(self.tanButton, 2, 1, 1, 1)
        self.cButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cButton.sizePolicy().hasHeightForWidth())
        self.cButton.setSizePolicy(sizePolicy)
        self.cButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.cButton.setFont(font)
        self.cButton.setStyleSheet("")
        self.cButton.setObjectName("cButton")
        self.buttonGrid.addWidget(self.cButton, 0, 2, 1, 1)
        self.divdButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divdButton.sizePolicy().hasHeightForWidth())
        self.divdButton.setSizePolicy(sizePolicy)
        self.divdButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.divdButton.setFont(font)
        self.divdButton.setStyleSheet("")
        self.divdButton.setObjectName("divdButton")
        self.buttonGrid.addWidget(self.divdButton, 0, 3, 1, 1)
        self.minusButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        self.minusButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("")
        self.minusButton.setObjectName("minusButton")
        self.buttonGrid.addWidget(self.minusButton, 1, 5, 1, 1)
        self.sqrtButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrtButton.sizePolicy().hasHeightForWidth())
        self.sqrtButton.setSizePolicy(sizePolicy)
        self.sqrtButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.sqrtButton.setFont(font)
        self.sqrtButton.setStyleSheet("")
        self.sqrtButton.setObjectName("sqrtButton")
        self.buttonGrid.addWidget(self.sqrtButton, 2, 0, 1, 1)
        self.eightButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        self.eightButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("")
        self.eightButton.setObjectName("eightButton")
        self.buttonGrid.addWidget(self.eightButton, 1, 3, 1, 1)
        self.oneButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("")
        self.oneButton.setObjectName("oneButton")
        self.buttonGrid.addWidget(self.oneButton, 3, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.calc, "")
        self.cald = QtWidgets.QWidget()
        self.cald.setObjectName("cald")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.cald)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.cald)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_2.addWidget(self.calendarWidget)
        self.splitter_2 = QtWidgets.QSplitter(self.cald)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.addButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.tasklist = QtWidgets.QListWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasklist.sizePolicy().hasHeightForWidth())
        self.tasklist.setSizePolicy(sizePolicy)
        self.tasklist.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.tasklist.setFont(font)
        self.tasklist.setObjectName("tasklist")
        self.deleteButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.cald, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "日程计算器"))
        self.factButton.setText(_translate("MainWindow", "!"))
        self.rightButton.setText(_translate("MainWindow", ")"))
        self.mutiButton.setText(_translate("MainWindow", "×"))
        self.squareButton.setText(_translate("MainWindow", "x²"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.sinButton.setText(_translate("MainWindow", "sin"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9 "))
        self.cosButton.setText(_translate("MainWindow", "cos"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cubeButton.setText(_translate("MainWindow", "x³"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.sixButton.setText(_translate("MainWindow", "6 "))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.piButton.setText(_translate("MainWindow", "π"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.leftButton.setText(_translate("MainWindow", "("))
        self.delButton.setText(_translate("MainWindow", "←"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.tanButton.setText(_translate("MainWindow", "tan"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.divdButton.setText(_translate("MainWindow", "÷"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sqrtButton.setText(_translate("MainWindow", "√x"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calc), _translate("MainWindow", "计算器"))
        self.addButton.setText(_translate("MainWindow", "添加新日程"))
        self.deleteButton.setText(_translate("MainWindow", "删除日程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cald), _translate("MainWindow", "日程表"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
