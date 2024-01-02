from main.engine.enginebase import Engine


class Sternman(Engine):
    def __init__(self,engine_last_service_date , current_mileage, engine_last_service_mileage, warning_indicator):
       super._init_(engine_last_service_date, current_mileage, engine_last_service_mileage)
       self.warning_indicator = warning_indicator
     

    def engine_should_be_serviced(self):
        if self.warning_indicator:
            return True
        else:
            return False