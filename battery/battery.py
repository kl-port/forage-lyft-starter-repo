import datetime
class Battery:
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self, threhold_year):
        if self.current_date > self.last_service_date + datetime.timedelta(days = 365*threhold_year):
            return True
        else:
            return False