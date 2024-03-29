import model_lego_noparams as model
import tools
import util
import casadi.tools as ctools
import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.linalg

doPlots = True

f = model.f
h = model.h

Nx = model.Nx
Nu = model.Nu
Nw = model.Nw
Ny = model.Ny
Nv = model.Nv

Delta = 0.1
Nt = 5        # Horizon size
Nsim = 200

# sigma_w = 0.05   # Standard deviation for the process noise
# sigma_v = 0.25  # Standard deviation of the measurements
# sigma_p = 0.5    # Standard deviation for prior

f_casadi = tools.getCasadiFunc(f, [Nx, Nu, Nw], ["x", "u", "w"], "f", rk4=False)
h_casadi = tools.getCasadiFunc(h, [Nx], ["x"], "H")

f_casadi_int = tools.getCasadiIntegrator(f,Delta,[Nx,Nu],["x","u"],"int_f")

def _calc_lin_disc_wrapper_for_mp_map(item):
    """ Function wrapper for map or multiprocessing.map . """
    _xi, _ui, _wi, _Delta = item
    Ai = f_casadi.jacobian(0, 0)(_xi, _ui, _wi)[0].full()
    Bi = f_casadi.jacobian(1, 0)(_xi, _ui, _wi)[0].full()
    Gi = f_casadi.jacobian(2, 0)(_xi, _ui, _wi)[0].full()
    Ei = f_casadi(_xi, _ui, _wi).full().ravel() - Ai.dot(_xi).ravel() - Bi.dot(_ui).ravel() - Gi.dot(_wi).ravel()
    [Ai[:], Bi[:], Gi[:], Ei[:]] = util.c2d(Ai, Bi, _Delta, Gi, Ei)
    return Ai, Bi, Gi, Ei


# ltvStruct = ctools.struct_symSX([ctools.entry("Ad", repeat=Nt, shape=(Nx, Nx)),
#                                  ctools.entry("Bd", repeat=Nt, shape=(Nx, Nu)),
#                                  # ctools.entry("Gd", repeat=Nt, shape=(Nx, Nw)),
#                                  ctools.entry("fd", repeat=Nt, shape=(Nx, 1))])
# ltv_guess = ltvStruct(0)

Q = 1e0*np.diag([1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]) #100.0*np.eye(Nx)
R = 1e0*np.eye(Nu)
Qn = 1e0*Q


def lfunc(w, v):
    return util.mtimes(w.T, Q, w) + util.mtimes(v.T, R, v)
l = tools.getCasadiFunc(lfunc, [Nw, Nv], ["w", "v"], "l")


def lxfunc(x, P):
    return util.mtimes(x.T, P, x)
lx = tools.getCasadiFunc(lxfunc, [Nx, (Nx, Nx)], ["x", "P"], "lx")

lb = {'u': np.array([-100, -100]), 'Du': np.array([-50, -50])}
ub = {'u': np.array([100, 100]), 'Du': np.array([50, 50])}
# lb = {'u': np.array([-100, -100])}
# ub = {'u': np.array([100, 100])}


# xlb = np.array([-np.inf,-np.inf,-np.inf,-np.inf,-np.pi,-np.inf,-np.inf,-np.inf,-np.pi])
# xub = np.array([np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf])
#
# ulb = np.array([-100.0, -100.0])
# uub = np.array([100.0, 100.0])
#
# lb = {
#     "u": np.tile(ulb,(Nt,1)),
#     "x": np.tile(xlb,(Nt+1,1)),
# }
# ub = {
#     "u" : np.tile(uub,(Nt,1)),
#     "x" : np.tile(xub,(Nt+1,1)),
# }

xr = np.zeros((Nx,), dtype=np.float64)
xr[0] = 2.0
xr[1] = -2.0

ref = {'xr': np.tile(xr, (Nt, 1))}

x0 = np.zeros((Nx,))
u0 = np.zeros((Nu,))

N = {"t": Nt, "x": Nx, "u": Nu}

