def execute():
    from app import myapp
    w = myapp.get_new_wild_web_window()
    from PyQt5.QtCore import QUrl
    w.browser.setUrl(QUrl.fromLocalFile('/usr/share/doc/piculator/sage/html/en/index.html'))
    w.showMaximized()