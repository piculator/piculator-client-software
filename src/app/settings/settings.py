from functools import partial

from easysettings import YAMLSettings, load_yaml_settings

settings = load_yaml_settings('config.yml')
settings.__dict__['custom_save'] = partial(settings.save, 'config.yml')
