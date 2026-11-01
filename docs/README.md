# NN2LLM — Concept Notes

This directory contains concise explanations that accompany the code in the repository. Notes are organised to follow the implementation rather than imply that every topic has already been coded.

## Foundations

1. [Why a Value class?](foundations/01_why_value_class.md)
2. [Operator overloading](foundations/02_operator_overloading.md)
3. [Complex expressions](foundations/03_complex_expressions.md)
4. [Computational graphs](foundations/04_computational_graph.md)
5. [Graph theory](foundations/04.1_graph_theory.md)
6. [Graphs in deep learning](foundations/04.2_graphs_in_deep_learning.md)
7. [PyTorch Autograd](foundations/04.3_pytorch_autograd.md)

## Planned learning areas

The following topics are part of the roadmap. Dedicated notes and implementations will be added as the project progresses:

- Local derivatives and reverse-mode automatic differentiation
- Topological ordering and backpropagation
- Neurons, layers, and multi-layer perceptrons
- Training loops, optimisation, and evaluation
- Character-level language models and tokenization
- Embeddings, attention, transformers, and LLM inference

## How to read the notes

Start with the first-principles explanation, inspect the related implementation under src/, and run the tests under tests/. Some notes discuss framework concepts or planned work for learning purposes; the root README identifies what the current code actually implements.
