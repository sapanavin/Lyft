"""This is an abstract class battery"""
from abc import ABC, abstractmethod
from datetime import date



class Battery(ABC):
   
    
    """This will flag if battery needs to get service immediately"""
    def __init__(self):
        pass

    @abstractmethod
    def battery_needs_service(self):
        """this will check if battery needs to service or not?"""
