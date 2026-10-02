from integrators.euler import forward_euler
from bodies import *
from simulation import SolarSystem
from visualization import viz2d


mu = G*SOLAR_MASS
solar_init_pos = np.array([0,0])
solar_init_vel = np.array([0,0])

earth_init_pos = np.array([AU,0])
v_avg = 2*np.pi*AU/T_EARTH
earth_init_vel = np.array([0,v_avg])

sun = Body("Sun",solar_init_pos,solar_init_vel,SOLAR_MASS)
earth = Planet("earth",earth_init_pos,earth_init_vel,EARTH_MASS)
# Just to check the scalability of visualizaton, will remove later
venus = Planet("venus",earth_init_pos/2,earth_init_vel,EARTH_MASS)

dt = 24*60*60

solar_system = SolarSystem(2,SOLAR_MASS)
solar_system.add_planets(earth)
solar_system.add_planets(venus)

def update():
    solar_system.step(forward_euler,dt)

viz2d(solar_system,update)    