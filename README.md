[![Build Status](https://travis-ci.org/zacikpa/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/zacikpa/open-source-development-course-hw02-1)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
```

Vector initialization and printing:
```python
a = Vector([0, 1, 2, 3])
b = Vector(size=4)
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations:
- Addition with a scalar `a + 1`
- Vector addition: `a + b`
- Vector substraction: `a - b`
- Vector additive inverse: `-a`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector
- Reversing vector elements: `reversed(a)`
- Vector XOR: `a ^ 1`
- Vector length: `a.length()`
- Vector length comparison:
```python
a == b
a != b
a < b
a > b
a >= b
a <= b
```
Caution: `==` operator does **NOT** test for identity, it tests whether the **length** of two vectors is equal.

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```
