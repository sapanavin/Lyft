# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement

import unittest
from datetime import datetime
import unittest
from main.battery.battery import Battery
from main.battery.nubbin import Nubbin
from main.engine.capulet import Capulet


from main.engine.enginebase import Engine
from main.engine.sternman import Sternman
from main.model.car import Car


"""Class will tests Car and  Funcationality"""

class Tests_Car_Factory(unittest.TestCase):

         
    def test_check_Parameters_Typr_Of_Car(self):
        try:
            Car("engine", "battery")
        except ValueError:
            return
        self.fail("ValueError was not raised")


    def test_check_Parameters_Of_Car(self):
        current_mileage=1000
        last_service_mileage = 10
        engine = Capulet(current_mileage, last_service_mileage)

        battery_current_date = datetime.today().date()
        battery_last_service_date = battery_current_date.replace(year=battery_current_date.year - 3)
        battery = Nubbin(battery_last_service_date, battery_current_date)
        
        car_obj1 = Car(engine, battery)
        
        self.assertIsInstance(car_obj1, Car, msg = "Object must be a type of Car")
        #self.assertNotIsInstance(car_obj2, Car, msg = "Car Object must be a created by Engine and Battery parameters")

      
       