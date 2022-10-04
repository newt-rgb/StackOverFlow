from PyQt5.QtWidgets import QDialog,QDialogButtonBox,QVBoxLayout,QLabel

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入错误！")
        self.resize(320, 180)
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.layout = QVBoxLayout()
        message = QLabel("输入错误，请重新输入！")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)