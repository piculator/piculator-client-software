from multiprocessing.connection import Listener
from threading import Thread, Event
from app import ports
from app.utils import generate_token


class DataBridge:
    def __init__(self, port: int = None):
        self.port = ports.data_bridge if port is None else port
        self.address = ('localhost', self.port)
        self.token = generate_token()
        self.listener = Listener(self.address, authkey=bytes(self.token, encoding='utf-8'))
        self.stop_event = Event()
        self.thread = Thread(target=self._run)
        self.thread.setDaemon(True)
        self.connection = None
        self.on_token_received = None

    def start(self):
        self.thread.start()

    def _run(self):
        self.connection = self.listener.accept()
        while not self.stop_event.is_set():
            msg = self.connection.recv()
            print(f'[DataBridge]: Received message: {msg}')
            if msg[0] == 'jupyter-token':
                if callable(self.on_token_received): self.on_token_received(msg[1])
            elif msg == 'exit':
                self.connection.close()
                break
        self.listener.close()

    def stop(self):
        self.stop_event.set()
        print('[DataBridge]: stop event has been set.')
