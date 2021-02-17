from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from app import myapp


def RunMainWindow(ui):
    myapp.qapp = QApplication(sys.argv)
    myapp.qmainwindow = QMainWindow()
    myapp.mainwindow = ui()
    myapp.mainwindow.setupUi(myapp.qmainwindow)
    myapp.mainwindow.setupAdditionalUi(myapp.qmainwindow)
    myapp.qmainwindow.show()
    return myapp.qapp.exec()
