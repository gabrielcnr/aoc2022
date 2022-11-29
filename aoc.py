import inspect
from pathlib import Path


def read_input():
    stack = inspect.stack()[:]
    filename = stack[1].filename
    return Path(filename).with_suffix('.txt').read_text()
