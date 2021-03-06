from . import func_settings, func_sage_notebook, \
    func_sage_online_notebook, func_sage_console, \
    func_local_console, func_local_ipython, func_python_ide, \
    func_simple_notepad, func_filesystem_manager, func_sensors, \
    func_spreadsheet, func_documentation, func_learn_python, func_learn_sage, \
    func_piculator_gamma, func_fallback, func_bluetooth, func_stopwatch, func_user_center
from app.logic.func import Function

funcs = [
    Function('Sage笔记本', 'Sagemath 交互式数学笔记本', 'assets/icon/notebook.png', False,
             ['jupyter', 'notebook'],
             func_sage_notebook.execute, None),
    Function('Sage 在线笔记本', 'Sagemath 在线交互式数学笔记本', 'assets/icon/cloud-notebook.png', True,
             ['jupyter', 'notebook', 'cloud'],
             func_sage_online_notebook.execute, func_sage_online_notebook.guest_fallback),
    Function('Sage 终端', 'Sagemath 终端', 'assets/icon/sage-console.png', False,
             ['console', 'terminal', '命令行'], func_sage_console.execute),
    Function('Piculator Gamma', '由 Sympy Gamma 驱动的智能数学引擎', 'assets/icon/gamma.png', False,
             ['steps'], func_piculator_gamma.execute),
    Function('IPython 终端', 'IPython 终端', 'assets/icon/ipython-console.png', False,
             ['console', 'terminal', '命令行'], func_local_ipython.execute),
    Function('Python IDE', 'Python 集成开发环境', 'assets/icon/python-ide.png', False,
             ['编程'], func_python_ide.execute),
    Function('Python 教程', '详细的 Python 入门教程', 'assets/icon/learn-python.png', False,
             ['tutorial', 'documentation'], func_learn_python.execute),
    Function('Sage 教程', '详细的 sagemath 入门教程', 'assets/icon/learn-sage.png', False,
             ['tutorial', 'documentation'], func_learn_sage.execute),
    Function('记事本', '简单记事本', 'assets/icon/notepad.png', False,
             ['notepad'], func_simple_notepad.execute),
    Function('文件管理', '管理文件系统', 'assets/icon/files.png', False,
             ['files'], func_filesystem_manager.execute),
    Function('秒表', '简单的秒表', 'assets/icon/stopwatch.png', False,
             ['stopwatch'], func_stopwatch.execute),
    Function('终端', '本地终端', 'assets/icon/console.png', False,
             ['console', 'terminal', '命令行'], func_local_console.execute),
    Function('使用说明书', 'Piculator 使用说明书', 'assets/icon/documentation.png', False,
             ['instructions', 'documentation', 'readme'], func_documentation.execute),
    Function('用户中心', '用户中心', 'assets/icon/user-center.png', True,
             ['user', 'center', 'portal'], func_user_center.execute, func_fallback.prompt_guest_not_allowed),
    Function('蓝牙分享', '使用蓝牙发送和接收文件', 'assets/icon/bluetooth.png', False,
             ['bluetooth', 'share'], func_bluetooth.execute),
    Function('传感器', '获取传感器数据', 'assets/icon/sensors.png', False,
             ['sensor'], func_sensors.execute),
    Function('电子表格', '可 Python 编程的电子表格', 'assets/icon/spreadsheet.png', False,
             ['spreadsheet'], func_spreadsheet.execute),
    Function('设置', '设置 Piculator 的可选项.', 'assets/icon/settings.png', True,
             ['configuration', 'settings'],
             func_settings.execute, func_settings.guest_fallback)
]


def configure_function_position():
    col, row = 0, 0
    for fun in funcs:
        if col == 5:
            col = 0
            row += 1
        fun.column = col
        fun.row = row
        col += 1
