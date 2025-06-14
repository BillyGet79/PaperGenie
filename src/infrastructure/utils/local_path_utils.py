import os


def get_root_path():
    current_path = __file__
    return os.path.dirname(os.path.dirname(os.path.dirname(current_path)))