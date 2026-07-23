# Operator Overloading

## What is Operator Overloading?

Python allows classes to redefine the behavior of operators such as: +, -, *, /, **

Instead of using primitive numbers, our `Value` class behaves like a number while recording the computation.

Example:

```python
c = a + b
```

Python internally executes:

```python
c = a.__add__(b)
```

Similarly,

```python
a * b
```

calls

```python
a.__mul__(b)
```

---

## Operators Implemented

| Operator | Magic Method |
|----------|---------------|
| + | __add__ |
| - | __sub__ |
| * | __mul__ |
| / | __truediv__ |
| ** | __pow__ |

---

## Why is this important?

Every operator returns a new `Value` object instead of a primitive number.

The new object stores:

- Computed value
- Parent nodes
- Operation

This allows us to build a computational graph automatically.

---

## Key Takeaways

✔ Operators behave like normal arithmetic.

✔ Every operation creates a new node.

✔ The graph grows automatically as expressions become larger.