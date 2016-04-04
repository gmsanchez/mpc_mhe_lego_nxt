import numpy as np
import scipy.linalg
# import model_dcmotor as model
import model_lego as model
import tools
import util
import matplotlib.pyplot as plt
from scipy import linalg
import time
from collections import deque
import multiprocessing as mp

doSimPlots = False
doMHEPlots = False

f = model.f
h = model.h

Nx = model.Nx
Nu = model.Nu
Nw = model.Nw
Ny = model.Ny
Nv = model.Nv
Np = model.Np

Delta = 0.1
Nt = 10         # Horizon size
Nsim = 100

Vb = 8.0
sigma_w = 0.0001   # Standard deviation for the process noise
sigma_v = np.deg2rad(0.5)  # Standard deviation of the measurements
sigma_p = 0.5    # Standard deviation for prior

f_casadi = tools.getCasadiFunc(f, [Nx, Nu, Nw, Np], ["x", "u", "w", "Vb"], "f", rk4=False)
h_casadi = tools.getCasadiFunc(h, [Nx], ["x"], "H")

simulator = tools.getCasadiIntegrator(f,Delta,[Nx,Nu,Nw,Np],["x","u","w","Vb"],"int_f")


def _calc_lin_disc_wrapper_for_mp_map(item):
    """ Function wrapper for map or multiprocessing.map . """
    _xi, _ui, _wi, _Vbi, _Delta = item
    Ai = f_casadi.jacobian(0, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Bi = f_casadi.jacobian(1, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Gi = f_casadi.jacobian(2, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Ei = f_casadi(_xi, _ui, _wi, _Vbi).full().ravel() - Ai.dot(_xi).ravel() - Bi.dot(_ui).ravel() - Gi.dot(_wi).ravel()
    [Ai[:], Bi[:], Gi[:], Ei[:]] = util.c2d(Ai, Bi, _Delta, Gi, Ei)
    return Ai, Bi, Gi, Ei


# Initialize estimator.
Q_mhe = np.diag((sigma_w * np.ones((Nw,))) ** 2)
R_mhe = np.diag((sigma_v * np.ones((Nv,))) ** 2)
Qinv_mhe = scipy.linalg.inv(Q_mhe)
Rinv_mhe = scipy.linalg.inv(R_mhe)
P_mhe = np.diag((sigma_p * np.ones((Nx,))) ** 2)
x0_mhe = np.zeros((Nx,)) + 0.0 * sigma_p * np.random.randn(Nx)

def lfunc_mhe(w, v):
    return util.mtimes(w.T, Qinv_mhe, w) + util.mtimes(v.T, Rinv_mhe, v)
l_mhe = tools.getCasadiFunc(lfunc_mhe, [Nw, Nv], ["w", "v"], "l")


def lxfunc_mhe(x, P):
    return util.mtimes(x.T, P, x)
lx_mhe = tools.getCasadiFunc(lxfunc_mhe, [Nx, (Nx, Nx)], ["x", "P"], "lx")

N_mhe = {"x":Nx, "y":Ny, "u":Nu, "t":Nt}

u_0 = np.zeros((Nt, Nu), order='F', dtype=np.float64)
y_0 = np.zeros((Nt+1, Ny), order='F', dtype=np.float64)

estimator, sol_mhe, varVal_mhe, parVal_mhe, lbx_mhe, ubx_mhe =\
    tools.nmhe_ltv(f_casadi, h_casadi, u_0, y_0, l_mhe, N_mhe, lx=lx_mhe,
                   x0bar=x0_mhe, P0=linalg.inv(P_mhe), Delta=Delta,
                   ltv_guess=None, guess=None, returnSolver=True)

# Solve before iterating
for t in range(Nt):
    parVal_mhe["u",t] = u_0[t,:]
    parVal_mhe["y",t] = y_0[t,:]
parVal_mhe["y",Nt] = y_0[Nt,:]

parVal_mhe["Ad",:], parVal_mhe["Bd",:], parVal_mhe["Gd",:], parVal_mhe["fd",:] = \
    zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal_mhe['x',:-1],parVal_mhe['u',:],
                                                    varVal_mhe['w',:], [Vb for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))

parVal_mhe["x0bar"] = x0_mhe
parVal_mhe["P0"] = linalg.inv(P_mhe)

res_mhe = estimator(x0=varVal_mhe, p=parVal_mhe, lbg=0, ubg=0, lbx=lbx_mhe, ubx=ubx_mhe)
sol_mhe = sol_mhe(res_mhe["x"])

# Initialize controller.
Q_mpc = np.diag([10, 10, 0, 0, 0, 0, 0, 0, 0])
R_mpc = 50e-6 * np.eye(Nu)
Qn_mpc = 0.1*Q_mpc


def lfunc_mpc(w, v):
    return util.mtimes(w.T, Q_mpc, w) + util.mtimes(v.T, R_mpc, v)
l_mpc = tools.getCasadiFunc(lfunc_mpc, [Nw, Nv], ["w", "v"], "l")


def lxfunc_mpc(x, P):
    return util.mtimes(x.T, P, x)
lx_mpc = tools.getCasadiFunc(lxfunc_mpc, [Nx, (Nx, Nx)], ["x", "P"], "lx")

lb_mpc = {'u': np.array([-100, -100]), 'Du': np.array([-20, -20])}
ub_mpc = {'u': np.array([100, 100]), 'Du': np.array([20, 20])}

xr = np.zeros((Nx,), dtype=np.float64)
xr[0] = 1.0
xr[1] = 1.0

ref = {'xr': np.tile(xr, (Nt, 1))}

uprev = np.zeros((Nu,))

x0_mpc = np.zeros((Nx,))
# x0_mpc[0] = -1.5
# x0_mpc[1] = 1.0

N_mpc = {"t": Nt, "x": Nx, "u": Nu}

# Solve one time go obtain the structure holders for variables and parameters
# sol,varVal,parVal = tools.nmpc_ltv(f_casadi, l, N, x0=_xk, lx=lx, Qn=Qn, lb=lb, ub=ub)
controller, sol_mpc, varVal_mpc, parVal_mpc, lb_mpc, ub_mpc =\
    tools.nmpc_ltv(f_casadi, l_mpc, N_mpc, x0=x0_mpc, lx=lx_mpc, Qn=Qn_mpc, lb=lb_mpc, ub=ub_mpc, uprev=uprev, ref=ref, returnSolver=True)
res_mpc = controller(x0=varVal_mpc, p=parVal_mpc, lbg=0, ubg=0, lbx=lb_mpc, ubx=ub_mpc)
sol_mpc = sol_mpc(res_mpc['x'])

for k in varVal_mpc.keys():
    varVal_mpc[k] = 0
for k in set(parVal_mpc.keys()).intersection(set(['x0', 'uprev', 'Qn', 'Ad', 'Bd', 'fd'])):
    parVal_mpc[k] = 0

# Get Nt measurements before we start the main loop.

# Start main estimator-controller loop.

''' It seems that deque is faster. However, we should check it out again.
http://stackoverflow.com/questions/15969708/how-do-you-rotate-the-numbers-in-an-numpy-array-of-shape-n-or-n-1
https://scimusing.wordpress.com/2013/10/25/ring-buffers-in-pythonnumpy/
http://blog.explainmydata.com/2012/07/expensive-lessons-in-python-performance.html
http://comments.gmane.org/gmane.comp.python.numeric.general/54130
http://www.rigtorp.se/2011/01/01/rolling-statistics-numpy.html
So, for now we create deque containers.
'''
_y = deque(y_0, maxlen=Nt+1)
_u = deque(u_0, maxlen=Nt)

xhat = deque()
xsim = deque()
usim = deque()

_xk = x0_mpc
_xk_mhe = _xk.copy()
_uk = uprev #np.zeros((Nu,))
x0_mhe = x0_mpc.copy()

# xsim.append(_xk)

# pool = mp.Pool()

for t in range(Nsim):
    starttime = time.time()
    # Get the measurement
    # _yk = h_casadi(_xk)
    _yk = np.deg2rad(np.around(np.rad2deg(h_casadi(_xk).full().ravel()), decimals=0))
    _y.append(_yk)

    # Estimate current state
    parVal_mhe["u", 0:-1] = parVal_mhe["u", 1:]
    parVal_mhe["u", -1] = _uk
    parVal_mhe["y", 0:-1] = parVal_mhe["y", 1:]
    parVal_mhe["y", -1] = _yk
    parVal_mhe["x0bar"] = x0_mhe

    for k in varVal_mhe.keys():
        varVal_mhe[k, :] = sol_mhe[k, :]

    parVal_mhe["Ad", :], parVal_mhe["Bd", :], parVal_mhe["Gd", :], parVal_mhe["fd", :] = \
        zip(*map(_calc_lin_disc_wrapper_for_mp_map,zip(varVal_mhe['x', :-1], parVal_mhe['u', :],
                                                       varVal_mhe['w', :], [Vb for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))

    res_mhe = estimator(x0=varVal_mhe, p=parVal_mhe, lbg=0, ubg=0, lbx=lbx_mhe, ubx=ubx_mhe)
    sol_mhe = sol_mhe(res_mhe["x"])

    # Now get the state estimate. Note that we are only interested in the last node of the horizon
    _xk_mhe = sol_mhe["x", -1].full().ravel()

    x0_mhe = sol_mhe["x", 1]

    # Obtain current inputs _uk

    parVal_mpc["x0"] = _xk_mhe
    parVal_mpc["uprev"] = _uk
    varVal_mpc["x",:-1] = sol_mpc["x",1:]
    varVal_mpc["x",-1] = sol_mpc["x",-1]
    varVal_mpc["u",:-1] = sol_mpc["u",1:]
    varVal_mpc["u",-1] = sol_mpc["u",-1]



    parVal_mpc["Ad",:], parVal_mpc["Bd",:], _, parVal_mpc["fd",:] = zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal_mpc['x',:-1],varVal_mpc['u'], [np.zeros((Nx,)) for _k in xrange(Nt)], [Vb for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))

    res_mpc = controller(x0=varVal_mpc, p=parVal_mpc, lbg=0, ubg=0, lbx=lb_mpc, ubx=ub_mpc)
    sol_mpc = sol_mpc(res_mpc['x'])

    _uk = np.around(sol_mpc["u"][0].full().ravel() , decimals=0)
    # _uk = sol["u"][0].full().ravel()
    # print _uk
    # _xk = sol_mpc["x"][0].full().ravel()
    # print _xk
    # raw_input()
    # print "%3d (%10.5g s): %s" % (t, time.time()-starttime, nlp_solver.stats()["return_status"])
    print "%3d (%10.5g s)" % (t, time.time()-starttime)


    xhat.append(_xk_mhe)
    xsim.append(_xk)
    usim.append(_uk)

    _xk = simulator(_xk, _uk, np.zeros((Nw,)), Vb).full().ravel()

# pool.close()
# pool.join()

xsim_mpc = np.array(xsim)
usim_mpc = np.array(usim)
xhat_ltv = np.array(xhat)
xsim_ltv = np.array(xsim)

doMPCPlots = True
doMHEPlots = True
fontsize = 12
pltDim = (4,3)

if doMPCPlots:
    f, axarr = plt.subplots(*pltDim)

    for i in range(Nx):
        thisPos = np.unravel_index(i,pltDim,order='F')
        axarr[thisPos].plot(xsim_mpc[:,i], 'k--', label='I_NMPC')
        #axarr[thisPos].plot(xsim_int[:,i], 'k:', label='cvodes')
        axarr[thisPos].set_ylabel('$x[%d]$'% i, fontsize=fontsize)
        # axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

        pltScale = 0.1
        (minlim,maxlim) = axarr[thisPos].get_xlim()
        offset = .5*pltScale*(maxlim - minlim)
        axarr[thisPos].set_xlim(minlim - offset, maxlim + offset)
        (minlim,maxlim) = axarr[thisPos].get_ylim()
        offset = .5*pltScale*(maxlim - minlim)
        axarr[thisPos].set_ylim(minlim - offset, maxlim + offset)

    for i in range(Nx,Nx+Nu):
        thisPos = np.unravel_index(i,pltDim,order='F')
        axarr[thisPos].step(np.arange(usim_mpc.shape[0]), usim_mpc[:,i-Nx], '.k', where='post')
        axarr[thisPos].set_ylabel('$u[%d]$'% (i-Nx))
        axarr[thisPos].grid()

        pltScale = 0.1
        (minlim,maxlim) = axarr[thisPos].get_xlim()
        offset = .5*pltScale*(maxlim - minlim)
        axarr[thisPos].set_xlim(minlim - offset, maxlim + offset)
        (minlim,maxlim) = axarr[thisPos].get_ylim()
        offset = .5*pltScale*(maxlim - minlim)
        axarr[thisPos].set_ylim(minlim - offset, maxlim + offset)

    thisPos = np.unravel_index(Nx+Nu,pltDim,order='F')
    axarr[thisPos].plot(xsim_mpc[:,0],xsim_mpc[:,1], 'ko-', label='I_NMPC')
    #axarr[thisPos].plot(xsim_int[:,0],xsim_int[:,1], 'k:', label='cvodes')
    #axarr[thisPos].legend(loc="upper left", prop={'size': 8})

    axarr[thisPos].set_xlabel('$x[0]=x$')
    axarr[thisPos].set_ylabel('$x[1]=y$')
    axarr[thisPos].grid()

    pltScale = 0.1
    (minlim,maxlim) = axarr[thisPos].get_xlim()
    offset = .5*pltScale*(maxlim - minlim)
    axarr[thisPos].set_xlim(minlim - offset, maxlim + offset)
    (minlim,maxlim) = axarr[thisPos].get_ylim()
    offset = .5*pltScale*(maxlim - minlim)
    axarr[thisPos].set_ylim(minlim - offset, maxlim + offset)
    plt.suptitle("NMPC LTV")
    
pltDim=(Nx,2)
fontsize=12
if doMHEPlots:
    f, axarr = plt.subplots(*pltDim)

    for i in range(Nx):
        thisPos = np.unravel_index(i, pltDim, order='F')
        axarr[thisPos].plot(xsim_ltv[:,i], 'k--', label='ltv')
        axarr[thisPos].plot(xhat_ltv[:,i], 'k:.', label='mhe')
        # axarr[thisPos].plot(xsim_rk4[:,i], 'k:o', label='rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    for i in range(Nx):
            thisPos = np.unravel_index(Nx+i, pltDim, order='F')
            axarr[thisPos].plot((xhat_ltv[:,i]-xsim_ltv[:,i]), 'k--', label='err mhe')
            # axarr[thisPos].plot((xsim_int[:,i]-xsim_rk4[:,i]), 'k:o', label='err rk4')
            axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
            axarr[thisPos].legend(loc="lower right", prop={'size': 8})
            axarr[thisPos].grid()

    plt.suptitle("NMHE LTV")
