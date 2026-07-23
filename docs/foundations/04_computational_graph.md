# Chapter 3: Computational Graph

> "Before a machine can learn how to improve a computation, it must first remember how that computation happened."

---

# Overview

So far in the project, we have implemented a custom `Value` class that supports arithmetic operations such as:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`**`)

Every operation creates a new `Value` object.

At first glance, this may seem unnecessary because Python's built-in numeric types already perform these operations.

However, there is a fundamental difference.

Python computes only the **final numerical result**, while our `Value` class records **how that result was produced**.

That recorded history is called a **Computational Graph**.

This chapter explains what a computational graph is, why it is one of the most important concepts in Deep Learning, and how it prepares us for Automatic Differentiation and Backpropagation.

---

# Learning Objectives

By the end of this chapter, you should be able to answer:

- What is a computational graph?
- Why is it represented as a graph?
- Why is it a Directed Acyclic Graph (DAG)?
- Why does every `Value` object store its parents?
- How does PyTorch build computational graphs?
- Why does `loss.backward()` start from the output node?

---

# Why Are We Learning This?

Imagine building a neural network.

The network receives an input.

It performs thousands of mathematical operations.

Finally, it produces a prediction.

Example:

```text
Prediction = 0.91
```

Suppose the correct answer is:

```text
Target = 1.00
```

The model is wrong.

Now ask yourself:

> Which weight caused this error?

To answer that question, we must know exactly **how the prediction was computed**.

If the computation history is lost, learning becomes impossible.

The computational graph preserves that history.

---

# Mathematics Perspective

Consider the expression:

```text
y = (a × b) + c
```

Instead of viewing this as one equation, we break it into smaller computations.

```text
d = a × b

y = d + c
```

Now each intermediate computation becomes a separate mathematical object.

This decomposition allows us to compute derivatives one step at a time using the Chain Rule.

---

# Computer Science Perspective

A computational graph is simply a graph data structure.

It consists of:

- Nodes
- Edges

## Nodes

Nodes represent values.

Examples:

```text
a

b

c

d

output
```

---

## Edges

Edges represent dependencies.

If node B depends on node A, we draw an edge.

```text
A -----> B
```

This means:

> "B cannot be computed until A exists."

---

# Example

Expression

```text
output = (a × b) + c
```

Graph

```text
          output
             +
            / \
           *   c
          / \
         a   b
```

Notice that the graph stores relationships instead of only numbers.

---

# Directed Graph

A computational graph is directed.

The arrows always point from earlier computations toward later computations.

```text
a

↓

*

↓

+

↓

output
```

The computation has a direction.

Inputs → Intermediate Results → Output

---

# Why Is It A DAG?

A computational graph is a **Directed Acyclic Graph (DAG).**

Directed

- Information flows in one direction.

Acyclic

- There are no circular dependencies.

Valid

```text
a → b → c
```

Invalid

```text
a → b → c
↑       ↓
└───────┘
```

A cycle would mean:

> "This value depends on itself."

That makes computation impossible.

---

# Why Not Store Only Numbers?

Suppose Python computes

```python
c = a * b
```

Python stores

```text
6
```

It forgets

- Which numbers created 6
- Which operator created 6
- How to compute gradients

Our `Value` class stores

```text
Value

├── data
├── grad
├── parents
├── operation
├── label
└── _backward
```

Instead of storing only the answer, it stores the entire computation history.

---

# Intuition

Imagine baking a cake.

The final cake is the output.

If someone asks,

> "Which ingredient made the cake too sweet?"

You cannot answer if all you have is the finished cake.

You need the recipe.

The computational graph is the recipe of every mathematical computation.

---

# How Our Value Class Builds The Graph

When we write

```python
c = a * b
```

our implementation creates

```text
Value

data = 6

parents = (a, b)

operation = "*"
```

Nothing more.

Nothing less.

The graph is not stored in one giant object.

It is distributed across every `Value` object through the `parents` relationship.

---

# Example

Expression

```text
output = ((a × b) + d)
```

Graph

```text
           output
              +
             / \
            *   d
           / \
          a   b
```

Every node knows only its immediate parents.

Together, all nodes form the complete computational graph.

---

# Engineering Insight

Notice something interesting.

Our implementation never created a separate `Graph` class.

Why?

Because the graph emerges naturally from object relationships.

Every `Value` object is a node.

Every `parents` reference is an edge.

The graph already exists.

We simply have not traversed it yet.

---

# Deep Learning Perspective

Every neural network performs a forward pass.

Example

```text
Input

↓

Linear Layer

↓

Activation

↓

Linear Layer

↓

Loss
```

Each layer creates new intermediate values.

Those intermediate values become nodes inside a computational graph.

The larger the neural network, the larger the graph.

---

# PyTorch Internals

When we write

```python
loss = model(x)
```

PyTorch performs two tasks simultaneously.

1. Computes the numerical result.

2. Builds a computational graph.

Every Tensor remembers how it was created.

Internally, tensors contain references such as:

- `grad_fn`
- `next_functions`

These form the graph that Autograd later traverses.

When we execute

```python
loss.backward()
```

PyTorch does **not** recompute the forward pass.

Instead, it walks backward through the graph that was already built.

---

# Why Does Backward Start From The Output?

Suppose we want

```text
∂Loss / ∂Weight
```

The derivative begins from the final loss.

Then it propagates backwards through every dependency until every parameter receives its gradient.

Therefore,

```python
loss.backward()
```

always starts from the output node.

---

# Common Misconceptions

### ❌ A computational graph stores only numbers.

False.

It stores relationships between computations.

---

### ❌ The graph is built during backpropagation.

False.

The graph is built during the forward pass.

Backpropagation only traverses it.

---

### ❌ Every graph needs a Graph class.

False.

Our graph is formed naturally through object references.

---

### ❌ Intermediate values are temporary.

False.

Intermediate values are essential because gradients flow through them.

---

# Connection To NN2LLM

Current implementation

```text
Value

├── data
├── grad
├── parents
├── operation
├── label
└── _backward
```

Current status

```
Project Setup                 ✅
Value Class                   ✅
Operator Overloading          ✅
Complex Expressions           ✅

Computational Graph           ← You are here
```

Everything implemented so far has been preparing for this chapter.

The `parents` attribute is no longer just metadata.

It is the edge of our computational graph.

---

# What's Next?

Now that we understand **what** a computational graph is, we need to answer a more practical question.

Suppose we have only the final output node.

How do we visit every node exactly once?

This leads us to our first graph algorithm:

**Depth-First Search (DFS)**

DFS will become the foundation for graph traversal, topological sorting, and eventually backpropagation.

---

# Interview Questions

### What is a computational graph?

A computational graph is a Directed Acyclic Graph (DAG) in which nodes represent values or operations, and edges represent dependencies between computations.

---

### Why do deep learning frameworks build computational graphs?

To preserve computation history so gradients can be computed automatically during backpropagation.

---

### Why is the graph directed?

Because computations have a dependency order that flows from inputs to outputs.

---

### Why must the graph be acyclic?

Because cyclic dependencies make evaluation and differentiation impossible.

---

### Where is the graph stored in NN2LLM?

The graph is stored implicitly through the `parents` attribute of every `Value` object.

---

# Key Takeaways

- A computational graph records the complete history of a computation.
- Every `Value` object represents a node in the graph.
- Parent references create the edges between nodes.
- The graph is built during the forward pass.
- Backpropagation traverses this graph in reverse.
- Understanding computational graphs is essential before implementing automatic differentiation.