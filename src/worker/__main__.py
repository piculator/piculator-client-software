from worker.ipc import ipc_server, listener
from threading import Thread
from worker import command, command_mapping

command_mapping[command][0]()
command_mapping[command][1]()
command_mapping[command][2]()
