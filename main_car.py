
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from abc import ABC






class Parent(ABC):
    def __init__(self):
        print("from Base class")

print("from parent")
m = Model("calliope")
m.model_details()