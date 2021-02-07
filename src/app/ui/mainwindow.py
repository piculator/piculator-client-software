from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QMessageBox
from app.ui.controls.tile_factory import make_tile
from app.base_ui.mainwindow_base import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def show_message_box(self):
        msg=QMessageBox()
        msg.setText("Text")
        msg.setWindowTitle("Hello")
        msg.exec()

    def setupAdditionalUi(self, MainWindow):
        for i in range(5):
            for j in range(5):
                self.grid.addWidget(make_tile('../assets/icon/piculator-icon@64.png',"Hello", self.show_message_box), i, j)