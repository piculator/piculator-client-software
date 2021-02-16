from worker.ipc import ipc_server, listener
from threading import Thread
from worker import command, command_mapping

server_thread = Thread(target=ipc_server)
server_thread.start()

command_mapping[command]()
