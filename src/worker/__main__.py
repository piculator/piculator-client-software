from worker.ipc import ipc_server, listener
from threading import Thread
from worker import command, command_mapping

server_thread = Thread(target=ipc_server)
server_thread.setDaemon(True)
server_thread.start()

print(server_thread.is_alive())

command_mapping[command][0]()
command_mapping[command][1]()
command_mapping[command][2]()
