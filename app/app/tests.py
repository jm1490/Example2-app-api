from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtarct_numbers(self):
        """test that values are subtracted together"""
        self.assertEqual(subtract(5, 11), 6)
