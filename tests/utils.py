import os

from .compat import text_type


def ensure_bytes(key):
    if isinstance(key, text_type):
        key = key.encode('utf-8')

    return key


def ensure_unicode(key):
    if not isinstance(key, text_type):
        key = key.decode()

    return key


def key_path(key_name):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'keys', key_name)
