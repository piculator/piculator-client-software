from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from app.base_ui.mainwindow_base import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupAdditionalUi(self, MainWindow):
        for i in range(10):
            for j in range(10):
                self.grid.addWidget(QPushButton(QIcon('../assets/icon/piculator-icon@64.png'), "Hello"), i, j)