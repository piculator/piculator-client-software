from app.pcsapp import PCSApp
from app.auth.login_manager import LoginManager
from app.constants import *
from app.constants import Ports as ports
from app.settings import settings
import os

os.environ['DISPLAY'] = ':0.0'
login_manager = LoginManager()
myapp = PCSApp()
