from PyQt5.QtCore import QUrl

from app import myapp


def webbrowser_test():
    w = myapp.get_new_wild_web_window()
    w.browser.setUrl(QUrl(myapp.mainwindow.searchbox.text()))
    w.show()
