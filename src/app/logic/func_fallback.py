from PyQt5.QtWidgets import QMessageBox
from app import myapp

def prompt_func_not_implemented():
    QMessageBox.warning(myapp.mainwindow.centralwidget ,'警告','很抱歉, 此功能暂未实现',QMessageBox.Ok)