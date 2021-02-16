import sys
from worker.jupyter_notebook import jupyter_notebook_main
from functools import reduce

try:
    secret_key = sys.argv[3]
    port = int(sys.argv[2])
    command = sys.argv[1]
except:
    print('Invalid arguments!')
    exit(-1)

command_mapping = {
    'jupyter-notebook': jupyter_notebook_main,
    'python-ide': None,
    'system-upgrade': None,
    'test-server': None
}

if command not in command_mapping:
    print(f'Command not found: {command}')
    print(f'Available commands are here: {reduce(lambda x, y: x + ", " + y, command_mapping.keys())}')
    exit(-1)
