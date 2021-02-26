from PyQt5 import QtGui
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget, QMessageBox

from app.base_ui.jupytermanager_base import Ui_JupyterManagerWindow
from app import myapp
from app.logic.func_fallback import prompt_func_not_implemented


class JupyterManagerWindow(Ui_JupyterManagerWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectSignals()

    def closeEvent(self, ev: QCloseEvent):
        result = QMessageBox.warning(self, '警告', '关闭此窗口将停止 Jupyter notebook, 是否继续?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if result == QMessageBox.Yes:
            from app.logic.func_sage_notebook import shutdown
            shutdown()
            myapp.jupyter_manager_window = None
        else:
            ev.setAccepted(False)

    def setJupyterStatus(self, s):
        self.jupyterStatus.setText(s)

    def _openBrowser(self):
        from app.logic.func_sage_notebook import wrapper
        wrapper.openBrowser()

    def connectSignals(self):
        from app.logic.func_sage_notebook import shutdown,terminate
        self.stopServer.clicked.connect(shutdown)
        self.forceStopServer.clicked.connect(terminate)
        self.openBrowser.clicked.connect(self._openBrowser)
        self.openJupyterToturial.clicked.connect(prompt_func_not_implemented)
        self.openPythonInteractiveToturial.clicked.connect(prompt_func_not_implemented)
        self.openSageInteractiveToturial.clicked.connect(prompt_func_not_implemented)
