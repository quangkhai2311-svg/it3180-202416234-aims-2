import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(
                cart.add_dvd(DigitalVideoDisc(f"DVD {index}"))
            )

        self.assertFalse(
            cart.add_dvd(DigitalVideoDisc("DVD 21"))
        )
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD A", cost=40))
        cart.add_dvd(DigitalVideoDisc("DVD B", cost=60))

        self.assertEqual(cart.total_cost(), 100)
