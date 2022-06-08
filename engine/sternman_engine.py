
from engine import engine 

class sternman_engine(engine):
    def __init__(self, last_service_mileage, current_mileage, warning_light_on = False):
        super().__init__(last_service_mileage, current_mileage, warning_light_on = False)

    def needs_service(self):
        return self.warning_light_on
            