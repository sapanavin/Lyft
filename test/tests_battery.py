# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement


from datetime import datetime
import unittest
from main.battery.battery import Battery
from main.battery.nubbin import Nubbin
from main.battery.spindler import Spindler

class TestsNubbin(unittest.TestCase):
    
    def test_last_service_date_type_check(self):
        a=""
        today = datetime.today().date()
        try:
            Nubbin(a, today)
        except ValueError:
            return
        self.fail("ValueError was not raised")
        
    def test_current_date_type_check(self):
        b=12
        today = datetime.today().date()
        try:
            Nubbin(today, b)
        except ValueError:
            return
        self.fail("ValueError was not raised")

    def test_dates_checking(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 3)
        last_service_date = today.replace(year=today.year - 3)
        try:
           Nubbin(last_service_date, future_date)
        except Exception:
            return
        self.fail("Exception was not raised")

    def test_Everything_Is_OK(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 3)
        last_service_date = today.replace(year=today.year - 3)
              
        tempobj = Nubbin(today, last_service_date)
        self.assertIsInstance(tempobj, Battery, msg = "Object Created Successsfully")
        
    def testBatteryNeedsServiceReturnsTrue(self):
        today = datetime.today().date()
        needs_servicing_date = today.replace(year=today.year - 4)
        tempobj = Nubbin(today, needs_servicing_date)

        self.assertTrue(tempobj.battery_needs_service(),  msg = "Battery needs to service as it's been serviced before 4 years")
    
    def test_battery_needs_service_returns_FALSE(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 3)
       
        tempobj = Nubbin(future_date, today)

        self.assertFalse(tempobj.battery_needs_service(),  msg = "Battery doesn't needs to service ")  

    def test_battery_Serviced_today(self):
        today = datetime.today().date()
       
        tempobj = Nubbin(today, today)

        self.assertFalse(tempobj.battery_needs_service(),  msg = "Battery doesn't needs to service ")       

class Tests_Spindler(unittest.TestCase):
    
    def test_last_service_date_type_check(self):
        a=""
        today = datetime.today().date()
        try:
            Spindler(a, today)
        except ValueError:
            return
        self.fail("ValueError was not raised")
        
    def test_current_date_type_check(self):
        b=12
        today = datetime.today().date()
        try:
            Spindler(today, b)
        except ValueError:
            return
        self.fail("ValueError was not raised")

    def test_dates_checking(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 3)
        last_service_date = today.replace(year=today.year - 3)
        try:
           Spindler(last_service_date, future_date )
        except Exception:
            return
        self.fail("Exception was not raised")

    def test_Everything_Is_OK(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 3)
        last_service_date = today.replace(year=today.year - 3)
              
        tempobj = Spindler(today, last_service_date)
        self.assertIsInstance(tempobj, Battery, msg = "Object Created Successsfully")
        
    def test_battery_needs_service_returns_TRUE(self):
        today = datetime.today().date()
        needs_servicing_date = today.replace(year=today.year - 2)
        tempobj = Spindler(today , needs_servicing_date)

        self.assertTrue(tempobj.battery_needs_service(),  msg = "Battery needs to service as it's been serviced before 2 years")
    
    def test_battery_needs_service_returns_FALSE(self):
        today = datetime.today().date()
        future_date = today.replace(year=today.year + 1)
       
        tempobj = Spindler(future_date, today)

        self.assertFalse(tempobj.battery_needs_service(),  msg = "Battery doesn't needs to service ")  

    def test_battery_Serviced_today(self):
        today = datetime.today().date()
       
        tempobj = Spindler(today, today)

        self.assertFalse(tempobj.battery_needs_service(),  msg = "Battery doesn't needs to service ")       


    if __name__ == '__main__':
        unittest.main()
