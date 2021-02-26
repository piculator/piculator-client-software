from app import settings, myapp

retry_cnt = 5
while retry_cnt > 0 and not myapp.login_manager.auto_login():
    retry_cnt -= 1

if not myapp.login_manager.logged_in:
    myapp.login_manager.process_manual_login()
else:
    myapp.mainwindow.showMaximized()
    myapp.qapp.exec()
settings.custom_save()
