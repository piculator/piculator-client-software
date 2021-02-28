from notebook.notebookapp import NotebookApp
import worker
import sys
from worker.ipc import Commander

notebook_handler = None
commander = None
app_token = None
data_bridge_port = None


def jupyter_notebook_main():
    notebook_handler.start()


def jupyter_notebook_initialize():
    global app_token, data_bridge_port
    try:
        data_bridge_port = int(sys.argv[4])
        app_token = sys.argv[5]
        global commander
        commander = Commander(data_bridge_port, app_token)
    except:
        print('Invalid arguments!')
        exit(-1)
    global notebook_handler
    notebook_handler = NotebookHandler()
    worker.thread_unsafe_globals['notebook_handler'] = notebook_handler
    worker.start_server_thread()


def jupyter_notebook_finalize():
    pass


class NotebookHandler:
    def __init__(self):
        self.app: NotebookApp = NotebookApp()
        self.app.open_browser = False
        self.app.initialize(['--notebook-dir=/home/pi'])
        self.access_url = self.app.display_url[2]
        self.running = False

    def stop(self):
        self.app.stop()
        self.running = False

    def start(self):
        self.running = True
        self.app.start()
