import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("DVD A", cost=100))

    def test_discount_20_percent(self):
        self.assertEqual(self.cart.total_after_discount(20), 80)

    def test_invalid_discount(self):
        for percent in (-1, 150):
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    self.cart.total_after_discount(percent)
