from app.settings.settings import settings


def set_defaults():
    default_settings = {
        'sage_executable': '/home/pi/sage/sage-9.2/sage',
        'sage_python_interpreter': '/home/pi/sage/sage-9.2/local/bin/python3',
        'terminal_executable': 'x-terminal-emulator',
        'terminal_execute_parameter': '-e'
    }
    for key in default_settings:
        settings.setdefault(key,default_settings[key])
