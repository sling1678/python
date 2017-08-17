from unittest import TestCase
from src import FractionClass
class TestFraction(TestCase):
    def setUp(self):
        self.Fraction = Fraction(2,3)
    def test_frac(self):
        self.assertEqual(Fraction(2,3).num, 3)

#    pass

if __name__ == "__main__":
    unittest.main()
