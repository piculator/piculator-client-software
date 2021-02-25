def execute():
    from app import myapp
    w = myapp.get_new_wild_web_window()
    from PyQt5.QtCore import QUrl
    w.browser.setUrl(QUrl('/usr/share/doc/python3/html/index.html'))
