# Compare integrators and the absolute value of their errors.
# CasADi cvodes vs RK4 vs LTV.

import casadi
import numpy as np
import tools
import util
import model_lego as model
import matplotlib.pyplot as plt

plt.interactive(True)
doSimPlots = True

Nsim = 80

Nx = model.Nx
Nu = model.Nu
Ny = model.Ny
Nw = Nx
Nv = Ny

Delta = 0.1

sigma_w = 0.5   # Standard deviation for the process noise
sigma_v = 0.25  # Standard deviation of the measurements
sigma_p = .5    # Standard deviation for prior

f = model.F
h = model.H

f_casadi = tools.getCasadiFunc(f, [Nx, Nu, Nw], ["x", "u", "w"], "F", rk4=False)
f_casadi_rk4 = tools.getCasadiFunc(f, [Nx, Nu, Nw], ["x", "u", "w"], "F_rk4", rk4=True, Delta=Delta, M=5)
f_casadi_int = tools.getCasadiIntegrator(f, Delta, [Nx, Nu, Nw], ["x", "u", "w"], "F_int")

h_casadi = tools.getCasadiFunc(h, [Nx], ["x"], "H")


def _calc_lin_disc_wrapper_for_mp_map(item):
    """ Function wrapper for map or multiprocessing.map . """
    _xi, _ui, _wi, _Delta = item
    Ai = f_casadi.jacobian(0, 0)(_xi, _ui, _wi)[0].full()
    Bi = f_casadi.jacobian(1, 0)(_xi, _ui, _wi)[0].full()
    Gi = f_casadi.jacobian(2, 0)(_xi, _ui, _wi)[0].full()
    Ei = f_casadi(_xi, _ui, _wi).full().ravel() - Ai.dot(_xi).ravel() - Bi.dot(_ui).ravel() - Gi.dot(_wi).ravel()
    [Ai[:], Bi[:], Gi[:], Ei[:]] = util.c2d(Ai, Bi, _Delta, Gi, Ei)
    return Ai, Bi, Gi, Ei

# Simulate everything
# _x0bar = np.array([1.0, 0.0, 4.0])
_x0 = np.zeros((Nx,))
_u0 = np.zeros((Nu,))

wsim = 0.0*sigma_w*np.fabs(np.random.randn(Nsim, Nw))
vsim = 0.0*sigma_v*np.random.randn(Nsim, Nv)

usim = [10.0, 20.0]*np.ones((Nsim, Nu))
ysim = np.zeros((Nsim, Ny))

xsim_rk4 = np.zeros((Nsim+1, Nx))
xsim_rk4[0,:] = _x0
xsim_int = np.zeros((Nsim+1, Nx))
xsim_int[0,:] = _x0
xsim_ltv = np.zeros((Nsim+1, Nx))
xsim_ltv[0,:] = _x0

for t in range(Nsim):
    # Measure.
    # ysim[t] = h(xsim[t,:]) + vsim[t,:]
    # Simulate with CasADi integrator.
    xsim_int[t+1,:] = f_casadi_int(xsim_int[t,:], usim[t,:], wsim[t,:]).full().ravel() #F_integrator(x0=xsim_int[t,:],p=np.hstack((usim[t,:],wsim[t,:])))['xf'].full().ravel()
    xsim_rk4[t+1,:] = f_casadi_rk4(xsim_rk4[t,:], usim[t,:], wsim[t,:]).full().ravel()
    # Simulate with LTV model.
    Ad, Bd, Gd, fd = _calc_lin_disc_wrapper_for_mp_map((xsim_ltv[t,:], usim[t,:], wsim[t,:], Delta))
    xsim_ltv[t+1,:] = Ad.dot(xsim_ltv[t,:]) + Bd.dot(usim[t,:]) + Gd.dot(wsim[t,:]) + fd


fontsize = 12
pltDim = (Nx, 2)

if doSimPlots:
    f, axarr = plt.subplots(*pltDim)

    for i in range(Nx):
        thisPos = np.unravel_index(i, pltDim, order='F')
        axarr[thisPos].plot(xsim_ltv[:,i], 'k--', label='ltv')
        axarr[thisPos].plot(xsim_int[:,i], 'k:.', label='cvodes')
        axarr[thisPos].plot(xsim_rk4[:,i], 'k:o', label='rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    for i in range(Nx):
        thisPos = np.unravel_index(Nx+i, pltDim, order='F')
        axarr[thisPos].plot(np.fabs(xsim_int[:,i]-xsim_ltv[:,i]), 'k--', label='err ltv')
        axarr[thisPos].plot(np.fabs(xsim_int[:,i]-xsim_rk4[:,i]), 'k:o', label='err rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    f, axarr = plt.subplots(*(Nu, 1))

    for i in range(Nu):
        thisPos = (i)
        axarr[thisPos].plot(usim[:,i], 'k:.', label='$u[%d]$' % i)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

plt.show(block=False)
