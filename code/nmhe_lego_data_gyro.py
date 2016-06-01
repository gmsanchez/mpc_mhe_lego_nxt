import casadi
import casadi.tools as ctools
import numpy as np
import scipy.linalg
# import model_dcmotor as model
import model_lego_powgain_gyro as model
import tools
import util
import matplotlib.pyplot as plt
from scipy import linalg
import time
from collections import deque
from nxt_lib.nxt_list import data_idx

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
Np = model.Np

motor_load = "/home/guiss/fun/thesis/code/datalogs/datalog_20150210_153746.csv"
_log_data = np.loadtxt(open(motor_load,"rb"), delimiter=",", skiprows=1, dtype=np.float64)
# _log_data = _log_data[0:300,:]

Delta = np.int(_log_data[1,data_idx['t']] - _log_data[0,data_idx['t']])*(1E-3)
NumSamples = _log_data.shape[0]
tplot = np.arange(NumSamples)*Delta
# Delta = 0.1
Nt = 5         # Horizon size
Nsim = _log_data.shape[0]

sigma_w = 0.01   # Standard deviation for the process noise
sigma_v = 0.00001 #np.deg2rad(0.5)  # Standard deviation of the measurements
sigma_p = 0.5    # Standard deviation for prior

f_casadi = tools.getCasadiFunc(f, [Nx, Nu, Nw, Np], ["x", "u", "w", "Vb"], "f", rk4=False)
h_casadi = tools.getCasadiFunc(h, [Nx], ["x"], "H")


