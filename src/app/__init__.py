import sys
import os

from PyQt5.QtWidgets import QApplication

from app.pcsapp import PCSApp
from app.auth.login_manager import LoginManager
from app.constants import *
from app.constants import Ports as ports
from app.settings import settings


os.environ['DISPLAY'] = ':0.0'
myapp = PCSApp()
myapp.qapp = QApplication(sys.argv)
myapp.login_manager = LoginManager()
from app.ui.mainwindow import MainWindow
myapp.mainwindow = MainWindow()
