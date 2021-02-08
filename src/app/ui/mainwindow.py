from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QMessageBox

from app.logic.funcs_list import funcs
from app.ui.controls.tile_factory import make_tile
from app.base_ui.mainwindow_base import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def show_message_box(self):
        msg = QMessageBox()
        msg.setText("Text")
        msg.setWindowTitle("Hello")
        msg.exec()

    def search_funcs(self):
        s = self.searchbox.text()
        for func in funcs:
            if not func.search(s):
                func.tile.setHidden(True)
            else:
                func.tile.setHidden(False)

    def setupAdditionalUi(self, MainWindow):
        self.search_btn.clicked.connect(self.search_funcs)
        for func in funcs:
            func.generate_tile()
            self.gridLayout.addWidget(func.tile, func.row, func.column)
