# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from datetime import datetime
import unittest
from main.battery.battery import Battery
from main.battery.nubbin import Nubbin
from main.battery.spindler import Spindler
from main.engine.capulet import Capulet


from main.engine.enginebase import Engine
from main.engine.sternman import Sternman
from main.engine.willoughby import Willoughby
from main.model.car import Car
from main.model.car_factory import Car_Factory


"""Class will tests Car and Car Factory  Funcationality"""

class Tests_Car_Factory(unittest.TestCase):
    engine_current_mileage=1000
    engine_last_service_mileage = 10
    engine = Capulet(engine_current_mileage, engine_last_service_mileage)

    battery_current_date = datetime.today().date()
    battery_last_service_date = battery_current_date.replace(year=battery_current_date.year - 1)
   
        
          
    def test__create_calliope(self):
        """"calliope":{ "engine":"capulet","battery":"spindler"}"""
        obj = Car_Factory()
        calliope = obj.create_calliope(self.battery_current_date, self.battery_last_service_date, self.engine_current_mileage, self.engine_last_service_mileage)
        
           
        self.assertIsInstance(calliope.engine, Capulet, msg = "Calliope Engine must be a type of Capulet")
        self.assertIsInstance(calliope.battery, Spindler, msg = "Calliope Battery must be a type of Spindler")
        self.assertIsInstance(calliope, Car, msg = "Calliope Oject must be a type of Car")
        
    def test__create_glissade(self):
        """glissade":{"engine":"willoughby","battery":"spindler"}"""
        obj = Car_Factory()
        glissade =  obj.create_glissade(self.battery_current_date, self.battery_last_service_date, self.engine_current_mileage, self.engine_last_service_mileage)
         
        self.assertIsInstance(glissade.engine, Willoughby, msg = "glissade Engine must be a type of willoughby")
        self.assertIsInstance(glissade.battery, Spindler, msg = "glissade Battery must be a type of Spindler")
        self.assertIsInstance(glissade, Car, msg = "glissade Oject must be a type of Car")

    def test_create_palindrome(self):
        """ palindrome":{"engine":"sternman","battery":"spindler"} """

        warning_light_on = True
        obj = Car_Factory()
        palindrome = obj.create_palindrome(self.battery_current_date, self.battery_last_service_date,warning_light_on)
        self.assertIsInstance(palindrome.engine, Sternman, msg = "glissade Engine must be a type of willoughby")
        self.assertIsInstance(palindrome.battery, Spindler, msg = "glissade Battery must be a type of Spindler")
        self.assertIsInstance(palindrome, Car, msg = "glissade Oject must be a type of Car")
   
   
    def test__create_rorschach(self):
        
        """rorschach":{"engine":"willoughby","battery":"nubbin"}"""
        obj = Car_Factory()
        rorschach =  obj.create_rorschach(self.battery_current_date, self.battery_last_service_date, self.engine_current_mileage, self.engine_last_service_mileage)
  
        self.assertIsInstance(rorschach.engine, Willoughby, msg = "rorschach Engine must be a type of willoughby")
        self.assertIsInstance(rorschach.battery, Nubbin, msg = "rorschach Battery must be a type of Nubbin")
        self.assertIsInstance(rorschach, Car, msg = "glissade Oject must be a type of Car")

    def test__create_thovex(self):
        
        """"thorex":{"engine":"capulet","battery":"nubbin"}"""
        obj = Car_Factory()
        thovex = obj.create_thovex(self.battery_current_date, self.battery_last_service_date, self.engine_current_mileage, self.engine_last_service_mileage)
                   
        self.assertIsInstance(thovex.engine, Capulet, msg = "thovex Engine must be a type of Capulet")
        self.assertIsInstance(thovex.battery, Nubbin, msg = "thovex Battery must be a type of Nubbin")
        self.assertIsInstance(thovex, Car, msg = "thovex Oject must be a type of Car")
                
                
    