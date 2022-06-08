import sys
sys.path.append("..")
from datetime import datetime
from battery.spindler_battery import splindler_battery
from engine.sternman_engine import sternman_engine


class Palindrome():
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_mileage

    def needs_service(self):
        return sternman_engine.needs_service(self.last_service_date, datetime.today().date()) and splindler_battery.needs_service(self.last_service_mileage, self.current_mileage)
