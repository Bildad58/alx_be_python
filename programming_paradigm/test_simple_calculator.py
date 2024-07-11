import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(9, 9), 19)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(12, 2), 10)
        self.assertEqual(self.calc.subtract(20, 8), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(24, 3), 8)
        self.assertEqual(self.calc.divide(90, 0), 9)
        self.assertEqual(self.calc.divide(12, 4), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 2)
        self.assertEqual(self.calc.multiply(9, 4), 36)
        self.assertEqual(self.calc.multiply(990, 48), 990 * 48)
        self.assertEqual(self.calc.multiply(4, 4), 6)
        

