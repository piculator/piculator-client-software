from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from loginwindow_ui import Ui_MainWindow as LoginWindowUi
from registerwindow_ui import Ui_MainWindow as RegisterWindowUi
import requests

# eval无法识别首字母小写的true和false，须预先定义
true, false = True, False

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = LoginWindowUi()
        # 初始化界面
        self.ui.setupUi(self)
        # 导入窗口图标
        self.setWindowIcon(QIcon('./piculator.ico'))
        
        #将loginPushButton按钮连接到handleLogin函数上
        self.ui.loginPushButton.clicked.connect(self.handleLogin)
        self.ui.registerPushButton.clicked.connect(self.openRegisterWindow)

        # 使用界面定义的控件，也是从ui里面访问
        # self.ui.webview.load('http://www.baidu.com')

    def handleLogin(self):

        print('User login')
        # QLineEdit.text()方法可以传入输入的文本
        # self.url = self.ui.serverLineEdit.text()
        self.url = 'http://localhost:5000/login'
        # QCheckBox.isChecked()方法可以传入复选框是否选中的真假值
        self.remember_password = self.ui.rememberPasswordCheckBox.isChecked()
        self.data = {
            "username":self.ui.userLineEdit.text(),
            "password":self.ui.passwordLineEdit.text(),
            "is_from_client":True}
        self.r = eval(requests.post(self.url, self.data).content)
        print(self.r)
        if self.r['is_logged_in']:
            print('登录成功')
        else:
            # QMessageBox.about('标题','正文') 会弹出对话框
            loginFailMessage = QMessageBox.about(self, "登录失败", self.r['reason'])   
   

    def openRegisterWindow(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

class RegisterWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = RegisterWindowUi()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('./piculator.ico'))

        self.ui.registerButton.clicked.connect(self.handleRegister)
        self.ui.loginButton.clicked.connect(self.openLoginWindow)
    
    def handleRegister(self):
        print('User register')

        self.url = "http://localhost:5000/register"
        # 将单选框选项转为字符串
        if self.ui.studentRadioButton.isChecked():
            self.identity = 'S'
        elif self.ui.teacherRadioButton.isChecked():
            self.identity = 'T'
        elif self.ui.otherRadioButton.isChecked():
            self.identity = 'O'
        else:
            self.identity = ''
        
        self.username, self.password, self.re_password = \
            self.ui.usernameLineEdit.text(), \
            self.ui.passwordLineEdit.text(), \
            self.ui.rePasswordLineEdit.text()
        
        if not (self.username and self.password and self.re_password and self.identity):
            self.allow_register = False
            self.warning = "表单信息不完整"
        elif not self.ui.serviceItemCheckBox.isChecked():
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
            self.r = eval(requests.post(self.url, self.data).content)
            print(self.r)
            if self.r['is_registered']:
                registerSucceedMessage = QMessageBox.about(self, "注册成功", self.r['message'])
            else:
                registerFailedWarning = QMessageBox.warning(self, "来自服务器的警告", self.r['message'])
        else:
            registerNotAllowedWarning = QMessageBox.warning(self, "警告", self.warning)
    
    def openLoginWindow(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


app = QApplication([])
window = LoginWindow()
window.show()
app.exec_()