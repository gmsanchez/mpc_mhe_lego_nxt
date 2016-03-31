import numpy as np

Nx = 3
Nu = 1
Ny = 1
Nw = Nx
Nv = Ny

w0 = np.zeros(Nx)
v0 = np.zeros(Ny)

# Parameters of the system
k1 = 0.5
k_1 = 0.05
k2 = 0.2
k_2 = 0.01
RT = 32.84


# Continuous-time models.
def f(x, u, w=[0,0,0]): # We define the model with u, but there isn't one.
    # [cA, cB, cC] = x[:Nx] # Doesn't work in Casadi 3.0.
    cA = x[0]
    cB = x[1]
    cC = x[2]
    rate1 = k1*cA - k_1*cB*cC
    rate2 = k2*cB**2 - k_2*cC
    return np.array([-rate1 + w[0], rate1 - 2*rate2 + w[1], rate1 + rate2 + w[2]])


def h(x):
    return RT*(x[0] + x[1] + x[2])