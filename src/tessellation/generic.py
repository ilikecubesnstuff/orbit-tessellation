"""
!!! attention "AI-Generated Content"
    This docstring is AI-generated.

Module: generic

This module provides a tessellation algorithm applied to orbits using a generic approach.

It defines the `TessellationGeneric` class, which inherits from `TessellationBase` and includes methods for
calculating simplex sides and measures. It also contains the `Normalization` nested class with various
normalization methods for tessellation, including volume approximations and convex hull calculations.

This module is part of the tessellation package and can be used for various orbit tessellation tasks.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np
from scipy import linalg, spatial

from .base import TessellationBase


class TessellationGeneric(TessellationBase):
    """
    !!! attention "AI-Generated Content"
        This docstring is AI-generated.

    A class representing a generic tessellation applied to orbits.
    """

    @staticmethod
    def simplex_sides(*vertices: np.ndarray) -> float:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Compute the sides of a simplex defined by its vertices.

        Args:
            *vertices: The vertices of the simplex.

        Returns:
            list: List of side lengths.

        Note:
            This method uses a combinatoric approach, which may not be practical in most cases.
        """
        return [v2 - v1 for v1, v2 in combinations(vertices, 2)]

    @staticmethod
    def simplex_measure(*vertices: np.ndarray) -> float:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Compute the measure (volume) of a simplex defined by its vertices.

        Args:
            *vertices: The vertices of the simplex.

        Returns:
            float: The volume of the simplex.

        Note:
            This method calculates the general simplex volume, which may not be practical in most cases.
        """
        first, *rest = vertices
        dim = len(first)
        mat = [v - first for v in rest]
        return linalg.det(mat) / np.math.factorial(dim)

    class Normalization(TessellationBase):
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        A class providing various methods for normalization in tessellation.

        Methods:
            nsphere_approx: Compute the approximate volume of an n-sphere containing the points.
            convexhull: Compute the volume of the convex hull of the points.
            convexhull_rot4: Compute the volume of the convex hull after rotation by 90 degrees four times.
            default: Default normalization method (convexhull_rot4).
        """

        def nsphere_approx(self) -> float:
            """
            !!! attention "AI-Generated Content"
                This docstring is AI-generated.

            Compute an approximate volume of an n-sphere containing the points.

            Returns:
                float: Approximate volume of the n-sphere.

            Note:
                This method uses Stirling's approximation, which may not be suitable for all cases.
            """
            d = self.points.shape[1]
            r = linalg.norm(self.points, axis=1)
            return 1 / np.sqrt(d * np.pi) * (2 * np.pi * np.e / d) ** (d / 2) * np.max(r) ** d

        def convexhull(self) -> float:
            """
            !!! attention "AI-Generated Content"
                This docstring is AI-generated.

            Compute the volume of the convex hull of the points.

            Returns:
                float: Volume of the convex hull.

            Note:
                This method may not work correctly for co-rotation cases.
            """
            points = self.tri.convex_hull
            return spatial.ConvexHull(points).volume

        def convexhull_rot4(self) -> float:
            """
            !!! attention "AI-Generated Content"
                This docstring is AI-generated.

            Compute the volume of the convex hull after rotation by 90 degrees four times.

            Returns:
                float: Volume of the convex hull after rotation.

            Note:
                This method involves specific rotations of the points.
            """
            x, y, *rest = self.points.T
            r000 = np.array([+x, +y, *rest]).T
            r090 = np.array([-y, +x, *rest]).T
            r180 = np.array([-x, -y, *rest]).T
            r270 = np.array([+y, -x, *rest]).T

            points = np.array([*r000, *r090, *r180, *r270])
            hull = spatial.ConvexHull(points)
            return hull.volume

        default = convexhull_rot4
