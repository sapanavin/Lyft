""" this module """
from datetime import datetime

from main.battery.battery import Battery

"""this class is a representation of Nubbin Battery Type"""
class Nubbin(Battery):
    """this class is child of Battery"""
    def __init__(self, battery_last_service_date):
        """There is no need to override 'eat' it has the same signature as the implementation in Animal."""
        
    def needs_battery_service(self):
        service_threshold_date = self.battery_last_service_date.replace(year=self.battery_last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
        
    def battery_should_be_serviced(self):
        return True