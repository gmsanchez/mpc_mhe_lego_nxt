# We show two different ways to create a CasADi function.
# Using plain CasADi and using Rawlings' mpc-toolbox-casadi function helper.

import sys
from os.path import expanduser
home = expanduser("~")
code_dir = home+"/fun/thesis/code/"
if code_dir not in sys.path:
    sys.path.extend([code_dir])

import casadi
import model_lego as model
import tools

# 1- Using plain CasADi
Nx = model.Nx
Nu = model.Nu

# Create necessary CasADi symbols
x = casadi.SX.sym("x", Nx)
u = casadi.SX.sym("u", Nu)

# Create the CasADi function
F_casadi_0 = casadi.Function("F", [x, u], [casadi.vertcat(model.F(x, u))])

# 2- Rawlings' mpc-toolbox-casadi function helper
F_casadi_1 = tools.getCasadiFunc(model.F, [Nx, Nu], ["x", "u"], "F", rk4=False)

if F_casadi_0.numel_out() == F_casadi_1.numel_out():
    for i in range(F_casadi_0.numel_out()):
        print "Output x[%d]" % i
        print "F_casadi_0: ", F_casadi_0(x, u)[i]
        print "F_casadi_1: ", F_casadi_1(x, u)[i]
