import abc
from abc import ABC, abstractmethod


class Engine(ABC):
    
    def __init__(self):
      pass
     

    @abstractmethod
    def engine_should_be_serviced(self):
        pass
