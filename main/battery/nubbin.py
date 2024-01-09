# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

""" this module """
from datetime import date, datetime

from main.battery.battery import Battery


class Nubbin(Battery):

    battery_current_date: date
    battery_last_service_date: date

    """this class is child of Battery"""
    def __init__(self, battery_current_date, battery_last_service_date):

        """Checking battery_last_service_date must be of type date otherwise raises a value Error"""
        if not isinstance(battery_last_service_date, date):
            raise ValueError("battery_last_service_date must be of type date.")
        
        """Checking battery_current_date must be of type date otherwise raises a value Error"""
        if not isinstance(battery_current_date, date):
            raise ValueError("battery_current_date must be of type date.")   

        """Checking last Service date should be less or equal to current date"""
        if not(battery_last_service_date <= battery_current_date):
                raise Exception("battery_last_service_date should be less than battery_current_date")
        
        
        """Super constructor is calling"""
        super().__init__()
        self.battery_current_date = battery_current_date
        self.battery_last_service_date = battery_last_service_date

        
        
    def battery_needs_service(self):
        service_threshold_date = self.battery_last_service_date.replace(year=self.battery_last_service_date.year + 4)
        return service_threshold_date <= datetime.today().date()
            
        
 