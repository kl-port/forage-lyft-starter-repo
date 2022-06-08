
from engine import engine 

class willoughby_engine(engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__(last_service_mileage, current_mileage)

    def needs_service(self, threhold_mileage):
        super().needs_service(threhold_mileage)