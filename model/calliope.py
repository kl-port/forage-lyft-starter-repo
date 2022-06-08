import sys
sys.path.append("..")
from datetime import datetime
from engine.capulet_engine import capulet_engine
from battery.spindler_battery import splindler_battery


class Calliope():
    def __init__(self,  current_mileage, last_service_mileage, warning_light_on = False):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = capulet_engine(self.last_service_date, datetime.today().date())
        battery = splindler_battery(self.last_service_mileage, self.current_mileage)
        return engine.needs_service and battery.needs_service
