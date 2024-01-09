# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement

import unittest


from main.engine.capulet import Capulet
from main.engine.enginebase import Engine
from main.engine.sternman import Sternman
from main.engine.willoughby import Willoughby

"""Class will tests Capulet Engine's Funcationality"""
class Tests_Capulet(unittest.TestCase):
    
    def test_engine_current_mileage_type_check(self):
        engine_current_mileage=""
        engine_last_service_mileage=123654
        try:
            Capulet(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")
        
    def test_engine_last_service_mileage_type_check(self):
        engine_current_mileage=12547896
        engine_last_service_mileage="object"
        try:
            Capulet(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")

    def test_engine_parameters_ARE_NEGTIVE(self):
        engine_current_mileage=-12547896
        engine_last_service_mileage=engine_current_mileage - 30001
        try:
            Capulet(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")
    
    def test_Succefully_Capulet_Object_created(self):
        engine_current_mileage=1000
        engine_last_service_mileage=10
    
        Capulet(engine_current_mileage, engine_last_service_mileage)
        
        tempobj = Capulet(engine_current_mileage, engine_last_service_mileage)
        self.assertIsInstance(tempobj, Engine, msg = "Object must be a type of Engine")
        self.assertIsInstance(tempobj, Capulet, msg = "Object must be a type of Capulet")

    def test_engine_last_service_mileage_NOT_LESS_THAN_Current_milage(self):
        engine_current_mileage=10
        engine_last_service_mileage=1000
    
        try:
            Capulet(engine_current_mileage, engine_last_service_mileage)
        except Exception:
            return
        self.fail("Exception was not raised")
        
    def test_engine_should_be_serviced_RETURNS_TRUE(self):
        engine_last_service_mileage=1000
        engine_current_mileage=engine_last_service_mileage+30001
       
    
        tempobj = Capulet(engine_current_mileage, engine_last_service_mileage)
        self.assertTrue(tempobj.engine_should_be_serviced(),msg="Engine needs to Service")
        
    def test_engine_should_be_serviced_RETURNS_FALSE(self):
        engine_last_service_mileage=1000
        engine_current_mileage=engine_last_service_mileage+30000
       
    
        tempobj = Capulet(engine_current_mileage, engine_last_service_mileage)
        self.assertFalse(tempobj.engine_should_be_serviced(),msg="Engine needs to Service")
        


"""Class will tests Willoughby Engine's Funcationality"""
class Tests_Willoughby(unittest.TestCase):
    
    def test_engine_current_mileage_type_check(self):
        engine_current_mileage=""
        engine_last_service_mileage=123654
        try:
            Willoughby(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")
        
    def test_engine_last_service_mileage_type_check(self):
        engine_current_mileage=12547896
        engine_last_service_mileage="object"
        try:
            Willoughby(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")
    
    def test_engine_parameters_ARE_NEGTIVE(self):
        engine_current_mileage = -12547896
        engine_last_service_mileage=engine_current_mileage - 60001
        try:
            Willoughby(engine_current_mileage, engine_last_service_mileage)
        except ValueError:
            return
        self.fail("ValueError was not raised")
   
    def test_Succefully_Willoughby_Object_created(self):
        engine_current_mileage=1000
        engine_last_service_mileage=10
    
              
        tempobj = Willoughby(engine_current_mileage, engine_last_service_mileage)
        self.assertIsInstance(tempobj, Engine, msg = "Object must be a type of Engine")
        self.assertIsInstance(tempobj, Willoughby, msg = "Object must be a type of Capulet")

    def test_engine_last_service_mileage_NOT_LESS_THAN_Current_milage(self):
        engine_current_mileage=10
        engine_last_service_mileage=1000
    
        try:
            Willoughby(engine_current_mileage, engine_last_service_mileage)
        except Exception:
            return
        self.fail("Exception was not raised")
        
    def test_engine_should_be_serviced_RETURNS_TRUE(self):
        engine_last_service_mileage=1000
        engine_current_mileage=engine_last_service_mileage+60001
       
    
        tempobj = Willoughby(engine_current_mileage, engine_last_service_mileage)
        self.assertTrue(tempobj.engine_should_be_serviced(),msg="Engine needs to Service")
        
    def test_engine_should_be_serviced_RETURNS_FALSE(self):
        engine_last_service_mileage=1000
        engine_current_mileage=engine_last_service_mileage+60000
       
    
        tempobj = Willoughby(engine_current_mileage, engine_last_service_mileage)
        self.assertFalse(tempobj.engine_should_be_serviced(),msg="Engine needs to Service")
        



"""Class will tests Sternman Engine's Funcationality"""

class Tests_Sternman(unittest.TestCase):
    def test__type_check(self):
        engine_warning_indicator=""
        
        try:
            Sternman(engine_warning_indicator)
        except ValueError:
            return
        self.fail("ValueError was not raised")

    def test_Successfully_Sterman_Object_created_for_TRUE_Warning_Indictor(self):
        engine_warning_indicator=True
           
        tempobj = Sternman(engine_warning_indicator)
        self.assertIsInstance(tempobj, Engine, msg = "Object must be a type of Engine")
        self.assertIsInstance(tempobj, Sternman, msg = "Object must be a type of Capulet")

    def test_Successfully_Sterman_Object_created_for_FALSE_Warning_Indictor(self):
        engine_warning_indicator=False
           
        tempobj = Sternman(engine_warning_indicator)
        self.assertIsInstance(tempobj, Engine, msg = "Object must be a type of Engine")
        self.assertIsInstance(tempobj, Sternman, msg = "Object must be a type of Capulet")

    def test_engine_should_be_serviced_for_TRUE_Warning_Indictor(self):
        engine_warning_indicator=True
           
        tempobj = Sternman(engine_warning_indicator)
        self.assertTrue(tempobj.engine_should_be_serviced(), msg="Engine shoulb be Service for False warning Indicator")

    def test_engine_should_be_NOT_serviced_for_FALSE_Warning_Indictor(self):
        engine_warning_indicator=False
           
        tempobj = Sternman(engine_warning_indicator)
        self.assertFalse(tempobj.engine_should_be_serviced(), msg="Engine shoulb be Service for False warning Indicator")

    


if __name__ == '__main__':
    unittest.main()