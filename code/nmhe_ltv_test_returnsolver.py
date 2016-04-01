import casadi
import casadi.tools as ctools
import numpy as np
import scipy.linalg
# import model_dcmotor as model
import model_lego as model
import tools
import util
import matplotlib.pyplot as plt
from scipy import linalg
import time

doSimPlots = False
doMHEPlots = True
fullInformation = False

f = model.f
h = model.h

Nx = model.Nx
Nu = model.Nu
Nw = model.Nw
Ny = model.Ny
Nv = model.Nv

Delta = 0.1
Nt = 10         # Horizon size
Nsim = 80

sigma_w = 0.0001   # Standard deviation for the process noise
sigma_v = np.deg2rad(0.5)  # Standard deviation of the measurements
sigma_p = 0.5    # Standard deviation for prior

f_casadi = tools.getCasadiFunc(f, [Nx, Nu, Nw], ["x", "u", "w"], "f", rk4=False)
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

x0 = np.zeros((Nx,))

wsim = 0.0*sigma_w*np.fabs(np.random.randn(Nsim, Nw))
vsim = 0.0*sigma_v*(np.random.rand(Nsim, Nv)-0.5)

usim = [80.0, 40.0]*np.ones((Nsim, Nu))
usim[0:Nt,0] = 0.0
usim[0:Nt,1] = 0.0
usim[Nt+0:Nt+25,0] = np.linspace(0,80,25)
usim[Nt+0:Nt+25,1] = np.linspace(0,40,25)
ysim = np.zeros((Nsim, Ny))

xsim_ltv = np.zeros((Nsim+1, Nx))
xsim_ltv[0,:] = x0

for t in range(Nsim):
    # Measure.
    # ysim[t] = h(xsim_ltv[t,:]) + vsim[t,:]
    ysim[t] = np.deg2rad( np.around( np.rad2deg( h(xsim_ltv[t,:]) + vsim[t,:]), decimals=0))
    # Simulate with CasADi integrator.
    # xsim_int[t+1,:] = f_casadi_int(xsim_int[t,:], usim[t,:], wsim[t,:]).full().ravel() #F_integrator(x0=xsim_int[t,:],p=np.hstack((usim[t,:],wsim[t,:])))['xf'].full().ravel()
    # xsim_rk4[t+1,:] = f_casadi_rk4(xsim_rk4[t,:], usim[t,:], wsim[t,:]).full().ravel()
    # Simulate with LTV model.
    Ad, Bd, Gd, fd = _calc_lin_disc_wrapper_for_mp_map((xsim_ltv[t,:], usim[t,:], wsim[t,:], Delta))
    xsim_ltv[t+1,:] = Ad.dot(xsim_ltv[t,:]) + Bd.dot(usim[t,:]) + Gd.dot(wsim[t,:]) + fd

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

Q = np.diag((sigma_w*np.ones((Nw,)))**2)
R = np.diag((sigma_v*np.ones((Nv,)))**2)
# Q = np.diag([0.001, 0.001, np.deg2rad(0.5), 1.0, 0.01, 0.01, 1.0, 0.01, 0.01])
Qinv = scipy.linalg.inv(Q)
Rinv = scipy.linalg.inv(R)
P = np.diag((sigma_p*np.ones((Nx,)))**2)
x_0 = x0 + 0.0*sigma_p*np.random.randn(Nx)

def lfunc(w, v):
    return util.mtimes(w.T, Qinv, w) + util.mtimes(v.T, Rinv, v)
l = tools.getCasadiFunc(lfunc, [Nw, Nv], ["w", "v"], "l")


def lxfunc(x, P):
    return util.mtimes(x.T, P, x)
lx = tools.getCasadiFunc(lxfunc, [Nx, (Nx, Nx)], ["x", "P"], "lx")

N = {"x":Nx, "y":Ny, "u":Nu, "t":Nt}

estimator, sol, varVal, parVal, lbx, ubx = tools.nmhe_ltv(f_casadi, h_casadi, usim[0:Nt, :], ysim[0:Nt+1, :],
                                                          l, N, lx=lx, x0bar=x_0, P0=linalg.inv(P), Delta=Delta,
                                                          ltv_guess=None, guess=None, returnSolver=True)

# Solve before iterating
for t in range(Nt):
    parVal["u",t] = usim[t,:]
    parVal["y",t] = ysim[t,:]
parVal["y",Nt] = ysim[Nt,:]

parVal["Ad",:], parVal["Bd",:], parVal["Gd",:], parVal["fd",:] = \
    zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal['x',:-1],parVal['u',:], varVal['w',:], [Delta for _k in xrange(Nt)])))
parVal["x0bar"] = x_0
parVal["P0"] = linalg.inv(P)

res = estimator(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lbx, ubx=ubx)
sol = sol(res["x"])

xhat_ltv = np.zeros((Nsim,Nx))
xhat_ltv[0,:] = x_0

for k in range(len(sol["x"])):
    xhat_ltv[k,:] = sol["x",k].full().ravel()

x_0 = sol['x',1]

for t in range(Nt+1,Nsim):
    # Define sizes of everything.
    N = {"x":Nx, "y":Ny, "u":Nu}
    if fullInformation:
        N["t"] = t
        tmin = 0
    else:
        N["t"] = min(t,Nt)
        tmin = max(0,t - Nt)
    tmax = t+1

    print (t, tmin, tmax)
    starttime = time.clock()

    parVal["u", 0:-1] = parVal["u", 1:]
    parVal["u", -1] = usim[t-1, :]
    parVal["y", 0:-1] = parVal["y", 1:]
    parVal["y", -1] = ysim[t,:]
    parVal["x0bar"] = x_0

    for k in varVal.keys():
        varVal[k, :] = sol[k, :]

    parVal["Ad", :], parVal["Bd", :], parVal["Gd", :], parVal["fd", :] = \
        zip(*map(_calc_lin_disc_wrapper_for_mp_map,
                 zip(varVal['x', :-1], parVal['u', :], varVal['w', :], [Delta for _k in xrange(Nt)])))

    res = estimator(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lbx, ubx=ubx)
    sol = sol(res["x"])

    # Now get the state estimate. Note that we are only interested in the last node of the horizon

    xhat_ltv[t,:] = sol["x", -1].full().ravel()
    x_0 = sol["x", 1]

    print "%3d (%10.5g s): %s" % (t, time.clock() - starttime, estimator.stats()['return_status'])


pltDim=(Nx,2)
fontsize=12
if doMHEPlots:
    f, axarr = plt.subplots(*pltDim)

    for i in range(Nx):
        thisPos = np.unravel_index(i, pltDim, order='F')
        axarr[thisPos].plot(xsim_ltv[:-1,i], 'k--', label='ltv')
        axarr[thisPos].plot(xhat_ltv[:,i], 'k:.', label='mhe')
        # axarr[thisPos].plot(xsim_rk4[:,i], 'k:o', label='rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    for i in range(Nx):
            thisPos = np.unravel_index(Nx+i, pltDim, order='F')
            axarr[thisPos].plot((xhat_ltv[:,i]-xsim_ltv[:-1,i]), 'k--', label='err mhe')
            # axarr[thisPos].plot((xsim_int[:,i]-xsim_rk4[:,i]), 'k:o', label='err rk4')
            axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
            axarr[thisPos].legend(loc="lower right", prop={'size': 8})
            axarr[thisPos].grid()

    plt.suptitle("NMHE LTV")
