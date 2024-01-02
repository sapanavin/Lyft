from abc import ABC

from main.model.model import Model




class Parent(ABC):
    def __init__(self):
        print("from Base class")

print("from parent")
m = Model("calliope")
m.model_details()