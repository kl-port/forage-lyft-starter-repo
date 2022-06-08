from datetime import datetime
import sys
sys.path.append("..")
from battery.nubbin_battery import nubbin_battery
from engine.capulet_engine import capulet_engine


class Thovex():
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_mileage

    def needs_service(self):
        return capulet_engine.needs_service(self.last_service_date, datetime.today().date()) and nubbin_battery.needs_service(self.last_service_mileage, self.current_mileage)
