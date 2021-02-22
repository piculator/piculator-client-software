from app import terminal_executable


def execute():
    from subprocess import Popen
    Popen([terminal_executable])
