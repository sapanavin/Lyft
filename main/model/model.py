
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=pointless-string-statement

import json

from main.battery.battery import Battery

from main.engine.enginebase import Engine

"""This class represenet as a Factory of model; 
class works as follows:
    1.user need to input name of model 
    2.class will search name of Engine and battery for the model from the Model_info.json file 
    3.dynamically create the engine and battery objects for the model"""

class Model():
    engine_obj :Engine
    battery_obj :Battery
    def __init__(self, model_name):
        self.model_name = model_name
        self.create_engine()
              
        
      

    def model_details(self):
       



       #G:\Forage\Lyft\My_Task_2\main\model_info.json  
        # Opening JSON file
        with open('G:\\Forage\\Lyft\\My_Task_2\\main\\model_info.json', encoding="utf-8") as json_file:
            model = json.load(json_file)
        
            # Print the type of data variable
            print("Type:", type(model))
        
            #extracting model details
            print(self.model_name +"all Details  :")
            print( model[self.model_name])
            global current_model_details 
            current_model_details = model[self.model_name]
            
            #extracting engine name
            global current_model_engine 
            current_model_engine = current_model_details['engine']
            print(self.model_name +"'s  Engine  :")
            print(current_model_engine)
            
            #extracting battery name
            global current_model_battery 
            current_model_battery = current_model_details['battery']
            print(self.model_name +"'s   battery  :")
            print(current_model_battery)

"""create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
+ create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
+ create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): Car
+ create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
+ create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
"""
 

    def createModel(self):  
             self.create_engine()
             self.create_battery()   
                  
    def create_engine(self):
            engine_name = current_model_engine
         # Create an object of the Engine class dynamically
            dynamic_class = type(engine_name, (Engine,), {})
        #get imput form user
            engine_last_service_date = input("engine_last_service_date")
            current_mileage = input("current_mileage")
            last_service_mileage = input("last_service_mileage")
            engine_obj = dynamic_class(engine_last_service_date,current_mileage,last_service_mileage)  # Creating an instance of the dynamically created class

            #print(type(obj))  # Output: <class '__main__.MyClass'>
            #print(obj)  # Output: 10 battery_last_service_date, battery_last_service_date, battery_current_date
    
    def create_battery(self):
            battery_name = current_model_battery
         # Create an object of the Engine class dynamically
            dynamic_class = type(battery_name, (Battery,), {})
        #get imput form user
            battery_last_service_date = input("battery_last_service_date")
            battery_current_date   =    input("battery_current_date")

            battery_obj = dynamic_class(battery_last_service_date, battery_current_date)  # Creating an instance of the dynamically created class

            #print(type(obj))  # Output: <class '__main__.MyClass'>
            #print(obj)  # Output: 10
            