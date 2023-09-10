# tessellation

[![PyPI - Version](https://img.shields.io/pypi/v/orbit-tessellation)](https://pypi.org/project/orbit-tessellation/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/orbit-tessellation)](https://pypi.org/project/orbit-tessellation/)
[![tests](https://github.com/ilikecubesnstuff/tessellation/actions/workflows/tests.yml/badge.svg)](https://github.com/ilikecubesnstuff/orbit-tessellation/actions/workflows/tests.yml)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A Python package for evaluating orbit commensurability using Delaunay tessellation. Use this in the [commensurability](https://github.com/ilikecubesnstuff/commensurability) package to analyze galaxy potentials.

## Installation

Install this package via `pip`:

```
python -m pip install orbit-tessellation
```

## Usage

Use `tessellation.Tessellation` on your point array to perform the commensurability evaluation.

```py
import numpy as np
from tessellation import Tessellation

# generate 100 random 2D points
points = np.random.normal(size=(100, 2))
tess = Tessellation(points)
```

This returns a tessellation object that contains info in its attributes. The `.measure` attribute gives the measure of the orbit (normalized to be in `[0, 1)`).
