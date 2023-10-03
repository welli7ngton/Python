# flake8: noqa
"""
Calculadora Simples

Implemente uma calculadora simples com operações de adição, subtração,
multiplicação e divisão.
"""

import unittest
from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def test_if_x_is_not_an_int_or_floatinstance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            Calculator('1', 2)
        self.assertEqual(ex.exception.args[0], 'x shold be an int or float')

    def test_if_y_is_not_an_int_or_float_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            Calculator(1, '2')
        self.assertEqual(ex.exception.args[0], 'y shold be an int or float')

    def test_postivie_sum_return(self):
        self.assertEqual(Calculator(10, 3).sum(), 13)

    def test_sum_negative_equation(self):
        self.assertEqual(Calculator(10, -15).sum(), -5)

    def test_negative_sum(self):
        self.assertEqual(Calculator(-7, -1).sum(), -8)

    def test_positives_sub_return(self):
        self.assertEqual(Calculator(10, 10).sub(), 0)

    def test_sub_negative_equation(self):
        self.assertEqual(Calculator(13, -7).sub(), 20)

    def test_negatives_sub(self):
        self.assertEqual(Calculator(-23, -18).sub(), -5)

    def test_positive_mult(self):
        self.assertEqual(Calculator(18, 53).mult(), 954)

    def test_negative_mult(self):
        self.assertEqual(Calculator(-3, -24).mult(), 72)

    def test_positive_and_negative_mult(self):
        self.assertEqual(Calculator(-17, 5).mult(), -85)

    def test_integer_division(self):
        self.assertEqual(Calculator(5, 5).division(), 1)

    def test_negative_integer_division(self):
        self.assertEqual(Calculator(-255, -25).division(), 10)

    def test_fractional_division(self):
        self.assertEqual(Calculator(5.55, 5.55).division(), 1.0)

    def test_division_by_zero(self):
        with self.assertRaises(Exception) as ex:
            Calculator(12, 0).division()
        self.assertEqual(ex.exception.args[0], '0DivisionError')


if __name__ == '__main__':
    unittest.main(verbosity=2)
