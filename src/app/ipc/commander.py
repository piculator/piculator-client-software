from multiprocessing.connection import Client


class Commander:
    def __init__(self, port, auth_key):
        self.address = ('localhost', port)
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
