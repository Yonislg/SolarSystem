import numpy as np


# gravitational accelaratin
def gravacc(mu,pos):
    r = np.linalg.norm(pos)
    acc = -mu*pos/r**3
    return acc