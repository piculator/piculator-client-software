from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtBoundSignal, QUrl
from PyQt5.QtWidgets import QMessageBox

from app.ipc import DataBridge
from app import myapp
from subprocess import Popen
from app import settings, ports
from app.ipc.commander import Commander
from app.ui.jupytermgrwindow import JupyterManagerWindow
from app.utils import generate_token
import os

commander = None
worker_token = generate_token()
worker_port = ports.get_worker_port()
wrapper = None
worker_proc = None

class NotebookThreadCommunicationWrapper(QObject):
    on_token_received = pyqtSignal(str)
    token = None

    def __init__(self):
        super().__init__()
        self.on_token_received.connect(self.process_token_received)

    def process_token_received(self, tk):
        myapp.jupyter_manager_window.setJupyterStatus('正在运行')
        self.openBrowser()

    def openBrowser(self):
        w = myapp.get_new_wild_web_window()
        w.browser.setUrl(QUrl(f'http://127.0.0.1:8888/tree?token={self.token}'))
        w.show()

    def data_bridge_thread_on_token_received(self, tk):
        self.token = tk
        self.on_token_received.emit(tk)


def execute():
    if myapp.data_bridge is not None and myapp.data_bridge.thread.is_alive():
        QMessageBox.warning(myapp.mainwindow,"警告","此功能已在运行中, 不能重复启动",QMessageBox.Ok)
    else:
        myapp.data_bridge = DataBridge()
    global wrapper
    wrapper = NotebookThreadCommunicationWrapper()
    myapp.data_bridge.on_token_received = wrapper.data_bridge_thread_on_token_received
    myapp.jupyter_manager_window = JupyterManagerWindow()
    myapp.jupyter_manager_window.showMaximized()
    myapp.data_bridge.start()
    env = dict(os.environ)
    env['PYTHONPATH'] = os.getcwd()
    global worker_proc
    worker_proc = Popen(
        [settings['sage_python_interpreter'], '-m', 'worker', 'jupyter-notebook',
         str(worker_port), worker_token,
         str(ports.data_bridge), myapp.data_bridge.token], env=env)
    myapp.jupyter_manager_window.setJupyterStatus('子进程已启动')
    global commander
    commander = Commander(worker_port, worker_token)
    t = 0
    # TODO: 不建议在UI线程上执行长时间任务, 会导致界面假死, 改写为异步或者多线程
    while not commander.connect():
        myapp.jupyter_manager_window.setJupyterStatus('正在连接到子进程...')
        sleep(1)
        t += 1
        if t > 120:
            myapp.jupyter_manager_window.setJupyterStatus('错误: 连接到子进程时出错')
            break
    else:
        myapp.jupyter_manager_window.setJupyterStatus('已连接到子进程,等待子进程消息')
        commander.send('get-token')

def shutdown():
    try:
        commander.send('exit')
        myapp.jupyter_manager_window.setJupyterStatus('正在/已停止')
    except BrokenPipeError:
        myapp.jupyter_manager_window.setJupyterStatus('已断开连接')

def terminate():
    worker_proc.kill()
    myapp.jupyter_manager_window.setJupyterStatus('已强行停止')