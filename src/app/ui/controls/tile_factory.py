from PyQt5.QtWidgets import QPushButton


def make_tile(imgpath: str, text: str, action) -> QPushButton:
    btn = QPushButton()
    size = 80
    btn.setFixedWidth(size)
    btn.setFixedHeight(size)
    btn.setText(text)
    btn.setStyleSheet('QPushButton {background-image: url("'+imgpath+f'");background-position: center; background-repeat: no-repeat;}}')
    btn.clicked.connect(action)
    return btn