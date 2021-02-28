def execute():
    from subprocess import Popen
    from app import settings
    Popen([settings['terminal_executable'], settings['terminal_execute_parameter'], 'python3', '-m', 'jupyter_console'],cwd='/home/pi')