# Solve one time go obtain the structure holders for variables and parameters
# sol,varVal,parVal = tools.nmpc_ltv(f_casadi, l, N, x0=_xk, lx=lx, Qn=Qn, lb=lb, ub=ub)
# controller, sol, varVal, parVal, lb, ub = tools.nmpc_ltv(f_casadi, l, N, x0=x0, lx=lx, Qn=Qn, lb=lb, ub=ub, ref=ref, uprev=None, returnSolver=True)
controller, sol, varVal, parVal, lb, ub = tools.nmpc_ltv(f_casadi, l, N, x0=x0, lx=lx, Qn=Qn, lb=lb, ub=ub, ref=ref, uprev=u0, returnSolver=True)
sol0 = controller(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lb, ubx=ub)
sol = sol(sol0['x'])

# Simulate to generate the matrices for the LTV system
for k in varVal.keys():
    varVal[k] = 0
for k in set(parVal.keys()).intersection(set(['x0', 'Qn', 'Ad', 'Bd', 'fd'])):
    parVal[k] = 0

# varVal["x"] = x0

# for t in range(N["t"]-1):
#     parVal["Ad",t], parVal["Bd",t], _, parVal["fd",t] = \
#         _calc_lin_disc_wrapper_for_mp_map((varVal["x",t], varVal["u",t], np.zeros((Nx,)), Delta))
#     varVal["x",t+1] = util.mtimes(parVal["Ad",t],varVal["x",t]).ravel() + util.mtimes(parVal["Bd",t],varVal["u",t]).ravel() + parVal["fd",t].full().ravel()

_xk = x0
_uk = varVal["u",0].full().ravel()

xsim_mpc = np.zeros((Nsim+1, Nx))
xsim_mpc[0,:] = x0
usim_mpc = np.zeros((Nsim, Nu))

parVal["Qn"] = Qn

for t in range(Nsim):
    parVal["x0"] = _xk
    parVal["uprev"] = _uk
    varVal["x",:-1] = sol["x",1:]
    varVal["x",-1] = sol["x",-1]
    varVal["u",:-1] = sol["u",1:]
    varVal["u",-1] = sol["u",-1]
    # parVal["Qn"] = Q

    starttime = time.time()

    parVal["Ad",:], parVal["Bd",:], _, parVal["fd",:] = zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal['x',:-1],varVal['u'], [np.zeros((Nx,)) for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))

    # print parVal["Ad"]

    
    # sol,_,_ = tools.nmpc_ltv(f_casadi, l, N, x0=_xk, lx=lx, Qn=Qn, lb=lb, ub=ub, ltv_guess=parVal, guess=varVal)
    sol0 = controller(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lb, ubx=ub)
    sol = sol(sol0['x'])

    # _uk = np.around( sol["u"][0].full().ravel() , decimals=0)
    _uk = sol["u"][0].full().ravel()
    print _uk
    _xk = sol["x"][0].full().ravel()
    # print _xk
    # raw_input()
    # print "%3d (%10.5g s): %s" % (t, time.time()-starttime, nlp_solver.stats()["return_status"])
    print "%3d (%10.5g s)" % (t, time.time()-starttime)

    _xk = f_casadi_int(_xk, _uk).full().ravel()
    xsim_mpc[t+1,:] = _xk
    usim_mpc[t,:] = _uk
    
    Qn = scipy.linalg.solve_discrete_lyapunov(parVal["Ad",0],Q,method='bilinear')
    
    # Ac_k = parVal["Ad",0]
    # Ac_k = f_casadi.jacobian(0, 0)(_xk, _uk, np.zeros((Nx,)))[0].full()
    # Qn = scipy.linalg.solve_lyapunov(Ac_k,Q)
    
    parVal["Qn"] = Qn

fontsize = 12
pltDim = (4,3)

if doPlots:
    f, axarr = plt.subplots(*pltDim) #, sharex=True)
    #f.tight_layout()

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
