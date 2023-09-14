# Introduction

!!! warning "Note to documentation author"
    Incomplete.

Use `tessellation.Tessellation` on your point array to perform the commensurability evaluation.

```py
import numpy as np
from tessellation import Tessellation

# generate 100 random 2D points
points = np.random.normal(size=(100, 2))
tess = Tessellation(points)
```

This returns a tessellation object that contains info in its attributes. The `.measure` attribute gives the measure of the orbit (normalized to be in `[0, 1)`).
