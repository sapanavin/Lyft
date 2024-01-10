
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from abc import ABC

from main.tyre.carrigan import CarriganTyre

class Parent(ABC):
    def __init__(self):
        print("from Base class")

print("from parent")
carriganTyreObj = CarriganTyre()
carriganTyreObj.wear_arr[0]=0.9
carriganTyreObj.wear_arr[1]=0.9
carriganTyreObj.wear_arr[2]=0.9
carriganTyreObj.wear_arr[3]=0.9

print( carriganTyreObj.tyre_needs_service() )