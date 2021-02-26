from app.ui.bluetoothwindow import BluetoothWindow
from app import myapp


def execute():
    myapp.bluetooth_window=BluetoothWindow()
    myapp.bluetooth_window.showMaximized()
