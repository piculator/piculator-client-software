from notebook.notebookapp import NotebookApp
import os

notebook_handler = None


def jupyter_notebook_main():
    global notebook_handler
    notebook_handler = NotebookHandler()
    notebook_handler.start()


class NotebookHandler:
    def __init__(self):
        self.app = NotebookApp()
        self.app.open_browser = False
        self.app.initialize([])

    def stop(self):
        self.app.stop()

    def start(self):
        self.app.start()
