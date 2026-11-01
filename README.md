# NN2LLM — Neural Networks to Large Language Models

[![Python tests](https://github.com/Saty290501/NN2LLM/actions/workflows/tests.yml/badge.svg)](https://github.com/Saty290501/NN2LLM/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Learning%20in%20progress-orange)

A hands-on journey from the foundations of neural networks to the ideas behind modern large language models. The goal is to understand the building blocks by implementing small, inspectable pieces rather than treating deep-learning frameworks as black boxes.

## Project status

This repository is intentionally incremental. The current implementation is a **scalar computation and graph-inspection foundation**:

- A Value object stores a scalar, its immediate parents, and the operation that created it.
- Arithmetic operations currently include addition, subtraction, multiplication, division, and numerical powers.
- The trace utility collects the nodes and dependency edges reachable from an output.
- The print_graph utility displays the dependency structure as an ASCII tree.
- Automated tests cover arithmetic behaviour and graph structure.

**Important:** reverse-mode automatic differentiation and a complete backpropagation pass are not implemented yet. The _backward field is currently a placeholder. They are planned next steps, not existing features.

## Learning roadmap

- [x] Create a scalar Value abstraction
- [x] Record parent dependencies for arithmetic operations
- [x] Inspect computational graphs with traversal utilities
- [x] Add automated tests for current behaviour
- [ ] Implement local gradient rules for each operation
- [ ] Add topological ordering and reverse-mode backpropagation
- [ ] Build neurons, layers, and a multi-layer perceptron
- [ ] Train and evaluate a small neural network
- [ ] Explore character-level language models and tokenization
- [ ] Implement attention and transformer components
- [ ] Study GPT-style models and LLM inference

## Repository structure

~~~text
NN2LLM/
├── src/
│   └── foundations/
│       ├── value.py       # Scalar Value nodes and arithmetic operations
│       └── graph.py       # Graph tracing and ASCII inspection
├── tests/
│   ├── test_value.py
│   ├── test_graph.py
│   └── test_complex_expression.py
└── docs/
    ├── README.md
    └── foundations/      # Concept notes linked to the implementation
~~~

## Getting started

### Requirements

- Python 3.10 or later
- No third-party Python packages are required for the current implementation or test suite.

### Clone the repository

~~~bash
git clone https://github.com/Saty290501/NN2LLM.git
cd NN2LLM
~~~

### Run the tests

~~~bash
python -m unittest discover -s tests -t . -v
~~~

### Try the current Value API

~~~python
from src.foundations.value import Value

a = Value(2.0, label="a")
b = Value(3.0, label="b")

result = (a * b) + a

print(result.data)       # 8.0
print(result.parents)   # Immediate dependencies
print(result.operation) # +
~~~

## Concept notes

The [docs index](docs/README.md) links the written explanations, including:

- [Why a Value class?](docs/foundations/01_why_value_class.md)
- [Operator overloading](docs/foundations/02_operator_overloading.md)
- [Complex expressions](docs/foundations/03_complex_expressions.md)
- [Computational graphs](docs/foundations/04_computational_graph.md)
- [Computational graphs in deep learning](docs/foundations/04.2_graphs_in_deep_learning.md)
- [PyTorch Autograd concepts](docs/foundations/04.3_pytorch_autograd.md)

## Learning references

This project is inspired by Andrej Karpathy's [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero). The code and notes here are an independent learning implementation; consult the original material and official framework documentation for deeper context.

## Engineering principles

- Keep each implementation small enough to inspect.
- Write tests for the behaviour that exists today.
- Distinguish implemented functionality from planned work.
- Explain the mathematics alongside the code.
- Prefer reproducible examples over unsupported performance claims.

---

Maintained by [Satyen Chaudhari](https://github.com/Saty290501).