def _calc_lin_disc_wrapper_for_mp_map(item):
    """ Function wrapper for map or multiprocessing.map . """
    _xi, _ui, _wi, _Vbi, _Delta = item
    Ai = f_casadi.jacobian(0, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Bi = f_casadi.jacobian(1, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Gi = f_casadi.jacobian(2, 0)(_xi, _ui, _wi, _Vbi)[0].full()
    Ei = f_casadi(_xi, _ui, _wi, _Vbi).full().ravel() - Ai.dot(_xi).ravel() - Bi.dot(_ui).ravel() - Gi.dot(_wi).ravel()
    [Ai[:], Bi[:], Gi[:], Ei[:]] = util.c2d(Ai, Bi, _Delta, Gi, Ei)
    return Ai, Bi, Gi, Ei

x0 = np.zeros((Nx,))

wsim = 0.0*sigma_w*np.fabs(np.random.randn(Nsim, Nw))
vsim = 0.0*sigma_v*(np.random.rand(Nsim, Nv)-0.5)

usim = np.zeros((Nsim, Nu))
usim[:, 0] = _log_data[:, data_idx['ul']]
usim[:, 1] = _log_data[:, data_idx['ur']]
ysim = np.zeros((Nsim, Ny))
ysim[:, 0] = _log_data[:, data_idx['mot_l']]
ysim[:, 1] = _log_data[:, data_idx['mot_r']]
ysim[:, 2] = _log_data[:, data_idx['gyro']]

_Vbk = _log_data[0, data_idx['battery']]/1000.0

u_0 = np.zeros((Nt, Nu), order='F', dtype=np.float64)
y_0 = np.zeros((Nt+1, Ny), order='F', dtype=np.float64)

xsim_ltv = np.zeros((Nsim+1, Nx))
xsim_ltv[0,:] = x0

# Q = np.diag((sigma_w*np.ones((Nw,)))**2)
# Q = np.diag([1.0E6, 1.0E6, 0.5, 1E-3, 1E-6, 0.10, 1E-3, 1E-6, 0.10])
Q = np.diag(np.ones((Nx,)))*1E0
#Q[4,4] = 1E2
#Q[7,7] = 1E2
#Q[3,3] = 1E2
#Q[6,6] = 1E2
# R = np.diag((sigma_v*np.ones((Nv,)))**2)
# Q = np.diag([0.001, 0.001, np.deg2rad(0.5), 1.0, 0.01, 0.01, 1.0, 0.01, 0.01])
#R = np.diag(np.ones((Ny,)))*1E-3
R = np.diag([1E-1, 1E-1, 1E0])
Qinv = scipy.linalg.inv(Q)
Rinv = scipy.linalg.inv(R)
P = np.diag((sigma_p*np.ones((Nx,)))**2)
x_0 = x0 + 0.0*sigma_p*np.random.randn(Nx)

x_0[10] = 1.089
x_0[9] = 1.089
x_0[11] = 0.95

#lb = {"x" : np.array([-np.inf, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf,
#                      -np.inf, -np.inf, -np.inf, 0.0, 0.0, 9.5])}

#ub = {"x" : np.array([np.inf, np.inf, np.inf, np.inf, np.inf, np.inf,
#                      np.inf, np.inf, np.inf, 2.0, 2.0, 11.0])}
                      
def lfunc(w, v):
    return util.mtimes(w.T, Qinv, w) + util.mtimes(v.T, Rinv, v)
l = tools.getCasadiFunc(lfunc, [Nw, Nv], ["w", "v"], "l")


def lxfunc(x, P):
    return util.mtimes(x.T, P, x)
lx = tools.getCasadiFunc(lxfunc, [Nx, (Nx, Nx)], ["x", "P"], "lx")

N = {"x":Nx, "y":Ny, "u":Nu, "t":Nt}

estimator, sol, varVal, parVal, lbx, ubx = tools.nmhe_ltv(f_casadi, h_casadi, u_0, y_0,
                                                          l, N, lx=lx, x0bar=x_0, P0=linalg.inv(P), Delta=Delta,
                                                          ltv_guess=None, guess=None, returnSolver=True)

# Solve before iterating
for k in varVal.keys():
    varVal[k] = 0

for t in range(Nt):
    parVal["u",t] = u_0[t,:]
    parVal["y",t] = y_0[t,:]
parVal["y",Nt] = y_0[Nt,:]

parVal["Ad",:], parVal["Bd",:], parVal["Gd",:], parVal["fd",:] = \
    zip(*map(_calc_lin_disc_wrapper_for_mp_map, zip(varVal['x',:-1],parVal['u',:], varVal['w',:], [_Vbk for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))
parVal["x0bar"] = x_0
parVal["P0"] = linalg.inv(P)

res = estimator(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lbx, ubx=ubx)
# sol = sol(res["x"])
sol = sol(0)
for t in range(len(sol["x"])):
    sol["x",t] = x_0

_y = deque(y_0, maxlen=Nt+1)
_u = deque(u_0, maxlen=Nt)

xhat = deque()


# xhat.append(x_0)

# for k in range(len(sol["x"])):
#     xhat_ltv[k,:] = sol["x",k].full().ravel()

# x_0 = sol['x',1]
# Define sizes of everything.
_yk = np.zeros((Ny,))
_uk = np.zeros((Nu,))

for t in range(Nsim):
    starttime = time.clock()
    _yk = np.deg2rad( ysim[t,:])
    _y.append(_yk)
    _uk = usim[t,:]
    _u.append(_uk)
    _Vbk = _log_data[t, data_idx['battery']]/1000.0

    parVal["u", 0:-1] = parVal["u", 1:]
    parVal["u", -1] = _uk
    parVal["y", 0:-1] = parVal["y", 1:]
    parVal["y", -1] = _yk
    parVal["x0bar"] = x_0

    for k in varVal.keys():
        varVal[k, 0:-1] = sol[k, 1:]
        varVal[k, -1] = sol[k, -1]

    parVal["Ad", :], parVal["Bd", :], parVal["Gd", :], parVal["fd", :] = \
        zip(*map(_calc_lin_disc_wrapper_for_mp_map,
                 zip(varVal['x', :-1], parVal['u', :], varVal['w', :], [_Vbk for _k in xrange(Nt)], [Delta for _k in xrange(Nt)])))

    res = estimator(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lbx, ubx=ubx)
    sol = sol(res["x"])

    # Now get the state estimate. Note that we are only interested in the last node of the horizon

    xhat.append(sol["x", -1].full().ravel())
    x_0 = sol["x", 1]

    print "%3d (%10.5g s): %s" % (t, time.clock() - starttime, estimator.stats()['return_status'])


xhat_ltv = np.array(xhat)
pltDim=(Nx,2)
fontsize=12
if doMHEPlots:
    f, axarr = plt.subplots(*pltDim)

    for i in range(Nx):
        thisPos = np.unravel_index(i, pltDim, order='F')
        # axarr[thisPos].plot(xsim_ltv[:-1,i], 'k--', label='ltv')
        axarr[thisPos].plot(xhat_ltv[:,i], 'k:.', label='mhe')
        # axarr[thisPos].plot(xsim_rk4[:,i], 'k:o', label='rk4')
        axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
        axarr[thisPos].legend(loc="lower right", prop={'size': 8})
        axarr[thisPos].grid()

    # for i in range(Nx):
    #         thisPos = np.unravel_index(Nx+i, pltDim, order='F')
    #         axarr[thisPos].plot((xhat_ltv[:,i]-xsim_ltv[:-1,i]), 'k--', label='err mhe')
            # axarr[thisPos].plot((xsim_int[:,i]-xsim_rk4[:,i]), 'k:o', label='err rk4')
            # axarr[thisPos].set_ylabel('$x[%d]$' % i, fontsize=fontsize)
            # axarr[thisPos].legend(loc="lower right", prop={'size': 8})
            # axarr[thisPos].grid()

    plt.suptitle("NMHE LTV")
    
fontsize_legend=16
fontsize_axislabel=18

plt.figure()
plt.plot(tplot,xhat_ltv[:,3], label=r"$MHE$", marker='+', markevery=5)
plt.plot(tplot,np.deg2rad(ysim[:,0]), marker='', markevery=5, label=r"$Medici\acute{o}n$")
plt.legend(fontsize=fontsize_legend)
plt.ylabel(r'$\theta_l \; \mathrm{[rad]}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$t \; \mathrm{[seg]}$', fontsize=fontsize_axislabel)
#plt.title(r'$\theta_l$')
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_theta_l_n_%d.pdf' % (Nt),format='PDF')

plt.figure()
plt.plot(tplot,xhat_ltv[:,6], label=r"$MHE$", marker='+', markevery=5)
plt.plot(tplot,np.deg2rad(ysim[:,1]), label=r"$Medici\acute{o}n$")
plt.legend(fontsize=fontsize_legend)
plt.ylabel(r'$\theta_r \; \mathrm{[rad]}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$t \; \mathrm{[seg]}$', fontsize=fontsize_axislabel)
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_theta_r_n_%d.pdf' % (Nt),format='PDF')

plt.figure()
plt.plot(tplot[1:],xhat_ltv[1:,4], label=r"$MHE$", marker='+', markevery=5)
plt.plot(tplot[1:],np.diff(np.deg2rad(ysim[:,0]))/Delta, label=r"$\Delta \theta_l / \Delta t$")
plt.legend(fontsize=fontsize_legend)
plt.ylabel(r'$\omega_l \; \mathrm{[rad/s]}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$t \; \mathrm{[seg]}$', fontsize=fontsize_axislabel)
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_omega_l_n_%d.pdf' % (Nt),format='PDF')

plt.figure()
plt.plot(tplot[1:],xhat_ltv[1:,7], label=r"$MHE$", marker='+', markevery=5)
plt.plot(tplot[1:],np.diff(np.deg2rad(ysim[:,1]))/Delta, label=r"$\Delta \theta_r / \Delta t$")
plt.legend(fontsize=fontsize_legend)
plt.ylabel(r'$\omega_r \; \mathrm{[rad/s]}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$t \; \mathrm{[seg]}$', fontsize=fontsize_axislabel)
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_omega_r_n_%d.pdf' % (Nt),format='PDF')

plt.figure()
plt.plot(tplot,usim[:,0], marker='+', markevery=5, label=r"$u_l$")
plt.plot(tplot,usim[:,1], label=r"$u_r$")
plt.legend(fontsize=fontsize_legend)
plt.ylabel(r'$u_{l,r}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$t \; \mathrm{[seg]}$', fontsize=fontsize_axislabel)
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_u_lr_n_%d.pdf' % (Nt),format='PDF')

plt.figure()
plt.plot(xhat_ltv[:,0], xhat_ltv[:,1], marker='o', markevery=5)
#plt.title("x vs y")
plt.ylabel(r'$y \; \mathrm{[m]}$', fontsize=fontsize_axislabel)
plt.xlabel(r'$x \; \mathrm{[m]}$', fontsize=fontsize_axislabel)
# plt.gca().invert_yaxis()
pltScale = 0.1
x1,x2,y1,y2 = plt.axis()
offset_x = .5*pltScale*(x2 - x1)
offset_y = .5*pltScale*(y2 - y1)
plt.axis([x1-offset_x, x2+offset_x, y1-offset_y, y2+offset_y])
plt.tight_layout()
plt.grid()
plt.savefig('mhe_gyro_xy_n_%d.pdf' % (Nt),format='PDF')
