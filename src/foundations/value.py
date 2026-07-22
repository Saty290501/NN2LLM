"""
NN2LLM - Value Module
=====================

This module defines the fundamental Value class used to build
computational graphs for automatic differentiation.

Unlike Python's built-in numeric types, a Value object stores
both numerical data and the metadata required to compute gradients.

Author:
    Satyen Chaudhari

Inspired by:
    Andrej Karpathy's "Neural Networks: Zero to Hero"
"""

from __future__ import annotations

from typing import Callable


class Value:
    """
    Represents a single node in a computational graph.

    A Value object stores a numerical value along with all the
    information required for automatic differentiation.
    """

    def __init__(
        self,
        data: float,
        parents: tuple["Value", ...] = (),
        operation: str = "",
        label: str = "",
    ) -> None:
        """
        Initialize a Value object.

        Parameters
        ----------
        data:
            Numerical value stored by the node.

        parents:
            Parent nodes that produced this Value.

        operation:
            Mathematical operation responsible for creating
            this Value.

        label:
            Optional human-readable identifier useful for
            debugging and visualization.
        """

        # Actual numerical value.
        self.data = float(data)

        # Gradients accumulate during backpropagation.
        self.grad = 0.0

        # Parent nodes in the computational graph.
        self.parents = parents

        # Operation that created this node.
        self.operation = operation

        # Friendly name for debugging.
        self.label = label

        # Placeholder function.
        # This will later contain the local gradient computation.
        self._backward: Callable[[], None] = lambda: None

    def __repr__(self) -> str:
        """
        Return a readable representation of the object.
        """

        return (
            f"Value("
            f"data={self.data}, "
            f"grad={self.grad}, "
            f"operation='{self.operation}')"
        )   