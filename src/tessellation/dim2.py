"""
!!! attention "AI-Generated Content"
    This docstring is AI-generated.

Module: dim3

This module provides a 2D tessellation algorithm applied to orbits. It defines the `Tessellation2D` class,
which inherits from `TessellationBase` and includes methods for calculating simplex sides and measures in
two-dimensional space. It also contains the `Normalization` nested class with various normalization methods
for 2D tessellation, including area calculations.

Additionally, it offers a plotting function to visualize the tessellation.

This module is part of the tessellation package and can be used for 2D orbit tessellation tasks.
"""
import numpy as np
from scipy import linalg

try:
    import matplotlib.pyplot as plt

    PLOTTING = True
except ImportError:
    PLOTTING = False

from .base import TessellationBase


class Tessellation2D(TessellationBase):
    """
    !!! attention "AI-Generated Content"
        This docstring is AI-generated.

    A class representing a 2D tessellation applied to orbits.
    """

    @staticmethod
    def simplex_sides(*vertices: np.ndarray) -> list:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Compute the side lengths of a 2D simplex defined by its vertices.

        Args:
            *vertices: The vertices of the simplex.

        Returns:
            list: List of side lengths.

        """
        v1, v2, v3 = vertices
        return [
            linalg.norm(v2 - v1),
            linalg.norm(v3 - v1),
            linalg.norm(v3 - v2),
        ]

    @staticmethod
    def simplex_measure(*vertices: np.ndarray) -> float:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Compute the measure (area) of a 2D simplex defined by its vertices.

        Args:
            *vertices: The vertices of the simplex.

        Returns:
            float: The area of the simplex.

        """
        (x1, y1), (x2, y2), (x3, y3) = vertices
        return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    class Normalization:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        A class providing various methods for normalization in 2D tessellation.

        Methods:
            circle: Compute the area of a circle containing the points.
            default: Default normalization method (circle).

        """

        def circle(self) -> float:
            """
            !!! attention "AI-Generated Content"
                This docstring is AI-generated.

            Compute the area of a circle containing the points.

            Returns:
                float: Area of the circle.

            """
            r = linalg.norm(self.points, axis=1)
            return np.pi * (max(r) ** 2)

        default = circle

    @property
    def area(self) -> float:
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Property to retrieve the area of the tessellation.

        Returns:
            float: Area of the tessellation (same as measure).

        """
        return self.measure

    def plot(
        self,
        plot_included=True,
        plot_removed=False,
        plot_points=True,
        verbosity=1,
        ax=None,
        show=True,
    ):
        """
        !!! attention "AI-Generated Content"
            This docstring is AI-generated.

        Plot the 2D tessellation.

        Args:
            plot_included (bool): Whether to plot included triangles (default True).
            plot_removed (bool): Whether to plot removed triangles (default False).
            plot_points (bool): Whether to plot points (default True).
            verbosity (int): Verbosity level (default 1).
            ax (matplotlib.axes._axes.Axes, optional): Matplotlib axes (default None).
            show (bool): Whether to display the plot (default True).

        Raises:
            ImportError: If Matplotlib is not available.

            RuntimeError: If tessellation failed.

        """
        if not PLOTTING:
            raise ImportError("This method requires matplotlib")
        if self.tri is None:
            raise RuntimeError("Tessellation failed; cannot produce tessellation plot")

        if not ax:
            fig = plt.figure()
            ax = fig.add_subplot()
        X, Y = self.points.T

        if plot_removed:
            plt.triplot(X, Y, self.tri.simplices, mask=self.mask, color="red")
            if verbosity:
                print(self.__class__.__name__, "plotting excluded edges (red):", len(self.mask))

        if plot_included:
            plt.triplot(X, Y, self.tri.simplices, mask=~self.mask, color="green")
            if verbosity:
                print(self.__class__.__name__, "plotting included edges (green):", len(~self.mask))

        if plot_points:
            plt.plot(X, Y, "k.", markersize=0.5)
            if verbosity:
                print(self.__class__.__name__, "plotting points:", len(X))

        if show:
            plt.show()
        return ax
