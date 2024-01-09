# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement

from datetime import date

from main.battery.battery import Battery
from main.battery.nubbin import Nubbin
from main.battery.spindler import Spindler
from main.engine.capulet import Capulet
from main.engine.enginebase import Engine
from main.engine.sternman import Sternman
from main.engine.willoughby import Willoughby

class Car():
    engine :Engine
    battery :Battery

    def __init__(self, engine:Engine, battery:Battery):

        """Checking Car's Engine must be of type Engine otherwise raises a value Error"""
        if not isinstance(engine, Engine):
            raise ValueError("engine must be of type Engine.") 
       
        """Checking Car's battery must be of type Battery otherwise raises a value Error"""
        if not isinstance(battery, Battery):
            raise ValueError("battery must be of type Battery.") 
        
        self.engine = engine
        self.battery = battery
       
              

    