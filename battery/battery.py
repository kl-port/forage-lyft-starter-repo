class battery:
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self, threhold_year):
        duration = self.current_date - self.last_service_date
        if duration > threhold_year:
            return True
        else:
            return False
