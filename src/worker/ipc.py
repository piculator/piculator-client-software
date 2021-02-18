from multiprocessing.connection import Listener, Connection
from time import sleep
from typing import Union
from multiprocessing.connection import Client

from worker import secret_key
from worker import port
from worker import thread_unsafe_globals


class Commander:
    def __init__(self, pport, auth_key):
        self.address = ('localhost', pport)
        self.auth_key = auth_key
        self.connection = None
        self.connected = False

    def connect(self):
        try:
            self.connection = Client(self.address, authkey=bytes(self.auth_key, encoding='utf-8'))
            self.connected = True
            return True
        except:
            return False

    def send(self, msg):
        self.connection.send(msg)

    def close(self):
        self.connection.close()


from worker import jupyter_notebook

address = ('localhost', port)
listener: Union[Listener, None] = None
conn: Union[Connection, None] = None


def event_loop():
    while True:
        msg = conn.recv()
        if msg == 'get-token':
            print(f'[worker-{port}]: waiting for notebook to start.')
            while 'notebook_handler' not in thread_unsafe_globals and not thread_unsafe_globals[
                'notebook_handler'].running:
                print('.')
            msg = ['jupyter-token', thread_unsafe_globals['notebook_handler'].app.token]
            t = 0
            while not jupyter_notebook.commander.connect():
                sleep(1)
                t += 1
                if t > 120:
                    raise TimeoutError(f'Connection to data_bridge timed out after 120 seconds.')
            jupyter_notebook.commander.send(msg)

        elif msg == 'exit':
            conn.close()
            break
        else:
            pass


def ipc_server():
    global listener, conn
    listener = Listener(address, authkey=bytes(secret_key, encoding='utf-8'))
    conn = listener.accept()
    event_loop()
    listener.close()
