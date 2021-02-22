def execute():
    from subprocess import Popen
    from app import terminal_executable, terminal_execute_parameter
    Popen([terminal_executable,terminal_execute_parameter,'python3','-m','jupyter_console'])