import unittest

from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator

    def test_one_plus_one_return_two(self):
        self.assertEqual(self.calculator.getResult(self, 1, 1, '+'), 2, 'Plus method wrong!')

    def test_two_minus_one_return_one(self):
        self.assertEqual(self.calculator.getResult(self, 2, 1, '-'), 1, 'Minus method wrong!')

    def test_two_multi_two_return_four(self):
        self.assertEqual(self.calculator.getResult(self, 2, 2, '*'), 4, 'Multi method wrong')

    def test_two_div_zore_raise_value_error_exception(self):
        self.assertRaises(ValueError, self.calculator.getResult, self.calculator, 2, 0, '/')


if __name__ == '__main__':
    unittest.main()
