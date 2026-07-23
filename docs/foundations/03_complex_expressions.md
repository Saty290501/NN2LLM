# Complex Expressions

## Overview

Until now, we have implemented arithmetic operators for our `Value` class:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`**`)

Each operator creates a new `Value` object while preserving the computation history.

However, real neural networks rarely perform a single operation. Instead, they execute a sequence of interconnected mathematical operations called **complex expressions**.

---

# Why are Complex Expressions Important?

A neural network is essentially one large mathematical expression.

For example, a single neuron computes:

```text
output = (x1 * w1) + (x2 * w2) + bias
```

Even this simple neuron contains multiple operations.

As neural networks become deeper, these expressions grow into large computational graphs.

Without understanding complex expressions, it is impossible to understand:

- Computational Graphs
- Automatic Differentiation
- Backpropagation
- Neural Network Training

---

# From Simple to Complex

## Simple Expression

```python
c = a + b
```

Graph

```text
a ----\
       +
b ----/
```

---

## Slightly More Complex

```python
d = (a * b) + c
```

Graph

```text
      d
      +
     / \
    *   c
   / \
  a   b
```

---

## Complex Expression

```python
output = ((a * b) + (c + d)) ** 2 / a
```

Graph

```text
                 output (/)
                 /       \
            h (**2)       a
               |
             g (+)
            /     \
        e (*)     f (+)
       /   \      /   \
      a     b    c     d
```

---

# Step-by-Step Evaluation

```python
a = Value(2.0)
b = Value(3.0)
c = Value(4.0)
d = Value(5.0)

e = a * b
f = c + d
g = e + f
h = g ** 2
output = h / a
```

### Step 1

```python
e = a * b
```

Result

```text
6
```

---

### Step 2

```python
f = c + d
```

Result

```text
9
```

---

### Step 3

```python
g = e + f
```

Result

```text
15
```

---

### Step 4

```python
h = g ** 2
```

Result

```text
225
```

---

### Step 5

```python
output = h / a
```

Result

```text
112.5
```

---

# Why Doesn't Python's float Work?

Consider:

```python
a = 2
b = 3

c = a * b
```

Python stores:

```text
c = 6
```

But it forgets:

- Which values created `6`
- Which operation created it
- The sequence of computations

Therefore, Python's built-in numeric types cannot perform automatic differentiation.

---

# How Does the Value Class Help?

Instead of storing only a number, every `Value` object stores:

```text
Value
│
├── data
├── grad
├── parents
├── operation
├── label
└── _backward
```

Every operation creates another `Value` object.

This automatically builds a computation graph.

---

# Dependency Chain

The final output depends on every previous computation.

```text
output

↓

h

↓

g

↓

e      f

↓

a b    c d
```

Understanding these dependencies is the key to understanding backpropagation.

---

# Connection with Deep Learning

When you execute:

```python
loss = model(inputs)
```

PyTorch records every mathematical operation.

Later, when you call:

```python
loss.backward()
```

PyTorch traverses the computation graph in reverse order and computes gradients.

Our implementation follows the same idea.

---

# Q&A

### What is a complex expression?

A complex expression is a mathematical expression composed of multiple operations whose intermediate results depend on one another.

---

### Why do we study complex expressions?

Because every neural network forward pass is a complex mathematical expression.

---

### Why are intermediate values stored?

Intermediate values preserve computation history, allowing gradients to be computed during backpropagation.

---

### What information does every Value object store?

- Numerical value
- Gradient
- Parent nodes
- Mathematical operation
- Label
- Backward function

---

### Why is computation history important?

Without computation history, it is impossible to determine how changes in an input affect the final output.

---

# Key Takeaways

- Complex expressions consist of multiple connected operations.
- Every intermediate result becomes a new `Value` object.
- Parent relationships form a computational graph.
- The computation graph records the complete history of a forward pass.
- This graph is the foundation of automatic differentiation and backpropagation.

---

# Next Chapter

➡️ Computational Graph

In the next chapter, we will learn how these interconnected `Value` objects form a graph and how to traverse that graph using Depth-First Search (DFS).