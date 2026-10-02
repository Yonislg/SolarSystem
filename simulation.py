import forces
import numpy as np
from bodies import Body,G


class SolarSystem:
    def __init__(self,dim,solar_mass):
        self.dim = dim
        self.planets = []
        self.sun = Body("Sun",np.zeros(dim),np.zeros(dim),solar_mass)
        self.mu = G*solar_mass

    def add_planets(self,planet):
        self.planets.append(planet)

    def step(self,integrator,dt):        
        for planet in self.planets:
            force_eq = forces.gravacc(self.mu,planet.position)
            planet.step(force_eq,integrator,dt)



