from integrators.euler import forward_euler
from bodies import *
import forces
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mu = G*SOLAR_MASS
solar_init_pos = np.array([0,0])
solar_init_vel = np.array([0,0])

earth_init_pos = np.array([AU,0])
v_avg = 2*np.pi*AU/T_EARTH
earth_init_vel = np.array([0,v_avg])

sun = Body("Sun",solar_init_pos,solar_init_vel,SOLAR_MASS)
earth = Body("earth",earth_init_pos,earth_init_vel,EARTH_MASS)

dt = 24*60*60

def update(earth):
    earth.acceleration = forces.gravacc(mu,earth.position)
    earth.velocity = forward_euler(earth.velocity,earth.acceleration,dt)
    earth.position = forward_euler(earth.position,earth.velocity,dt)
    return earth

scale = AU/5

fig, ax = plt.subplots()

ax.set_aspect("equal")
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

ax.set_xlabel(f"x / ({scale:.2e} m)")
ax.set_ylabel(f"y / ({scale:.2e} m)")

# Earth
earth_plot, = ax.plot([], [], "bo")

# Optional orbit trail
trail_plot, = ax.plot([], [], "-", linewidth=1)

trail_x = []
trail_y = []


def animate(frame):
    update(earth)

    # scaled coordinates
    x = earth.position[0] / scale
    y = earth.position[1] / scale

    earth_plot.set_data([x], [y])

    # save orbit trail
    trail_x.append(x)
    trail_y.append(y)

    trail_plot.set_data(trail_x, trail_y)

    return earth_plot, trail_plot


ani = FuncAnimation(
    fig,
    animate,
    frames=365,
    interval=20,
    blit=False
)

plt.show()