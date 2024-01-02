
from enginebase import Engine


class Capulet(Engine):
    def __init__(self,engine_last_service_date , current_mileage, last_service_mileage):
       super._init_(engine_last_service_date, current_mileage, last_service_mileage)
      
     

    def engine_should_be_serviced(self):
       return self.current_mileage - self.last_service_mileage > 30000
