from __future__ import annotations

import inspect
from typing import Any, Optional

import numpy as np

from .base import TessellationBase as _TessType
from .dim2 import Tessellation2D as _Tess2D
from .dim3 import Tessellation3D as _Tess3D
from .exceptions import LowDimensionalityException
from .generic import TessellationGeneric as _TessND


def Tessellation(
    orbit_or_point_array: Any,
    dims_for_orbit: Optional[tuple[str]] = None,
    *,
    incremental: bool = True,
    qhull_options: Optional[str] = None,
    axis_ratio: float = 10,
    normalization_routine: str = "default",
    verbosity: int = 0,
) -> _TessType:
    points = orbit = orbit_or_point_array

    pkg = None
    module = inspect.getmodule(orbit)
    if module:
        pkg, *_ = module.__name__.partition(".")

    if pkg in ("galpy", "gala", "agama"):
        orbit = orbit_or_point_array
        if dims_for_orbit is None:
            raise TypeError("Orbit dimensions must be supplied if tessellating an orbit object")
        if pkg == "galpy":
            axes = [getattr(orbit, dim) for dim in dims_for_orbit]
            points = np.array([ax(orbit.t) for ax in axes]).T
        elif pkg == "gala":
            points = np.array([getattr(orbit, dim).value for dim in dims_for_orbit]).T
        elif pkg == "agama":
            raise NotImplementedError()
    else:
        if dims_for_orbit is not None:
            raise ValueError("Orbit dimensions must only be passed with an orbit object")
        points = np.array(points, dtype=float)

    if points.ndim != 2:
        raise ValueError(
            "Tessellation can only be performed on a 2D array of shape (npoints, ndim)"
        )

    init_args = dict(
        points=points,
        incremental=incremental,
        qhull_options=qhull_options,
        axis_ratio=axis_ratio,
        normalization_routine=normalization_routine,
        verbosity=verbosity,
    )

    # NOTE: ndim is not the same as points.ndim
    *_, ndim = points.shape
    if ndim == 2:
        return _Tess2D(**init_args)
    elif ndim == 3:
        return _Tess3D(**init_args)
    elif ndim > 3:
        return _TessND(**init_args)
    else:
        raise LowDimensionalityException(
            "Unsupported dimensionality, requires dimension 2 or greater"
        )
