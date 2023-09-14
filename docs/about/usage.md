# Start Using `orbit-tessellation`

!!! warning "Note to documentation author"
    Clunky section, clean up code blocks into smaller steps with more granular guidance and better focus.

Follow the [installation](../installation.md) guide to install the package on your machine.

Although the PyPI package name is `orbit-tessellation`, the package is imported with the name `tessellation`. To get started, import `Tessellation` from here and call it passing in your point array.

```py
from tessellation import Tessellation
tess = Tessellation(points)
```

This should create a tessellation object specific to the dimensionality of your points. (For dimensions larger than 3, a generic N-dimensional class is used.)

For a full walkthrough, see the [user guide](../user/index.md).

## 2D Example

``` py
import numpy as np
from tessellation import Tessellation

rng = np.random.default_rng(0)
points = rng.uniform(-1, 1, (100, 2))  # 2D point array
tess = Tessellation(points)

print(tess)
# Tessellation2D[measure=0.6117203428434417]
print(tess.measure)
# 0.6117203428434417
print(tess.points)
# array([[ 2.73923375e-01, -4.60426572e-01],
#        [-9.18052952e-01, -9.66944729e-01],
# ...
print(tess.tri.simplices)
# array([[24, 48, 46],
#        [56,  1,  5],
# ...
print(tess.mask)
# array([ True, False,  True,  True,  True,  True,  True,  True,  True,
#         True,  True,  True,  True,  True,  True,  True,  True,  True,
# ...
```

## 3D Example

``` py
import numpy as np
from tessellation import Tessellation

rng = np.random.default_rng(0)
points = rng.uniform(-1, 1, (100, 3))  # 3D point array
tess = Tessellation(points)

print(tess)
# Tessellation3D[measure=0.7958927374074697]
print(tess.measure)
# 0.7958927374074697
print(tess.points)
# array([[ 2.73923375e-01, -4.60426572e-01, -9.18052952e-01],
#        [-9.66944729e-01,  6.26540478e-01,  8.25511155e-01],
# ...
print(tess.tri)
# array([[53, 74,  1, 50],
#        [18, 20, 74, 50],
# ...
print(tess.mask)
# array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#         True,  True,  True,  True,  True,  True,  True,  True,  True,
# ...
```

## Using Galpy/Gala

=== "Galpy"

    ``` py
    import numpy as np
    import astropy.units as u

    import galpy.potential as gp
    import galpy.orbit as o

    from tessellation import Tessellation

    mw = gp.MWPotential2014
    t = np.linspace(0, 2, 501) * u.Gyr

    orbit = o.Orbit([
        8 * np.random.random() * u.kpc,       # R
        0 * u.km/u.s,                         # vR
        200 * np.random.random() * u.km/u.s,  # vT
        2 * np.random.random() * u.kpc,       # z
        0 * u.km/u.s,                         # vz
        0 * u.deg                             # phi
    ])
    orbit.integrate(t, mw)

    tess = Tessellation(orbit)
    print(tess.measure)
    ```

=== "Gala"

    ``` py
    import numpy as np
    import astropy.units as u

    import gala.potential as gp
    import gala.dynamics as gd

    from tessellation import Tessellation

    mw = gp.MilkyWayPotential()
    t = np.linspace(0, 2, 501) * u.Gyr

    w0 = gd.PhaseSpacePosition(
        pos = [
            8 * np.random.random(), 0, 2 * np.random.random()
        ] * u.kpc,
        vel = [
            0, 200 * np.random.random(), 0
        ] * u.km/u.s,
    )
    orbit = mw.integrate_orbit(w0, t=t)

    tess = Tessellation(orbit)
    print(tess.measure)
    ```
