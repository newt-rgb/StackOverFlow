import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calculator_ui import Ui_MainWindow
from calculator_cal import mywindow
#实例化mywindow对象，展示页面

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())

