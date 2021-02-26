from app.utils import singleton
from PyQt5.QtNetwork import QNetworkAccessManager


@singleton
class PCSApp:
    def __init__(self):
        self.qapp = None
        self.mainwindow = None
        self.notebook_handler = None
        self.data_bridge = None
        self.q_network_access_manager = QNetworkAccessManager()
        self.web_windows = {}
        self._current_web_window_ref_key = 0
        self.jupyter_manager_window = None
        self.bluetooth_window = None
        self.login_manager = None

    def get_web_window_ref_key(self):
        self._current_web_window_ref_key += 1
        return self._current_web_window_ref_key - 1

    def get_new_wild_web_window(self):
        from app.ui.webwindow import WebWindow
        w = WebWindow()
        w.browser_ref_key = self.get_web_window_ref_key()
        self.web_windows[w.browser_ref_key] = w
        return w
