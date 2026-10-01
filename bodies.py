import numpy as np
import scipy.constants as scic

G = scic.G

SOLAR_MASS = 1.9884*10**30
AU = scic.au

T_EARTH = scic.Julian_year

EARTH_ECCENTRICITY = 0.0167
EARTH_MASS = 5.9722*10*24

class Body:
    def __init__(self,name,position,velocity,mass):
        self.name = name
        self.position = position
        self.velocity = velocity
        self.mass = mass