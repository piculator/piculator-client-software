import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from app.base_ui.loginwindow_base import Ui_LoginWindow
from app.ui.registerwindow import RegisterWindow


class LoginWindow(QMainWindow, Ui_LoginWindow):

    def __init__(self):
        super().__init__()
        # 初始化界面
        self.setupUi(self)
        # 导入窗口图标
        self.setWindowIcon(QIcon('assets/piculator.ico'))

        # 将loginPushButton按钮连接到handleLogin函数上
        self.loginPushButton.clicked.connect(self.handleLogin)
        self.registerPushButton.clicked.connect(self.openRegisterWindow)
        self.guestModePushButton.clicked.connect(self.enterGuestMode)

        # 使用界面定义的控件，也是从ui里面访问
        # self.ui.webview.load('http://www.baidu.com')
        self.register_window = None
        self.logged_in = None
        self.remember_password = None
        self.url = ''
        self.data = None
        self._result = None
        self.label.setStyleSheet(
            'QLabel {background-image: url("assets/banner.png");background-position: center; background-repeat: no-repeat;}')

    def handleLogin(self):
        # QLineEdit.text()方法可以传入输入的文本
        # self.url = self.ui.serverLineEdit.text()
        # QCheckBox.isChecked()方法可以传入复选框是否选中的真假值
        self.remember_password = self.rememberPasswordCheckBox.isChecked()
        self.data = {
            "username": self.userLineEdit.text(),
            "password": self.passwordLineEdit.text(),
            "is_from_client": True
        }
        self.url = self.serverLineEdit.text()
        try:
            self._result = requests.post(self.url, self.data).json()
        except:
            self._result = {
                'is_logged_in': False,
                'reason': "网络错误, 请检查网络连接和服务器地址"
            }
        if self._result['is_logged_in']:
            from app import myapp
            myapp.login_manager.user.username = self.data['username']
            myapp.login_manager.logged_in = True
            myapp.login_manager.server_url = self.url
            myapp.mainwindow.showMaximized()
            self.close()
            myapp.login_manager.login_window = None
        else:
            # QMessageBox.about('标题','正文') 会弹出对话框
            QMessageBox.about(self, "登录失败", self._result['reason'])

    def openRegisterWindow(self):
        self.register_window = RegisterWindow()
        self.register_window.exec()
        if self.register_window.registered:
            self.logged_in = True
            from app import myapp
            myapp.login_manager.user.username = self.register_window.data['username']
            myapp.login_manager.server_url = self.register_window.url
            myapp.login_manager.logged_in = True
            myapp.mainwindow.showMaximized()
            self.close()
            myapp.login_manager.login_window = None

    def enterGuestMode(self):
        from app import myapp
        myapp.login_manager.user.username = 'guest'
        myapp.login_manager.logged_in = True
        myapp.mainwindow.showMaximized()
        self.close()
        myapp.login_manager.login_window = None
