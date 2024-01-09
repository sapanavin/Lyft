# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement

from datetime import date


from main.battery.nubbin import Nubbin
from main.battery.spindler import Spindler
from main.engine.capulet import Capulet

from main.engine.sternman import Sternman
from main.engine.willoughby import Willoughby
from main.model.car import Car

class Car_Factory():
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
       
       calliope_engine = Capulet(current_mileage, last_service_mileage)
       calliope_battery = Spindler(current_date, last_service_date)
       calliope = Car(calliope_engine , calliope_battery)
       return calliope

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
       
       glissade_engine = Willoughby(current_mileage, last_service_mileage)
       glissade_battery = Spindler(current_date, last_service_date)
       glissade = Car(glissade_engine , glissade_battery)
       return glissade

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
      
       palindrome_engine = Sternman(warning_light_on)
       palindrome_battery = Spindler(current_date, last_service_date)
       palindrome = Car(palindrome_engine, palindrome_battery)
       return palindrome

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
       
       rorschach_engine = Willoughby(current_mileage, last_service_mileage)
       rorschach_battery = Nubbin(current_date, last_service_date)
       rorschach = Car(rorschach_engine , rorschach_battery)
       return rorschach
    
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
       
       thovex_engine = Capulet(current_mileage, last_service_mileage)
       thovex_battery = Nubbin(current_date, last_service_date)
       thovex = Car(thovex_engine , thovex_battery)
       return thovex