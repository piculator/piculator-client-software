def execute():
    from app import myapp
    from PyQt5.QtCore import QUrl
    w = myapp.get_new_wild_web_window()
    w.browser.setUrl(QUrl(myapp.login_manager.server_url))
