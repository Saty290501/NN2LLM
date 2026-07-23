"""
NN2LLM - Computational Graph Utilities
======================================

This module contains helper functions for traversing and inspecting
the computational graph built using the Value class.

These utilities do NOT perform automatic differentiation.
Their responsibility is simply to understand the structure
of the graph.

Author:
    Satyen Chaudhari

Inspired by:
    Andrej Karpathy's "Neural Networks: Zero to Hero"
"""

from __future__ import annotations

from typing import Set, Tuple

from src.foundations.value import Value


def trace(root: Value) -> Tuple[Set[Value], Set[tuple[Value, Value]]]:
    """
    Traverse the computational graph starting from the output node.

    Returns
    -------
    nodes:
        Every Value object reachable from the output.

    edges:
        Parent → Child relationships.
    """

    nodes: Set[Value] = set()
    edges: Set[tuple[Value, Value]] = set()

    def build(node: Value):
        if node not in nodes:
            nodes.add(node)

            for parent in node.parents:
                edges.add((parent, node))
                build(parent)

    build(root)

    return nodes, edges

def print_graph(node: Value, prefix: str = "", is_last: bool = True) -> None:
    """
    Print the computational graph as an ASCII tree.
    """

    if node.label:
        name = f"{node.label} ({node.data})"
    elif node.operation:
        name = f"{node.operation} ({node.data})"
    else:
        name = str(node.data)

    # Root node
    if prefix == "":
        print(name)
    else:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + name)

    # Prepare indentation for child nodes
    child_prefix = prefix + ("    " if is_last else "│   ")

    parents = list(node.parents)

    for index, parent in enumerate(parents):
        print_graph(
            parent,
            child_prefix,
            index == len(parents) - 1,
        )