from app import terminal_executable,terminal_execute_parameter,sage_executable

def execute():
    from subprocess import Popen
    Popen([terminal_executable,terminal_execute_parameter,sage_executable])