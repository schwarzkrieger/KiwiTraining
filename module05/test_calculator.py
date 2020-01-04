"""Test calculator"""
import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    """Testcase for calculator functions"""
    def test_add(self):
        """Test add()"""
        result = calculator.add(10, 20)
        self.assertEqual(result, 30)

    def test_subtract(self):
        """Test subtract()"""
        result = calculator.subtract(10, 20)
        self.assertEqual(result, -10)

    def test_multiply(self):
        """Test multiply()"""
        result = calculator.multiply(10, 20)
        self.assertEqual(result, 200)

    def test_divide(self):
        """Test divide()"""
        result = calculator.divide(20, 10)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
