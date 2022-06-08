
class Engine:
    def __init__(self, last_service_mileage, current_mileage, warning_light_on = False):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.warning_light_on = warning_light_on

    def needs_service(self, threhold_mileage):
        duration = self.current_mileage - self.last_service_mileage
        if duration > threhold_mileage:
            return True
        elif self.warning_light_on:
            return True
        else:
            return False