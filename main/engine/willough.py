from main.engine.enginebase import Engine


class Willough(Engine):
    def __init__(self,engine_last_service_date , current_mileage, engine_last_service_mileage):
       super._init_(engine_last_service_date, current_mileage, engine_last_service_mileage)
      
     

    def engine_should_be_serviced(self):
       return self.current_mileage - self.engine_last_service_mileage > 60000
