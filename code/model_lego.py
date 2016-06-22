# -*- coding: utf-8 -*-
import numpy as np
import casadi

Nx = 11
Ny = 2
Nu = 2
Nw = Nx
Nv = Ny
Np = 1

w0 = np.zeros(Nx)
v0 = np.zeros(Ny)

# Lego parameters
# http://www.mathworks.com/matlabcentral/fileexchange/35206-simulink-support-package-for-lego-mindstorms-nxt-hardware--r2012a-/content/lego/legodemos/lego_selfbalance_plant.m
# http://www.nt.ntnu.no/users/skoge/prost/proceedings/ecc-2013/data/papers/0959.pdf
# DC motor state space system model
# http://ctms.engin.umich.edu/CTMS/index.php?example=MotorPosition&section=SystemModeling

wR = 0.028 #0.0216 # (43.2*0.5)/1000.0   # Wheel radius [mm]
wB = 0.12  #0.105 # 105.0/1000.0       # Distance between wheels [mm]
#wR = 0.028 # (43.2*0.5)/1000.0   # Wheel radius [mm]
#wB = 0.120  #0.105 # 105.0/1000.0       # Distance between wheels [mm]
fm = 0.0022     # motor viscous friction constant
Jm = 1e-5       # DC motor inertia moment [kgm^2]
Rm = 6.69       # DC motor resistance []
Kb = 0.468      # DC motor back EMF constant [Vsec/rad]
Kt = 0.317      # DC motor torque constant [Nm/A]
Gu = 1E-2       # PWM gain factor
Vb = 8.00       # V Power Supply voltage
Vo = 0.625      # V Power Supply offset
mu = 1.089      # Power Supply gain factor =
Vo_l = 0.68
Vo_r = 0.68
mu_l = 1.04
mu_r = 0.99
L = 1.0


def f(x, u, w=w0, Vb=Vb):
    """
    Model for a differential drive mobile robot.
    x[0] -> x
    x[1] -> y
    x[2] -> \psi
    x[3] -> \theta_l
    x[4] -> \omega_l
    x[5] -> i_l
    x[6] -> \theta_r
    x[7] -> \omega_r
    x[8] -> i_r
    """
    # wR = 43.2*0.5 # Wheel radius [mm]
    # wB = 82.0 # Distance between wheels [mm]
    # fm = 0.0022 # motor viscous friction constant
    # Jm = 1e-5           # DC motor inertia moment [kgm^2]
    # Rm = 6.69           # DC motor resistance []
    # Kb = 0.468          # DC motor back EMF constant [Vsec/rad]
    # Kt = 0.317          # DC motor torque constant [Nm/A]
    # Gu = 1E-2 #PWM gain factor
    # Vb = 8.00 #V Power Supply voltage
    # Vo = 0.625 #V Power Supply offset
    # mu = 1.089 #Power Supply gain factor
    # L = 1.0
    #if len(x.shape)>1:
    #    x = x.ravel()
    #if len(u.shape)>1:
    #    u = u.ravel()
    
    return np.array([0.5*wR*(x[4]+x[7])*casadi.cos(x[2]),
                     0.5*wR*(x[4]+x[7])*casadi.sin(x[2]),
                     (wR/wB)*(x[7]-x[4]),
                     x[4],
                     -(fm/Jm)*x[4] + (Kt/Jm)*x[5],
                     -(Kb/L)* x[4] - (Rm/L)* x[5] + ((Gu*(x[9]*Vb-Vo_l))/L)*u[0],
                     x[7],
                     -(fm/Jm)*x[7] + (Kt/Jm)*x[8],
                     -(Kb/L)* x[7] - (Rm/L)* x[8] + ((Gu*(x[10]*Vb-Vo_r))/L)*u[1],
                     0,
                     0])


def h(x, v=v0):
    return np.array([x[3],x[6]])
