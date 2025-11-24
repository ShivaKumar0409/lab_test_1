 Q4. 2 Develop a Python class `Rectangle` with methods for area and perimeter. Use an AI assistant for auto-generating docstrings and inline comments. Compare them with your manual documentation.


   import unittest
from rectangle import Rectangle   # assumes your class is in rectangle.py


class TestRectangle(unittest.TestCase):

    def test_area_small_values(self):
        """Input: width=2, height=3 → Output: area=6"""
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_area_large_values(self):
        """Input: width=10, height=50 → Output: area=500"""
        rect = Rectangle(10, 50)
        self.assertEqual(rect.area(), 500)

    def test_area_zero(self):
        """Input: width=0, height=7 → Output: area=0"""
        rect = Rectangle(0, 7)
        self.assertEqual(rect.area(), 0)

    def test_perimeter_small_values(self):
        """Input: width=2, height=3 → Output: perimeter=10"""
        rect = Rectangle(2, 3)
        self.assertEqual(rect.perimeter(), 10)

    def test_perimeter_large_values(self):
        """Input: width=10, height=50 → Output: perimeter=120"""
        rect = Rectangle(10, 50)
        self.assertEqual(rect.perimeter(), 120)

    def test_perimeter_zero_width(self):
        """Input: width=0, height=5 → Output: perimeter=10"""
        rect = Rectangle(0, 5)
        self.assertEqual(rect.perimeter(), 10)

    def test_perimeter_zero_height(self):
        """Input: width=6, height=0 → Output: perimeter=12"""
        rect = Rectangle(6, 0)
        self.assertEqual(rect.perimeter(), 12)


if __name__ == "__main__":
    unittest.main()
