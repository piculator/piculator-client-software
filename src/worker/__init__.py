import sys
from functools import reduce
from threading import Thread

thread_unsafe_globals = {}

try:
    secret_key = sys.argv[3]
    port = int(sys.argv[2])
    command = sys.argv[1]
except:
    print('Invalid arguments!')
    exit(-1)

from worker.ipc import ipc_server

server_thread = Thread(target=ipc_server)
server_thread.setDaemon(True)

def start_server_thread():
    server_thread.start()

from worker.jupyter_notebook import jupyter_notebook_initialize, jupyter_notebook_main, jupyter_notebook_finalize

command_mapping = {
    'jupyter-notebook': (jupyter_notebook_initialize, jupyter_notebook_main, jupyter_notebook_finalize),
    'python-ide': None,
    'system-upgrade': None,
    'test-server': None
}

if command not in command_mapping:
    print(f'Command not found: {command}')
    print(f'Available commands are here: {reduce(lambda x, y: x + ", " + y, command_mapping.keys())}')
    exit(-1)
