from datetime import datetime

from main.battery.battery import Battery



class spindler(Battery):
    def __init__(self, battery_last_service_date):
        super().__init__(battery_last_service_date)
        
    def needs_battery_service(self):
        service_threshold_date = self.battery_last_service_date.replace(year=self.battery_last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
        
    def battery_should_be_serviced(self):
        return True