from battery.battery import Battery

class nubbin_battery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
    def  needs_service(self, threhold_year = 4):
        return super().needs_service(threhold_year)



