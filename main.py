import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from calculator_ui import Ui_MainWindow
from calculator_cal import mywindow
from PyQt5 import QtWidgets,QtCore
#实例化mywindow对象，展示页面
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    icon = QIcon("icon.png")
    #设置窗口图标
    w = mywindow()
    w.setWindowIcon(icon)
    #设置图标
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    #左键小图标打开窗口
    def leftClick(i_reason):
        if i_reason == QSystemTrayIcon.ActivationReason.Trigger:
            w.show()
    tray.activated.connect(leftClick)
    #设置小图标菜单栏
    menu = QMenu()
    quit = QAction("退出")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
    tray.setContextMenu(menu)
    
    w.show()
    sys.exit(app.exec_())

