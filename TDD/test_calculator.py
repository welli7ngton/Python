"""
Calculadora Simples

Implemente uma calculadora simples com operações de adição, subtração,
multiplicação e divisão.
"""

import unittest
from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def test_postivie_sum_return(self):
        self.assertEqual(Calculator.sum(10, 20), 30)

    def test_sum_negative_equation(self):
        self.assertEqual(Calculator.sum(10, -15), -5)

    def test_negative_sum(self):
        self.assertEqual(Calculator.sum(-1, -7), -8)

    def test_positives_sub_return(self):
        self.assertEqual(Calculator.sub(10, 10), 0)

    def test_sub_negative_equation(self):
        self.assertEqual(Calculator.sub(13, -7), 20)

    def test_negatives_sub(self):
        self.assertEqual(Calculator.sub(-23, -18), -5)

    def test_positive_mult(self):
        self.assertEqual(Calculator.mult(18, 53), 954)

    def test_negative_mult(self):
        self.assertEqual(Calculator.mult(-3, -24), 72)

    def test_positive_and_negative_mult(self):
        self.assertEqual(Calculator.mult(-17, 5), -85)

    def test_integer_division(self):
        self.assertEqual(Calculator.division(5, 5), 1)

    def test_negative_integer_division(self):
        self.assertEqual(Calculator.division(-255, -25), 10)

    def test_fractional_division(self):
        self.assertEqual(Calculator.division(5.555555, 5), 1)

    def test_division_by_zero(self):
        self.assertEqual(Calculator.division(32, 0), '0DivisionError')


unittest.main(verbosity=2)
