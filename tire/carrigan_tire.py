from tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_ware):
        self.tire_ware = tire_ware

    def needs_service(self):
        tire_wares = 0
        for i in self.tire_ware:
            if i == 0.9:
                tire_wares += 1
        return tire_wares >= 1
