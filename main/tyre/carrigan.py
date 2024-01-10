# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement


from main.tyre.tyre import Tyre


class CarriganTyre(Tyre):
    wear_arr= [0,0,0,0]


    def tyre_needs_service(self):
        for x in self.wear_arr:
            if(x >= 0.9):
                return True
                    
        return False