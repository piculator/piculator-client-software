from PyQt5.QtWebKitWidgets import QWebView
from app import myapp


class BrowserView(QWebView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createWindow(self, wtype):
        w = myapp.get_new_wild_web_window()
        w.show()
        return w.browser
