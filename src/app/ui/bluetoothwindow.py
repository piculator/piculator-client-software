from PyQt5.QtWidgets import QWidget

from app.base_ui.bluetoothwindow_base import Ui_BluetoothSharingWindow
from bluetooth import discover_devices

from app.logic.func_fallback import prompt_func_not_implemented


class BluetoothWindow(Ui_BluetoothSharingWindow,QWidget):
    def __init__(self):
        super().__init__()

    def connectSignals(self):
        self.refreshDeviceList.clicked.connect(self.scan_devices_and_update)

    def scan_devices_and_update(self):
        self.combo_devices.addItems(discover_devices())

    def showEvent(self, a0):
        prompt_func_not_implemented()