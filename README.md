[![Build Status](https://travis-ci.org/zacikpa/open-source-development-course-hw02-1.svg?branch=master)](https://travis-ci.org/zacikpa/open-source-development-course-hw02-1)

# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
```

Initialization and printing:
```python
a = Vector([0, 1, 2, 3])
b = Vector(size=4)
print(a)

m = Matrix.ident(4)
n = Matrix.square(2)
o = Matrix.from_matrix(n)
print(m)
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
- XOR with a scalar: `a ^ 1`
- Vector XOR: `a ^ b`
- AND with a scalar: `a & 1`
- Vector AND: `a & b`
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
- Addition `m + n`

## Installation

```bash
pip install -U --no-cache . 
```
