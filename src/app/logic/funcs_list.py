from . import func_settings, func_sage_notebook, \
    func_sage_online_notebook, func_sage_console, \
    func_local_console, func_local_ipython, func_python_ide, \
    func_simple_notepad, func_filesystem_manager, func_sensors, \
    func_spreadsheet, func_documentation, func_learn_python, func_learn_sage, func_test
from app.logic.func import Function

funcs = [
    Function('设置', '设置 Piculator 的可选项.', 'assets/icon/piculator-icon@64.png', True,
             ['configuration', 'settings'],
             func_settings.execute, func_settings.guest_fallback),
    Function('Sage笔记本', 'Sagemath 交互式数学笔记本', '<null>', False,
             ['jupyter', 'notebook'],
             func_sage_notebook.execute, None),
    Function('Sage 在线笔记本', 'Sagemath 在线交互式数学笔记本', '<null>', True,
             ['jupyter', 'notebook', 'cloud'],
             func_sage_online_notebook.execute, func_sage_online_notebook.guest_fallback),
    Function('Sage 终端', 'Sagemath 终端', '<null>', False,
             ['console', 'terminal', '命令行'], func_sage_console.execute),
    Function('终端', '本地终端', '<null>', False,
             ['console', 'terminal', '命令行'], func_local_console.execute),
    Function('IPython 终端', 'IPython 终端', '<null>', False,
             ['console', 'terminal', '命令行'], func_local_ipython.execute),
    Function('Python IDE', 'Python 集成开发环境', '<null>', False,
             ['编程'], func_python_ide.execute),
    Function('记事本', '简单记事本', '<null>', False,
             ['notepad'], func_simple_notepad.execute),
    Function('文件管理', '管理文件系统', '<null>', False,
             ['files'], func_filesystem_manager.execute),
    Function('传感器', '获取传感器数据', '<null>', False,
             ['sensor'], func_sensors.execute),
    Function('电子表格', '可 Python 编程的电子表格', '<null>', False,
             ['spreadsheet'], func_spreadsheet.execute),
    Function('使用说明书', 'Piculator 使用说明书', '<null>', False,
             ['instructions', 'documentation', 'readme'], func_documentation.execute),
    Function('Python 教程', '详细的 Python 入门教程', '<null>', False,
             ['tutorial', 'documentation'], func_learn_python.execute),
    Function('Sage 教程', '详细的 sagemath 入门教程', '<null>', False,
             ['tutorial', 'documentation'], func_learn_sage.execute),
    Function('测试-Web browser', 'Web browser Test', '<null>', False,
             [], func_test.webbrowser_test)
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
