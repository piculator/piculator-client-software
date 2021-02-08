import platform

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
if platform.system() == "Windows":
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
else:
    from PyQt5.QtWebKitWidgets import QWebView


class WebWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebView()
        self.browser.setUrl(QUrl('https://html5test.com'))
        self.setCentralWidget(self.browser)
