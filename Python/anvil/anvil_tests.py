from python.anvil.anvil import duplicate_encode

import unittest


class AnvilTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(duplicate_encode("din"),"(((")

    def test_2(self):
        self.assertEqual(duplicate_encode("recede"),"()()()")

    def test_3(self):
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
