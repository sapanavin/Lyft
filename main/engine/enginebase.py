import abc
from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self,engine_last_service_date , current_mileage, engine_last_service_mileage):
        self.engine_last_service_date = engine_last_service_date
        self.current_mileage = current_mileage
        self.engine_last_service_mileage = engine_last_service_mileage

    @abstractmethod
    def engine_should_be_serviced(self):
        pass
