import os
import pathlib

from buttonpython.settings import BASE_DIR


#def func1():
#    f = open(os.path.join(BASE_DIR, 'templates', 'demofile.txt'), "r")
#    return f.readlines()

def func1():
    return (pathlib.Path(BASE_DIR)/'templates'/'demofile.txt').read_text()