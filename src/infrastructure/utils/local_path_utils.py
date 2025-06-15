import os


def get_root_path():
    current_path = __file__
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_path))))


def get_resources_path():
    root_path = get_root_path()
    return os.path.join(root_path, 'resources')


def get_src_path():
    root_path = get_root_path()
    return os.path.join(root_path, 'src')
