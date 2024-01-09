

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from main.engine.enginebase import Engine


from main.engine.enginebase import Engine


class Willoughby(Engine):

   def __init__(self, engine_current_mileage, engine_last_service_mileage):
       
      """Checking battery_last_service_date must be of type date otherwise raises a value Error"""
      if not isinstance(engine_current_mileage, int):
            raise ValueError("engine_current_mileage must be of type int.") 
      
      if not isinstance(engine_last_service_mileage, int):
            raise ValueError("engine_last_service_mileage must be of type int.")

      """Checking engine_last_service_mileage should not be greater or equal to engine_current_mileage"""
      if(engine_last_service_mileage  > engine_current_mileage):
                raise Exception("engine_last_service_mileage should not be greater than battery_current_date")
        
      """Checking engine_last_service_mileage & engine_current_mileage are not Nagative numbers"""
      if(engine_current_mileage  < 0 or engine_last_service_mileage  < 0):
                raise ValueError("engine_last_service_mileage & Current_mileage should not be greater than zero")
        

      super().__init__()
      self.engine_current_mileage = engine_current_mileage
      self.engine_last_service_mileage = engine_last_service_mileage
      
   def engine_should_be_serviced(self):
       return self.engine_current_mileage - self.engine_last_service_mileage > 60000
