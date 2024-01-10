from datetime import datetime
import unittest

from main.tyre.carrigan import CarriganTyre
from main.tyre.octoprime import OctoprimeTyre

class Tests_Carrigan(unittest.TestCase):

    def test_successful_Object_Creation(self):
         carrigan = CarriganTyre()
         self.assertIsInstance(carrigan, CarriganTyre, msg = "Object must be a type of Carrigan")


    def test_tyre_needs_service(self):
         
         carriganTyreObj = CarriganTyre()
         carriganTyreObj.wear_arr[0]=0.9
         carriganTyreObj.wear_arr[1]=0
         carriganTyreObj.wear_arr[2]=0
         carriganTyreObj.wear_arr[3]=0.9
         self.assertTrue(carriganTyreObj.tyre_needs_service(), msg="Engine should be Service ")

    def test_tyre_Dont_needs_service(self):
         
         carriganTyreObj = CarriganTyre()
         self.assertFalse(carriganTyreObj.tyre_needs_service(), msg="Engine should not be Service ")


class Tests_Octoprime(unittest.TestCase):

    def test_successful_Object_Creation(self):
         octoprime = OctoprimeTyre()
         self.assertIsInstance(octoprime, OctoprimeTyre, msg = "Object must be a type of Octoprime")


    def test_tyre_needs_service(self):
        """here addition of wear_arr is greater than 3 so tyre needs to service"""
         
        octoprimeTyreObj = OctoprimeTyre()
        octoprimeTyreObj.wear_arr[0]=0.9
        octoprimeTyreObj.wear_arr[1]=0.9
        octoprimeTyreObj.wear_arr[2]=0.5
        octoprimeTyreObj.wear_arr[3]=0.9
        
        self.assertTrue(octoprimeTyreObj.tyre_needs_service(), msg="Tyre should be Service ")

    def test_tyre_Dont_needs_service(self):
         
        octoprimeTyreObj = OctoprimeTyre()
        octoprimeTyreObj.wear_arr[0]=0.3
        octoprimeTyreObj.wear_arr[1]=0.4
        octoprimeTyreObj.wear_arr[2]=0.5
        octoprimeTyreObj.wear_arr[3]=0.1
        self.assertFalse(octoprimeTyreObj.tyre_needs_service(), msg="Tyre should not be Service ")

    if __name__ == '__main__':
        unittest.main()