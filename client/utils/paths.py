import os


def get_full_path(path):
    value = os.path.join(os.path.dirname(__file__), "..", path)
    return value
