from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from loginwindow_ui import Ui_MainWindow as LoginWindowUi
from registerwindow_ui import Ui_MainWindow as RegisterWindowUi


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
        self.server = self.ui.serverLineEdit.text()
        self.user = self.ui.userLineEdit.text()
        self.password = self.ui.passwordLineEdit.text()
        # QCheckBox.isChecked()方法可以传入复选框是否选中
        self.remember_password = self.ui.rememberPasswordCheckBox.isChecked()
        self.lis = [self.server, self.user, self.password, self.remember_password]
        print(self.lis)

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

        self.username = self.ui.usernameLineEdit.text()
        self.password = self.ui.passwordLineEdit.text()
        self.re_password = self.ui.rePasswordLineEdit.text()
        if self.ui.studentRadioButton.isChecked():
            self.identity='S'
        elif self.ui.teacherRadioButton.isChecked():
            self.identity='T'
        elif self.ui.otherRadioButton.isChecked():
            self.identity='O'
        self.service_item = self.ui.serviceItemCheckBox.isChecked()
        self.lis=[
            self.username, self.password, self.re_password,
            self.identity, self.service_item]
        print(self.lis)
    
    def openLoginWindow(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


app = QApplication([])
window = LoginWindow()
window.show()
app.exec_()