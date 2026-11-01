import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.foundations.graph import print_graph, trace
from src.foundations.value import Value


class ComputationalGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Value(2.0, label="a")
        self.b = Value(3.0, label="b")
        self.product = self.a * self.b
        self.product.label = "product"
        self.sum_value = self.a + self.b
        self.sum_value.label = "sum"
        self.output = self.product + self.sum_value
        self.output.label = "output"

    def test_trace_returns_all_reachable_nodes(self) -> None:
        nodes, _ = trace(self.output)
        self.assertEqual(
            nodes,
            {self.a, self.b, self.product, self.sum_value, self.output},
        )

    def test_trace_returns_parent_to_child_edges(self) -> None:
        _, edges = trace(self.output)
        expected_edges = {
            (self.a, self.product),
            (self.b, self.product),
            (self.a, self.sum_value),
            (self.b, self.sum_value),
            (self.product, self.output),
            (self.sum_value, self.output),
        }
        self.assertEqual(edges, expected_edges)

    def test_print_graph_includes_nodes_and_values(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            print_graph(self.output)

        rendered = output.getvalue()
        self.assertIn("output", rendered)
        self.assertIn("product", rendered)
        self.assertIn("sum", rendered)
        self.assertIn("2.0", rendered)
        self.assertIn("3.0", rendered)


if __name__ == "__main__":
    unittest.main()
