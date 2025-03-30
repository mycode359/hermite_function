# Hermite Functions Library

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A Python package for computing quantum harmonic oscillator eigenfunctions (Hermite functions).

## Features
- Normalized Hermite functions ψₙ(x)
- Orthonormality verification
- Visualization tools

## Installation
```bash
pip install git+https://github.com/yourusername/hermite-functions.git
```

## Usage
```python
from hermite import normalized_hermite_function
import numpy as np

x = np.linspace(-4, 4, 500)
psi_2 = normalized_hermite_function(2, x)
```

![Example Plot](examples/plot.png)
