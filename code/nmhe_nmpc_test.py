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

doSimPlots = False
doMHEPlots = False

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

simulator = tools.getCasadiIntegrator(f,Delta,[Nx,Nu],["x","u"],"int_f")


def _calc_lin_disc_wrapper_for_mp_map(item):
    """ Function wrapper for map or multiprocessing.map . """
    _xi, _ui, _wi, _Delta = item
    Ai = f_casadi.jacobian(0, 0)(_xi, _ui, _wi)[0].full()
    Bi = f_casadi.jacobian(1, 0)(_xi, _ui, _wi)[0].full()
    Gi = f_casadi.jacobian(2, 0)(_xi, _ui, _wi)[0].full()
    Ei = f_casadi(_xi, _ui, _wi).full().ravel() - Ai.dot(_xi).ravel() - Bi.dot(_ui).ravel() - Gi.dot(_wi).ravel()
    [Ai[:], Bi[:], Gi[:], Ei[:]] = util.c2d(Ai, Bi, _Delta, Gi, Ei)
    return Ai, Bi, Gi, Ei


# Initialize estimator.
Q_mhe = np.diag((sigma_w * np.ones((Nw,))) ** 2)
R_mhe = np.diag((sigma_v * np.ones((Nv,))) ** 2)
Qinv_mhe = scipy.linalg.inv(Q_mhe)
Rinv_mhe = scipy.linalg.inv(R_mhe)
P_mhe = np.diag((sigma_p * np.ones((Nx,))) ** 2)
x0bar = np.zeros((Nx,)) + 0.0*sigma_p*np.random.randn(Nx)

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
                   x0bar=x0bar, P0=linalg.inv(P_mhe), Delta=Delta,
                   ltv_guess=None, guess=None, returnSolver=True)

# Solve before iterating
for t in range(Nt):
    parVal_mhe["u",t] = u_0[t,:]
    parVal_mhe["y",t] = y_0[t,:]
parVal_mhe["y",Nt] = y_0[Nt,:]

parVal_mhe["Ad",:], parVal_mhe["Bd",:], parVal_mhe["Gd",:], parVal_mhe["fd",:] = \
    zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal_mhe['x',:-1],parVal_mhe['u',:],
                                                    varVal_mhe['w',:], [Delta for _k in xrange(Nt)])))

parVal_mhe["x0bar"] = x0bar
parVal_mhe["P0"] = linalg.inv(P_mhe)

res_mhe = estimator(x0=varVal_mhe, p=parVal_mhe, lbg=0, ubg=0, lbx=lbx_mhe, ubx=ubx_mhe)
sol_mhe = sol_mhe(res_mhe["x"])

# Initialize controller.

# Get Nt measurements before we start the main loop.

# Start main estimator-controller loop.

''' It seems that deque is faster. However, we should check it out again.
http://stackoverflow.com/questions/15969708/how-do-you-rotate-the-numbers-in-an-numpy-array-of-shape-n-or-n-1
https://scimusing.wordpress.com/2013/10/25/ring-buffers-in-pythonnumpy/
http://blog.explainmydata.com/2012/07/expensive-lessons-in-python-performance.html
http://comments.gmane.org/gmane.comp.python.numeric.general/54130
So, for now we create deque containers.
'''
_y = deque(y_0, maxlen=Nt+1)
_u = deque(u_0, maxlen=Nt)

xhat = deque()
xsim = deque()