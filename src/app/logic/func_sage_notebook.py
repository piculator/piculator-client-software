from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtBoundSignal, QUrl

from app.ipc import DataBridge
from app import myapp
from subprocess import Popen
from app import sage_python_interpreter, ports
from app.ipc.commander import Commander
from app.ui.webwindow import WebWindow
from app.utils import generate_token
import os

commander = None


class NotebookThreadCommunicationWrapper(QObject):
    on_token_received = pyqtSignal(str)
    token = None

    def __init__(self):
        super().__init__()
        self.on_token_received.connect(self.process_token_received)

    def process_token_received(self, tk):
        w = myapp.get_new_wild_web_window()
        w.browser.setUrl(QUrl(f'http://127.0.0.1:8888/tree?token={tk}'))
        w.show()

    def data_bridge_thread_on_token_received(self, tk):
        self.token = tk
        self.on_token_received.emit(tk)


def execute():
    if myapp.data_bridge is None:
        myapp.data_bridge = DataBridge()
    wrapper = NotebookThreadCommunicationWrapper()
    myapp.data_bridge.on_token_received = wrapper.data_bridge_thread_on_token_received
    # wrapper.on_token_received.connect(wrapper.process_token_received)
    myapp.data_bridge.start()
    worker_token = generate_token()
    worker_port = ports.get_worker_port()
    env = dict(os.environ)
    env['PYTHONPATH'] = os.getcwd()
    worker_proc = Popen(
        [sage_python_interpreter, '-m', 'worker', 'jupyter-notebook',
         str(worker_port), worker_token,
         str(ports.data_bridge), myapp.data_bridge.token], env=env)
    global commander
    commander = Commander(worker_port, worker_token)
    t = 0
    while not commander.connect():
        sleep(1)
        t += 1
        if t > 120:
            raise TimeoutError(f'Connection to worker-{worker_port} timed out after 120 seconds.')
    commander.send('get-token')
