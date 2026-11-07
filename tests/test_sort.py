import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", cost=20))
        self.cart.add_dvd(DigitalVideoDisc("C", cost=10))
        self.cart.add_dvd(DigitalVideoDisc("A", cost=30))

    def test_sort_by_title(self):
        total = self.cart.total_cost()
        self.cart.sort_by_title()

        self.assertEqual([dvd.title for dvd in self.cart.items], ["A", "B", "C"])
        self.assertEqual(self.cart.total_cost(), total)

    def test_sort_by_cost(self):
        total = self.cart.total_cost()
        self.cart.sort_by_cost()

        self.assertEqual([dvd.title for dvd in self.cart.items], ["C", "B", "A"])
        self.assertEqual([dvd.cost for dvd in self.cart.items], [10, 20, 30])
        self.assertEqual(self.cart.total_cost(), total)
