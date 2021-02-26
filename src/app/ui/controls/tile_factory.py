from PyQt5.QtWidgets import QPushButton


def make_tile(imgpath: str, text: str, tooltip: str, action) -> QPushButton:
    btn = QPushButton()
    btn.setFixedWidth(140)
    btn.setFixedHeight(100)
    # btn.setText(text)
    btn.setToolTip(tooltip)
    btn.setWhatsThis(tooltip)
    btn.setStyleSheet('QPushButton {background-image: url("'+imgpath+f'");background-position: center; background-repeat: no-repeat;}}')
    btn.clicked.connect(action)
    return btn
