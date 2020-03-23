[![Build Status](https://travis-ci.org/jurf/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.org/jurf/open-source-development-course-hw02-1)

# Simple Vector implementation in python

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector
a = Vector([0, 1, 2, 3])
print(a)
```

Operations:
- Addition/subtraction with a scalar `a + 1`
- Vector addition/subtraction: `a + b`
- Scalar multiplication: `k * a`
- Bit-wise XOR: `k ^ a`
- Vector magnitude: `a.length()`
- `reverse()`, `hash()`, `repr()`, `reversed()`, `a[i] = k`

## Installation

```bash
pip install -U --no-cache .
```
