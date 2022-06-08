from engine.engine import Engine 

class sternman_engine(Engine):
    def __init__(self, last_service_mileage, current_mileage, warning_light_on):
        super().__init__(last_service_mileage, current_mileage, warning_light_on)

    def needs_service(self):
        return self.warning_light_on
            