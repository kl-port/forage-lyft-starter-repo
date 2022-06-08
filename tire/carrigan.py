
class carrigan_tire():
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        for i in self.tires:
            if i >= 0.9:
                return True
        return False