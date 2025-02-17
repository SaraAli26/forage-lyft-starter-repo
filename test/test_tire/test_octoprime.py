import unittest


from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_ware = [1,1,1,1]
        tire = OctoprimeTire(tire_ware)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_ware = [0,0,1,0]
        tire = OctoprimeTire(tire_ware)
        self.assertFalse(tire.needs_service())