from multiprocessing.connection import Listener, Connection
from typing import Union

from worker import secret_key
from worker import port

address = ('localhost', port)
listener: Union[Listener, None] = None
conn: Union[Connection, None] = None


def event_loop():
    while True:
        msg = conn.recv()

        if msg == 'exit':
            conn.close()
        break


def ipc_server():
    global listener, conn
    listener = Listener(address, authkey=bytes(secret_key, encoding='utf-8'))
    conn = listener.accept()
    event_loop()
    listener.close()
