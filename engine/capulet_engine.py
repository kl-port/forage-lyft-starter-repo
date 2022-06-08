
from engine import engine 

class capulet_engine(engine.engine):
    def __init__(self, last_service_mileage, current_mileage, warning_light_on = False):
        super().__init__(last_service_mileage, current_mileage, warning_light_on = False)

    def needs_service(self, threhold_mileage = 30000):
        super().needs_service(threhold_mileage)