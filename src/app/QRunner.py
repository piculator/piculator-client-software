from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def RunMainWindow(ui):
    qapp = QApplication(sys.argv)
    mainwindow = QMainWindow()
    mwui = ui()
    mwui.setupUi(mainwindow)
    mwui.setupAdditionalUi(mainwindow)
    mainwindow.show()
    sys.exit(qapp.exec())
