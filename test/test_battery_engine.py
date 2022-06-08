import unittest
import sys
sys.path.append("..")
from datetime import datetime
from battery.nubbin_battery import nubbin_battery
from battery.spindler_battery import splindler_battery
from engine.capulet_engine import capulet_engine
from engine.sternman_engine import sternman_engine
from engine.willoughby_engine import willoughby_engine

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = nubbin_battery(last_service_date, today)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = nubbin_battery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = splindler_battery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = splindler_battery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 0
        engine = capulet_engine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 0
        light_on = True
        engine = sternman_engine(last_service_mileage, current_mileage, light_on)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 0
        light_on = False
        engine = sternman_engine(last_service_mileage, current_mileage, light_on)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 0
        engine = willoughby_engine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
