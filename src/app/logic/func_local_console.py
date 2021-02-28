from app import settings


def execute():
    from subprocess import Popen
    Popen([settings['terminal_executable']],cwd='/home/pi')
