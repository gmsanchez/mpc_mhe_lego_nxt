import casadi
import numpy as np
import scipy.linalg
import model_dcmotor as model
import tools
import util
import matplotlib.pyplot as plt

doSimPlots = False
doMHEPlots = False
fullInformation = False

f = model.F
h = model.H

Nx = model.Nx
Nu = model.Nu
Nw = model.Nw
Ny = model.Ny
Nv = model.Nv

Delta = 0.1
Nt = 10         # Horizon size
Nsim = 80

sigma_w = 0.5   # Standard deviation for the process noise
sigma_v = 0.25  # Standard deviation of the measurements
sigma_p = .5    # Standard deviation for prior

f_casadi = tools.getCasadiFunc(model.F, [Nx, Nu, Nw], ["x", "u", "w"], "f", rk4=False)
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

_x0 = np.zeros((Nx,))

wsim = 0.0*sigma_w*np.fabs(np.random.randn(Nsim, Nw))
vsim = 0.0*sigma_v*np.random.randn(Nsim, Nv)

usim = 20.0*np.ones((Nsim, Nu))
ysim = np.zeros((Nsim, Ny))

# xsim_rk4 = np.zeros((Nsim+1, Nx))
# xsim_rk4[0,:] = _x0
# xsim_int = np.zeros((Nsim+1, Nx))
# xsim_int[0,:] = _x0
xsim_ltv = np.zeros((Nsim+1, Nx))
xsim_ltv[0,:] = _x0

for t in range(Nsim):
    # Measure.
    # ysim[t] = model.H(xsim[t,:]) + vsim[t,:]
    # Simulate with CasADi integrator.
    # xsim_int[t+1,:] = f_casadi_int(xsim_int[t,:], usim[t,:], wsim[t,:]).full().ravel() #F_integrator(x0=xsim_int[t,:],p=np.hstack((usim[t,:],wsim[t,:])))['xf'].full().ravel()
    # xsim_rk4[t+1,:] = f_casadi_rk4(xsim_rk4[t,:], usim[t,:], wsim[t,:]).full().ravel()
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
        # axarr[thisPos].plot(xsim_int[:,i], 'k:.', label='cvodes')
        # axarr[thisPos].plot(xsim_rk4[:,i], 'k:o', label='rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    # for i in range(Nx):
    #     thisPos = np.unravel_index(Nx+i, pltDim, order='F')
    #     axarr[thisPos].plot(np.fabs(xsim_int[:,i]-xsim_ltv[:,i]), 'k--', label='err ltv')
    #     axarr[thisPos].plot(np.fabs(xsim_int[:,i]-xsim_rk4[:,i]), 'k:o', label='err rk4')
    #     axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
    #     axarr[thisPos].legend(loc="lower right", prop={'size': 8})
    #     axarr[thisPos].grid()

    f, axarr = plt.subplots(Nu, 1)

    if Nu==1:
        axarr.plot(usim[:, 0], 'k:.', label='$u[%d]$' % 0)
        axarr.legend(loc="lower right", prop={'size': 8})
        axarr.grid()
    else:
        for i in range(Nu):
            thisPos = (i)
            axarr[thisPos].plot(usim[:,i], 'k:.', label='$u[%d]$' % i)
            axarr[thisPos].legend(loc="lower right", prop={'size': 8})
            axarr[thisPos].grid()

    plt.show(block=False)

Q = np.eye(Nw)
R = np.eye(Nv)
Qinv = scipy.linalg.inv(Q)
Rinv = scipy.linalg.inv(R)


def lfunc(w, v):
    return util.mtimes(w.T, Qinv, w) + util.mtimes(v.T, Rinv, v)
l = tools.getCasadiFunc(lfunc, [Nw, Nv], ["w", "v"], "l")


def lxfunc(x, P):
    return util.mtimes(x.T, P, x)
lx = tools.getCasadiFunc(lxfunc, [Nx, (Nx, Nx)], ["x", "P"], "lx")


for t in range(Nsim):
    # Define sizes of everything.
    N = {"x":Nx, "y":Ny, "u":Nu}
    if fullInformation:
        N["t"] = t
        tmin = 0
    else:
        N["t"] = min(t,Nt)
        tmin = max(0,t - Nt)
    tmax = t+1
    print (tmin,tmax)
    tools.nmhe_ltv(f_casadi, h_casadi, usim[tmin:tmax-1,:], ysim[tmin:tmax,:], l, N)
    raw_input("Ciclo for...")