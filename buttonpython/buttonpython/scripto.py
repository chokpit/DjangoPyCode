def func1():
    f = open("demofile.txt", "r") #I don't know why but the txt file must be in this path: BASE_ROOT/buttonpython/
    return f.readlines()