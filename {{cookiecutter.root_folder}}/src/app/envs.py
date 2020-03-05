import os
from distutils import util


def get_string(name, default=None):
    return os.environ.get(name, default)


def get_bool(name, default=True):
    val = os.environ.get(name)
    if val:
        return util.strtobool(val)
    else:
        return default


def get_int(name, default=0):
    val = os.environ.get(name)
    if val:
        return int(val)
    else:
        return default
