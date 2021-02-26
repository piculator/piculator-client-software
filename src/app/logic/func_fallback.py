from PyQt5.QtWidgets import QMessageBox


def prompt_func_not_implemented():
    from app import myapp
    QMessageBox.warning(myapp.mainwindow.centralwidget, '警告', '很抱歉, 此功能暂未实现', QMessageBox.Ok)


def prompt_guest_not_allowed():
    from app import myapp
    QMessageBox.warning(myapp.mainwindow.centralwidget, '警告', '您需要登录才能使用此功能!无法以访客身份继续')
