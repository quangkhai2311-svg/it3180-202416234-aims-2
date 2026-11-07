import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategoryTests(unittest.TestCase):
    def test_search_by_category(self):
        items = [DigitalVideoDisc("The Lion King", "Animation"),
                 DigitalVideoDisc("Star Wars", "Science Fiction")]
        self.assertEqual(search_by_category(items, "animation"), [items[0]])
        self.assertEqual(search_by_category(items, "ANIMATION"), [items[0]])
        self.assertEqual(search_by_category(items, "Drama"), [])
        self.assertEqual(search_by_category(items, "Anim"), [])
        self.assertEqual(search_by_category([], "Animation"), [])
