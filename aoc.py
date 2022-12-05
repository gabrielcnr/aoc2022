import inspect
from pathlib import Path


def read_input(test=False):
    stack = inspect.stack()[:]
    filename = stack[1].filename
    p = Path(filename)
    if test:
        name = p.name.replace('day', 'test')
        input_path = p.with_name(name).with_suffix('.txt')
    else:
        input_path = p.with_suffix('.txt')
    return input_path.read_text().splitlines()
