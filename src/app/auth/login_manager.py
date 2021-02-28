from app.utils import singleton
from app.auth.user import User
from app.ui.loginwindow import LoginWindow


@singleton
class LoginManager:
    def __init__(self):
        self.logged_in = False
        self.user = User('guest')
        self.login_window = LoginWindow()
        self.server_url = ''

    def auto_login(self):
        return False

    @property
    def is_guest(self):
        return self.user.is_guest

    def process_manual_login(self):
        from app import myapp
        self.login_window.showMaximized()
        myapp.qapp.exec()
    
    def _url_append_x(self,page):
        '''parameter page should not begin with /'''
        if self.server_url[-1]=='/':
            return self.server_url + page
        else:
            return self.server_url + '/' + page
    
    @property
    def login_url(self):
        return self._url_append_x('login')
    
    @property
    def register_url(self):
        return self._url_append_x('register')
