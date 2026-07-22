"""
NN2LLM - Value Module
=====================

This module defines the core `Value` class, which will become the
foundation of the automatic differentiation engine used throughout
the NN2LLM project.

Unlike Python's built-in numeric types (`int` and `float`), a `Value`
object is designed to store not only a numerical value but also the
information required to build a computational graph.

In later milestones, this class will support:

- Computational graph construction
- Gradient tracking
- Reverse-mode automatic differentiation (Backpropagation)
- Mathematical operations such as:
    - Addition
    - Multiplication
    - Subtraction
    - Division
    - Power
- Activation functions:
    - ReLU
    - Tanh
    - Sigmoid
    - Exp

Current Status
--------------
This file currently contains only the project documentation.
The implementation of the `Value` class will be added incrementally
as we progress through the NN2LLM learning roadmap.

Author
------
Satyen Chaudhari

Project
-------
NN2LLM
(Building Neural Networks to Large Language Models from Scratch)

Inspired by
-----------
Andrej Karpathy's "Neural Networks: Zero to Hero"

Version
-------
0.1.0
"""