"""Example test"""
from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Testing addition of 2 numbers """
        res = calc.add(5, 5)
        self.assertEqual(res, 10)

    def test_subtract_numbers(self):
        """Testing addition of 2 numbers """
        res = calc.subtract(5, 5)
        self.assertEqual(res, 0)
