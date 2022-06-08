from battery import battery

class nubbin_battery(battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)
    def  needs_service(self, threhold_year = 4):
        super().needs_service(threhold_year)



