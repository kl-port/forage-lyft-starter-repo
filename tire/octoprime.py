
class carrigan_tire():
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        if sum(self.tires) >= 3:
            return True
        return False