import numpy as np

from . import dim2, dim3, generic


class Tessellation:

    def __new__(cls, points, *args, **kwargs):
        dim = len(points[0])
        if dim == 2:
            return dim2.Tessellation(points, *args, **kwargs)
        elif dim == 3:
            return dim3.Tessellation(points, *args, **kwargs)
        else:
            return generic.Tessellation(points, *args, **kwargs)

    @classmethod
    def from_galpy_orbit(cls, orbit, *args, dims=('x', 'y', 'z'), **kwargs):
        axes = [getattr(orbit, dim) for dim in dims]
        points = np.array([ax(orbit.t) for ax in axes]).T
        return cls(points, *args, **kwargs)

    @classmethod
    def from_gala_orbit(cls, orbit, *args, dims=('x', 'y', 'z'), **kwargs):
        points = np.array([getattr(orbit, dim).value for dim in dims]).T
        return cls(points, *args, **kwargs)