import sys

from app import settings, login_manager
from app.ui.mainwindow import MainWindow
from app.QRunner import RunMainWindow

retry_cnt = 5
while retry_cnt > 0 and not login_manager.auto_login():
    retry_cnt -= 1

if not login_manager.logged_in:
    while not login_manager.login():
        pass

exit_code = RunMainWindow(MainWindow)
settings.custom_save()
sys.exit(exit_code)
