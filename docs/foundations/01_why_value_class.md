# Why Value Class?

## Problem

Python's built-in numeric types (`int` and `float`) only store a numerical value.

Example:

```python
a = 2
b = 3

c = a * b
```

Python computes:

```
c = 6
```

However, it does not remember:

- Which values created `6`
- Which mathematical operation was used
- How to compute gradients

---

## Solution

Instead of using primitive numbers, deep learning frameworks use custom objects.

Our `Value` class stores:

- data
- gradient
- parent nodes
- operation
- label
- backward function

This allows every computation to become part of a computational graph.

---

## Why is it important?

Without the `Value` class:

- No computational graph
- No automatic differentiation
- No backpropagation
- No neural network training

---

## Key Takeaways

✔ Value stores both data and computation history.

✔ Every mathematical operation creates a new Value object.

✔ This forms the foundation of an automatic differentiation engine.