from .func import Function
import func_settings
funcs = [
    Function('设置', '设置 Piculator 的可选项.', '<null>', True,
             ['configuration', 'settings'],
             func_settings.execute,func_settings.guest_fallback),
    Function('设置', '设置 Piculator 的可选项.', '<null>', False,
             ['configuration', 'settings'],
             func_settings.execute,func_settings.guest_fallback),
]
