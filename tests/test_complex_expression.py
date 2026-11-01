import unittest

from src.foundations.value import Value


class ComplexExpressionTests(unittest.TestCase):
    def test_nested_expression_computes_expected_scalar(self) -> None:
        a = Value(2.0, label="a")
        b = Value(3.0, label="b")
        c = Value(4.0, label="c")
        d = Value(5.0, label="d")

        product = a * b
        total = product + (c + d)
        squared = total ** 2
        output = squared / a

        self.assertEqual(product.data, 6.0)
        self.assertEqual(total.data, 15.0)
        self.assertEqual(squared.data, 225.0)
        self.assertEqual(output.data, 112.5)
        self.assertEqual(output.operation, "/")


if __name__ == "__main__":
    unittest.main()
