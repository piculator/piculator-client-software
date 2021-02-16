from app.utils.singleton import singleton


@singleton
class PCSApp:
    def __init__(self):
        self.webbrowser_testwindow = None
        self.qapp = None
        self.mainwindow = None
        self.qmainwindow = None
        self.notebook_handler = None
