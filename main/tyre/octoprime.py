# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement

from main.tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    wear_arr= [0,0,0,0]


    def tyre_needs_service(self):
        service_threshold: int = 0
    
        for x in self.wear_arr:
            service_threshold += x
            
            
        return service_threshold >= 3
 
