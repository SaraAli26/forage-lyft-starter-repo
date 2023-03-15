from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, last_service_date, battery, engine):
        self.battery = battery
        self.engine = engine
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
