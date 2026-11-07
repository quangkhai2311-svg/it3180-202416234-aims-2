import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_title(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        for keyword in ("Lion", "lion", "LION"):
            with self.subTest(keyword=keyword):
                self.assertEqual(search_by_title(items, keyword), [items[0]])
        self.assertEqual(search_by_title(items, "missing"), [])
        self.assertEqual(search_by_title([], "lion"), [])
        self.assertEqual(search_by_title(items, ""), items)
