# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import shutil
import os
from collections import OrderedDict
from configobj import ConfigObj


def _read_configuration(usr_config, def_config=None):
    """Reads the config file if it exists, else reads the default config.

    Internal method, call read_configuration instead.

    Args:
        * usr_config: A string that specifies the config file name.
        * def_config: A string that specifies the config default file name.

    Returns:
        An instance of a ConfigObj.
    """
    usr_config_file = os.path.expanduser(usr_config)
    cfg = ConfigObj()
    cfg.filename = usr_config_file
    if def_config:
        cfg.merge(ConfigObj(def_config, interpolation=False))
    cfg.merge(ConfigObj(usr_config_file, interpolation=False))
    return cfg


def write_default_config(source, destination, overwrite=False):
    """Writes the default config from a template.

    Args:
        * source: A string that specifies the path to the template.
        * destination: A string that specifies the path to write.
        * overwite: A boolean that specifies whether to overwite the file.

    Returns:
        None.
    """
    destination = os.path.expanduser(destination)
    if not overwrite and os.path.exists(destination):
        return
    shutil.copyfile(source, destination)


def read_configuration():
    """Reads the config file if it exists, else reads the default config.

    Args:
        * None

    Returns:
        An instance of a ConfigObj.
    """
    config_template = 'sawsrc'
    config_name = '~/.sawsrc'
    default_config = os.path.join(os.path.dirname(__file__), config_template)
    write_default_config(default_config, config_name)
    return _read_configuration(config_name, default_config)


def get_shortcuts(config):
    """Gets the shortcuts from the specified config.

    Args:
        * config: An instance of ConfigObj

    Returns:
        An OrderedDict containing the shortcut commands as the keys and their
        corresponding full commands as the values.
    """
    return OrderedDict(zip(config['shortcuts'].keys(),
                           config['shortcuts'].values()))
