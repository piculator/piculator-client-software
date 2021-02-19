import platform

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from app import myapp
from app.ui.browser import BrowserView


class WebWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.browser = BrowserView()
        self.setCentralWidget(self.browser)
        self.browser.page().setNetworkAccessManager(myapp.q_network_access_manager)
        self.browser_ref_key = None

    def closeEvent(self, qce):
        if self.browser_ref_key is not None:
            self.browser.destroy()
            # self.browser.stop()
            myapp.web_windows[self.browser_ref_key]=None
        qce.accept()
