import unittest

from src.foundations.value import Value


class ValueArithmeticTests(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Value(12.0, label="a")
        self.b = Value(4.0, label="b")

    def test_addition(self) -> None:
        result = self.a + self.b
        self.assertEqual(result.data, 16.0)
        self.assertEqual(result.parents, (self.a, self.b))
        self.assertEqual(result.operation, "+")

    def test_subtraction(self) -> None:
        result = self.a - self.b
        self.assertEqual(result.data, 8.0)
        self.assertEqual(result.parents, (self.a, self.b))
        self.assertEqual(result.operation, "-")

    def test_multiplication(self) -> None:
        result = self.a * self.b
        self.assertEqual(result.data, 48.0)
        self.assertEqual(result.parents, (self.a, self.b))
        self.assertEqual(result.operation, "*")

    def test_division(self) -> None:
        result = self.a / self.b
        self.assertEqual(result.data, 3.0)
        self.assertEqual(result.parents, (self.a, self.b))
        self.assertEqual(result.operation, "/")

    def test_division_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.a / Value(0.0)

    def test_numerical_power(self) -> None:
        result = self.b ** 2
        self.assertEqual(result.data, 16.0)
        self.assertEqual(result.parents, (self.b,))
        self.assertEqual(result.operation, "**2")


if __name__ == "__main__":
    unittest.main()
