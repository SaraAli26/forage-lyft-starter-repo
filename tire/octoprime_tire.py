from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_ware):
        self.tire_ware = tire_ware

    def needs_service(self):
        tire_ware_sum = 0
        for i in self.tire_ware:
            tire_ware_sum += i
        return tire_ware_sum >= 3
