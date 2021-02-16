from app.ui.mainwindow import MainWindow
from app.QRunner import RunMainWindow
import app

retry_cnt = 5
while retry_cnt > 0 and not app.login_manager.auto_login():
    retry_cnt -= 1

if not app.login_manager.logged_in:
    while not app.login_manager.login():
        pass

RunMainWindow(MainWindow)
