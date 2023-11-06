import pathlib, os

def get_full_path(path):
    current_dir = pathlib.Path().resolve()
    value = os.path.join(current_dir, path)
    return value
