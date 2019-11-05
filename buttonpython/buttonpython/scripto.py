import os
from buttonpython.settings import BASE_DIR


def func1():
    f = open(os.path.join(BASE_DIR, 'templates', 'demofile.txt'), "r") #I don't know why but the txt file must be in this path: BASE_ROOT/buttonpython/
    return f.readlines()