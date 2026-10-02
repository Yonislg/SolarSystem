from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from bodies import AU

def viz2d(solar_system,update):
    scale = AU/5

    fig, ax = plt.subplots()

    ax.set_aspect("equal")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)

    ax.set_xlabel(f"x / (5 au)")
    ax.set_ylabel(f"y / (5 au)")

    #sun
    sun_plot = ax.plot(0,0,"yo")

    # Earth
    for planet in solar_system.planets:
        planet.plot, = ax.plot([], [], "bo")

        # Optional orbit trail
        planet.trail, = ax.plot([], [], "-", linewidth=1)

        planet.trail_x = []
        planet.trail_y = []


    def animate(frame):
        update()
        
        # scaled coordinates
        for planet in solar_system.planets:
            x = planet.position[0] / scale
            y = planet.position[1] / scale

            planet.plot.set_data([x], [y])

            # save orbit trail
            planet.trail_x.append(x)
            planet.trail_y.append(y)

            planet.trail.set_data(planet.trail_x, planet.trail_y)

        return


    ani = FuncAnimation(
        fig,
        animate,
        frames=365,
        interval=20,
        blit=False
    )

    plt.show()