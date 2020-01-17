# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
```

Vector initialization and printing:
```python
a = Vector([0, 1, 2, 3])
b = Vector(size=4)
print(a)
```

Operations:
- Addition with a scalar `a + 1`
- Vector addition: `a + b`
- Vector substraction: `a - b`
- Multiplication with a scalar `2 * a`
- Vector additive inverse: `-a`
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


## Installation

```bash
pip install -U --no-cache . 
```
