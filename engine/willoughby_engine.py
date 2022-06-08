from engine.engine import Engine 

class willoughby_engine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__(last_service_mileage, current_mileage)

    def needs_service(self, threhold_mileage = 60000):
        return super().needs_service(threhold_mileage)