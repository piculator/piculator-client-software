from notebook.notebookapp import NotebookApp
import worker
import sys

notebook_handler = None


def jupyter_notebook_main():
    notebook_handler.start()


def jupyter_notebook_initialize():
    try:
        app_token = sys.argv[4]

    except:
        print('Invalid arguments!')
        exit(-1)

    global notebook_handler
    notebook_handler = NotebookHandler()
    worker.thread_unsafe_globals['notebook_handler'] = notebook_handler


def jupyter_notebook_finalize():
    pass


class NotebookHandler:
    def __init__(self):
        self.app = NotebookApp()
        self.app.open_browser = False
        self.app.initialize([])
        self.access_url = self.app.display_url[2]

    def stop(self):
        self.app.stop()

    def start(self):
        self.app.start()
