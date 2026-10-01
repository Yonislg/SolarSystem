# Two-Body Orbital Simulation

This project explores the gravitational two-body problem using a simplified Sun–Earth system.

The Sun is assumed to be infinitely more massive than the Earth. As a result, the Sun remains fixed at the origin and only the Earth's motion is considered.

## 1. The Two-Body Problem

According to Newton's law of gravitation, the acceleration of the Earth is

$$
\ddot{\mathbf{r}}
=
-\frac{GM}{|\mathbf{r}|^3}\mathbf{r}
$$

where:

- $\mathbf{r}$ is the Earth's position relative to the Sun,
- $G$ is the gravitational constant,
- $M$ is the mass of the Sun,
- $|\mathbf{r}|$ is the Earth–Sun distance.

Using the standard gravitational parameter

$$
\mu = GM
$$

the governing equation shortens to

$$
\ddot{\mathbf{r}}
=
-\frac{\mu}{r^3}\mathbf{r}
$$



For a bound orbit, the solution is an ellipse centered around the sun.

The orbital shape can be written as

$$
r(\theta)
=
\frac{a(1-e^2)}
{1+e\cos\theta}
$$

where:

- $a$ is the semi-major axis,
- $e$ is the orbital eccentricity,
- $\theta$ is the true anomaly.

When

$$
e = 0,
$$

the orbit is circular.

