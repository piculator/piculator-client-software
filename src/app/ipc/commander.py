from multiprocessing.connection import Client


def send_msg(port, auth_key, msg):
    address = ('localhost', port)
    conn = Client(address, authkey=auth_key)
    conn.send(msg)
