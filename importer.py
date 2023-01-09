import importlib

def imports():
    globals()["math"] = importlib.import_module("math")