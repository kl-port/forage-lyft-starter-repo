from battery.battery import Battery

class splindler_battery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
    def  needs_service(self, threhold_year = 3):
        return super().needs_service(threhold_year)