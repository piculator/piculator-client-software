from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
import requests

from app.base_ui.registerwindow_base import Ui_RegisterWindow


class RegisterWindow(QDialog, Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('assets/piculator.ico'))
        self.piculatorLogoLable.setStyleSheet(
            'QLabel {background-image: url("assets/banner.png");background-position: center; background-repeat: no-repeat;}')
        self.registerButton.clicked.connect(self.handleRegister)
        self.identity = self.username = self.password = self.re_password = None
        self.warning = None
        self.allow_register = None
        self.data = None
        self._result = None
        self.registered = False

    def handleRegister(self):

        # 将单选框选项转为字符串
        if self.studentRadioButton.isChecked():
            self.identity = 'S'
        elif self.teacherRadioButton.isChecked():
            self.identity = 'T'
        elif self.otherRadioButton.isChecked():
            self.identity = 'O'
        else:
            self.identity = ''

        self.username = self.usernameLineEdit.text()
        self.password = self.passwordLineEdit.text()
        self.re_password = self.rePasswordLineEdit.text()
        from app import myapp
        myapp.login_manager.server_url = self.serverLineEdit.text()

        if not (self.username and self.password and self.re_password and self.identity and myapp.login_manager.register_url):
            self.allow_register = False
            self.warning = "表单信息不完整"
        elif not self.serviceItemCheckBox.isChecked():
            self.allow_register = False
            self.warning = "须同意服务条款才可继续"
        elif self.password != self.re_password:
            self.allow_register = False
            self.warning = "重复密码不一致，请重新输入"
        else:
            self.allow_register = True

        if self.allow_register:
            self.data = {
                "username": self.username,
                "password": self.password,
                "identity": self.identity,
                "is_from_client": True,
            }
            try:
                self._result = requests.post(myapp.login_manager.register_url, self.data).json()
            except:
                self._result = {
                    'is_registered': False,
                    'message': '网络错误, 请检查网络连接和服务器地址'
                }
            if self._result['is_registered']:
                self.registered = True
                QMessageBox.about(self, "注册成功", self._result['message'])
                self.close()
            else:
                QMessageBox.warning(self, "来自服务器的警告", self._result['message'])
        else:
            QMessageBox.warning(self, "警告", self.warning)
