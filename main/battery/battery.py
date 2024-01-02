"""This is an abstract class battery"""
from abc import ABC, abstractmethod



class Battery(ABC):
    """This will flag if battery needs to get service immediately"""
    def __init__(self, battery_last_service_date):
        self.battery_last_service_date = battery_last_service_date

    @abstractmethod
    def battery_needs_service(self):
        """this will check if battery needs to service or not?"""

    @abstractmethod
    def battery_should_be_serviced(self):
        """This will flag if battery needs to get service immediately"""