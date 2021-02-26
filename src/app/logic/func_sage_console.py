from app import settings


def execute():
    from subprocess import Popen
    Popen([settings['terminal_executable'], settings['terminal_execute_parameter'], settings['sage_executable']])
