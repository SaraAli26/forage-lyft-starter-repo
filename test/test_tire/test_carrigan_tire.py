import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_ware = [0.9, 1, 0.9,0.8]
        tire = CarriganTire(tire_ware)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_ware = [1, 1, 1,1]
        tire = CarriganTire(tire_ware)
        self.assertFalse(tire.needs_service())