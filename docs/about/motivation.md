# Motivation

!!! warning "Note to documentation author"
    Generate images to explain with visual examples.

!!! warning "Note to documentation author"
    This summary needs reworking after finishing the remaining sections.

Most orbits in a galaxy will fill a [toroid](https://en.wikipedia.org/wiki/Toroid) fully over time. A special class of orbits will repeat its tracks and only probe a small sub-volume of the toroid - these orbits are called "commensurate".

Commensurate orbits are closely linked with *resonant* orbits, and these are often probed with the use of frequency analysis tools (such as [superfreq](https://superfreq.readthedocs.io/en/latest/) or [naif](https://naif.readthedocs.io/en/latest/)). By relying on the stability of an orbit's kinematic frequencies, the fundamental frequencies can be extracted after sufficiently long orbit integration.

Orbit tessellation aims to pick out commensurate orbits with lower orbit integration timescales, as well as pick out commensurabilities in cases where the kinematic frequencies need not stay constant (such as in an evolving potential).

## Orbit Classification

!!! warning "Note to documentation author"
    [General questions:] What is orbit classification? Why is it interesting/important?

## Resonant Orbits

Orbits are *resonant* if the frequencies of their motion (angular, radial, vertical) become commensurable (in rational proportion). In 3D, resonances are a phenomenon govenred by the equation:

$$ m\Omega_p = n_1\Omega_r + n_2\Omega_\varphi + n_3\Omega_z $$

Resonances are crucial because in a collisionless system, they are the only places where orbits can gain or lose conserved quantities such as energy and angular momentum.

From ["The capture and escape of stars"](https://academic.oup.com/mnras/article/285/1/49/993447):
> Why are the resonant orbits so important? Suppose a disturbance rotating at angular frequency $\Omega_p$ is applied to the disc. On each traverse, the resonant stars meet the crests and troughs of the perturbation potential at the same spots in their orbits and this causes secular change in the orbital elements. The non-resonant stars feel only periodic fluctuations that average to zero. As the strength of the perturbation increases, stars near the locus of exact resonance are captured into libration around the parent periodic orbit. So, the neighbourhoods of the resonances are the regions of a galaxy where a disturbance can produce long-term effects by changing populations of orbital families.

### Frequency Analysis

!!! warning "Note to documentation author"
    Briefly describe what frequency analysis is and how existing tools have worked.

## Repeated Tracks

Commensurate orbits are those that repeat its tracks over its orbit, probing a relatively small volume in 3D space.

To formalize this notion, an algorithm developed in ["Using commensurabilities and orbit structure to understand barred galaxy evolution"](https://academic.oup.com/mnras/article/500/1/838/5925365) tessellates the points from orbit integration and trims simplices that connected unrelated parts of the orbit. Unrelated parts of the orbit must be connected by simplices of large "axis ratios", so this is set as the trimming criterion.

For specific details, see [the algorithm](algorithm.md).
