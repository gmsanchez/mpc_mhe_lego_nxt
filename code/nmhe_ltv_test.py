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
usim[0:25,0] = np.linspace(0,80,25)
usim[0:25,1] = np.linspace(0,40,25)
# usim[0:,0] =
ysim = np.zeros((Nsim, Ny))

# xsim_rk4 = np.zeros((Nsim+1, Nx))
# xsim_rk4[0,:] = _x0
# xsim_int = np.zeros((Nsim+1, Nx))
# xsim_int[0,:] = _x0
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


varStruct = ctools.struct_symSX([ctools.entry("x", repeat=Nt + 1, shape=(Nx, 1)),
                                 ctools.entry("w", repeat=Nt, shape=(Nw, 1)),
                                 ctools.entry("v", repeat=Nt + 1, shape=(Nv, 1))])
ltvStruct = ctools.struct_symSX([  # ctools.entry("y", repeat=N["t"] + 1, shape=(N["y"], 1)),
                                   # ctools.entry("u", repeat=N["t"], shape=(N["u"], 1)),
                                   # ctools.entry("x0bar", shape=(Nx, 1)),
                                   # ctools.entry("P0", shape=(Nx, Nx)),
                                 ctools.entry("Ad", repeat=Nt, shape=(Nx, Nx)),
                                 ctools.entry("Bd", repeat=Nt, shape=(Nx, Nu)),
                                 ctools.entry("Gd", repeat=Nt, shape=(Nx, Nw)),
                                 ctools.entry("fd", repeat=Nt, shape=(Nx, 1))])
ltv_guess = ltvStruct(0)
curr_sol = varStruct(0)
curr_sol["x",0] = x_0
xhat_ltv = np.zeros((Nsim,Nx))
xhat_ltv[0,:] = x_0

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

    print (tmin, tmax)
    starttime = time.clock()
    # print "ltv_len: ",len(range(N["t"]))
    ltv_guess = ltvStruct(0)

    for k in range(N["t"]):
        ltv_guess["Ad",k], ltv_guess["Bd",k], ltv_guess["Gd",k], ltv_guess["fd",k] =\
        _calc_lin_disc_wrapper_for_mp_map((curr_sol["x",k], usim[k+tmin, :], curr_sol["w",k], Delta))
            #_calc_lin_disc_wrapper_for_mp_map((xsim_ltv[k+tmin,:], usim[k+tmin, :], wsim[k+tmin,:], Delta))

    # for k in ltv_guess.keys():
    #     print k, ltv_guess[k]

    sol = tools.nmhe_ltv(f_casadi, h_casadi, usim[tmin:tmax-1,:], ysim[tmin:tmax,:], l, N,
                   lx=lx, x0bar=x_0, P0=linalg.inv(P), Delta=Delta, ltv_guess=ltv_guess, guess=None, returnSolver=False)

    xhat_ltv[t,:] = sol["x"][-1].full().ravel()

    curr_sol = varStruct(0)
    for k in sol.keys():
        for i in range(len(sol[k])):
            curr_sol[k,i] = sol[k,i]

    if not fullInformation and t + 1 > Nt:
        # for k in sol.keys():
            # curr_sol[k,0:-1] = sol[k,1:]
            # curr_sol[k,-1] = sol[k,-1]
        x_0 = curr_sol["x",1]
        # xhat_ltv.append(np.array(curr_sol["x", 0]).flatten())
    # else:
    #     curr_sol['x',0:tmax] = sol['x',0:tmax]

    # raw_input("Ciclo for...")
    print "%3d (%10.5g s)" % (t, time.clock() - starttime)
    # print "%3d (%10.5g s): %s" % (t, time.clock() - starttime, sol["status"])

# for i in xrange(1,len(curr_sol["x"])):
#    xhat_ltv.append(np.array(curr_sol["x",i]).flatten())

xhat_ltv = np.array(xhat_ltv)


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
