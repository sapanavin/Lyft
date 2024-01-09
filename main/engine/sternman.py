# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from main.engine.enginebase import Engine


class Sternman(Engine):
    warning_indicator:bool
    
    def __init__(self, engine_warning_indicator):
       
        """Checking battery_last_service_date must be of type date otherwise raises a value Error"""
        if not isinstance(engine_warning_indicator, bool):
            raise ValueError("warning_indicator must be of type bool.") 
        super().__init__()
        self.engine_warning_indicator = engine_warning_indicator
     

    def engine_should_be_serviced(self):
        return self.engine_warning_indicator
         
       
             