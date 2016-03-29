import casadi
import casadi.tools as ctools
import numpy as np
import util


def nmhe(f, h, u, y, l, N, lx=None, x0bar=None, lb={}, ub={}, guess={}, g=None,
         p=None, verbosity=5, largs=None, funcargs={}, timelimit=60, Delta=None,
         wAdditive=False, casaditype="SX"):
    pass


def nmhe_ltv(f, h, u, y, l, N, lx=None, x0bar=None, P0=None, Delta=None, ltv_guess=None, guess=None, returnSolver=False):

    N = N.copy()
    # Check specified sizes.
    try:
        for i in ["x", "y"]:
            if N[i] <= 0:
                N[i] = 1
            if N["t"] < 0:
                N["t"] = 0
        if "w" not in N:
            N["w"] = N["x"]
        N["v"] = N["y"]
    except KeyError:
        raise KeyError("Invalid or missing entries in N dictionary!")

    # Structure that will be degrees of freedom for the optimizer
    varStruct = ctools.struct_symSX([ctools.entry("x", repeat=N["t"]+1, shape=(N["x"], 1)),
                                     ctools.entry("w", repeat=N["t"], shape=(N["w"], 1)),
                                     ctools.entry("v", repeat=N["t"]+1, shape=(N["v"], 1))])

    # Structure that will be fixed parameters for the optimizer
    parStruct = ctools.struct_symSX([ctools.entry("y", repeat=N["t"]+1, shape=(N["y"], 1)),
                                     ctools.entry("u", repeat=N["t"], shape=(N["u"], 1)),
                                     ctools.entry("x0bar", shape=(N["x"], 1)),
                                     ctools.entry("P0", shape=(N["x"], N["x"])),
                                     ctools.entry("Ad", repeat=N["t"], shape=(N["x"], N["x"])),
                                     ctools.entry("Bd", repeat=N["t"], shape=(N["x"], N["u"])),
                                     ctools.entry("Gd", repeat=N["t"], shape=(N["x"], N["w"])),
                                     ctools.entry("fd", repeat=N["t"], shape=(N["x"], 1))])

    # Build the objective
    obj = 0
    # First, the arrival cost
    obj += lx((varStruct["x", 0] - parStruct["x0bar"]), parStruct["P0"])
    for i in range(N["t"]):
        obj += l(varStruct["w", i], varStruct["v", i])
    # Final term of stage costs.
    obj += l(np.zeros((N["w"],)), varStruct["v", -1])  # Or should we use N["t"]+1 as index?

    # Build the constraints
    # State evolution f.
    state_constraints = []
    for t in range(N["t"]):
        state_constraints.append(varStruct["x", t+1] -
                                 casadi.mtimes(parStruct["Ad", t], varStruct["x", t]) -
                                 casadi.mtimes(parStruct["Bd", t], parStruct["u", t]) -
                                 casadi.mtimes(parStruct["Gd", t], varStruct["w", t]) -
                                 parStruct["fd", t])
    # for idx, thiscon in enumerate(state_constraints):
    #     print (idx, thiscon)
    #     raw_input()

    # Measurement h.
    measurement_constraints = []
    for t in range(N["t"]+1):
        measurement_constraints.append(parStruct["y", t] - h(varStruct["x", t]) - varStruct["v", t])
    # for idx, thiscon in enumerate(measurement_constraints):
    #     print (idx, thiscon)
    #     raw_input()

    # Build up constraints.
    con = state_constraints + measurement_constraints
    con = casadi.vertcat(*con)

    varVal = varStruct(0)
    parVal = parStruct(0)

    if guess is not None:
        for k in set(guess.keys()).intersection(varVal.keys()):
            for i in range(len(varVal[k])):
                varVal[k,i] = guess[k,i]

    parVal["P0"] = P0
    parVal["x0bar"] = x0bar

    if ltv_guess is not None:
        for k in ltv_guess.keys():
            for t in range(len(parVal[k])):
                parVal[k,t] = ltv_guess[k,t]
            # print k, parVal[k]

    for t in range(len(parVal["u"])):
        parVal["u",t] = u[t,:]

    for t in range(len(parVal["y"])):
        parVal["y", t] = y[t, :]

    # parDict = {'u': u, 'y': y}
    # for k in parDict.keys(): #("y","u"):
    #     for t in range(len(parVal[k])):
    #         parVal[k,t] = parDict[k][t, :]

    # Formulate the NLP
    nlp = {'x': varStruct, 'p': parStruct, 'f': obj, 'g': con}
    opts = {"ipopt.print_level": 0, "print_time": False, 'ipopt.max_iter': 100}
    nlp_solver = casadi.nlpsol("nlpsol", "ipopt", nlp, opts)
    if returnSolver:
        return nlp_solver
    else:
        sol = nlp_solver(x0=varVal, p=parVal, lbg=0, ubg=0)
        return varStruct(sol["x"])


def nmhe_rk4(f, h, u, y, l, N, lx=None, x0bar=None, P0=None, guess=None, returnSolver=False):

    N = N.copy()
    # Check specified sizes.
    try:
        for i in ["x", "y"]:
            if N[i] <= 0:
                N[i] = 1
            if N["t"] < 0:
                N["t"] = 0
        if "w" not in N:
            N["w"] = N["x"]
        N["v"] = N["y"]
    except KeyError:
        raise KeyError("Invalid or missing entries in N dictionary!")

    # Structure that will be degrees of freedom for the optimizer
    varStruct = ctools.struct_symSX([ctools.entry("x", repeat=N["t"]+1, shape=(N["x"], 1)),
                                     ctools.entry("w", repeat=N["t"], shape=(N["w"], 1)),
                                     ctools.entry("v", repeat=N["t"]+1, shape=(N["v"], 1))])

    # Structure that will be fixed parameters for the optimizer
    parStruct = ctools.struct_symSX([ctools.entry("y", repeat=N["t"]+1, shape=(N["y"], 1)),
                                     ctools.entry("u", repeat=N["t"], shape=(N["u"], 1)),
                                     ctools.entry("x0bar", shape=(N["x"], 1)),
                                     ctools.entry("P0", shape=(N["x"], N["x"])) ])
                                     # ctools.entry("Ad", repeat=N["t"], shape=(N["x"], N["x"])),
                                     # ctools.entry("Bd", repeat=N["t"], shape=(N["x"], N["u"])),
                                     # ctools.entry("Gd", repeat=N["t"], shape=(N["x"], N["w"])),
                                     # ctools.entry("fd", repeat=N["t"], shape=(N["x"], 1))])

    # print "Ad: ", len(parStruct["Ad"])

    # Build the objective
    obj = 0
    # First, the arrival cost
    obj += lx((varStruct["x", 0] - parStruct["x0bar"]), parStruct["P0"])
    for i in range(N["t"]):
        obj += l(varStruct["w", i], varStruct["v", i])
    # Final term of stage costs.
    obj += l(np.zeros((N["w"],)), varStruct["v", -1])  # Or should we use N["t"]+1 as index?

    # Build the constraints
    # State evolution f.
    state_constraints = []
    for t in range(N["t"]):
        state_constraints.append(varStruct["x", t+1] - f(varStruct["x",t], parStruct["u",t], np.zeros((N["w"],))) - varStruct["w",t])
                                 # casadi.mtimes(parStruct["Ad", t], varStruct["x", t]) -
                                 # casadi.mtimes(parStruct["Bd", t], parStruct["u", t]) -
                                 # casadi.mtimes(parStruct["Gd", t], varStruct["w", t]) -
                                 # parStruct["fd", t])
    # for idx, thiscon in enumerate(state_constraints):
    #     print (idx, thiscon)
    #     raw_input()

    # Measurement h.
    measurement_constraints = []
    for t in range(N["t"]+1):
        measurement_constraints.append(parStruct["y", t] - h(varStruct["x", t]) - varStruct["v", t])
    # for idx, thiscon in enumerate(measurement_constraints):
    #     print (idx, thiscon)
    #     raw_input()

    # Build up constraints.
    con = []
    for k in range(len(state_constraints)):
        con.append(state_constraints[k])
    for k in range(len(measurement_constraints)):
        con.append(measurement_constraints[k])
    # con = state_constraints + measurement_constraints
    con = casadi.vertcat(*con)

    varVal = varStruct(0)
    parVal = parStruct(0)

    if guess is not None:
        for k in set(guess.keys()).intersection(varVal.keys()):
            for i in range(len(varVal[k])):
                varVal[k,i] = guess[k,i]


    parVal["P0"] = P0
    parVal["x0bar"] = x0bar

    # if ltv_guess is not None:
    #     for k in ltv_guess.keys():
    #         for t in range(len(parVal[k])):
    #             parVal[k,t] = ltv_guess[k,t]
            # print k, parVal[k]

    for t in range(len(parVal["u"])):
        parVal["u",t] = u[t,:]

    for t in range(len(parVal["y"])):
        parVal["y", t] = y[t, :]

    # parDict = {'u': u, 'y': y}
    # for k in parDict.keys(): #("y","u"):
    #     for t in range(len(parVal[k])):
    #         parVal[k,t] = parDict[k][t, :]

    # Formulate the NLP
    nlp = {'x': varStruct, 'p': parStruct, 'f': obj, 'g': con}
    opts = {"ipopt.print_level": 0, "print_time": False, 'ipopt.max_iter': 100}
    nlp_solver = casadi.nlpsol("nlpsol", "ipopt", nlp, opts)
    if returnSolver:
        return nlp_solver
    else:
        sol = nlp_solver(x0=varVal, p=parVal, lbg=0, ubg=0)
        return varStruct(sol["x"])


def nmpc_ltv(f, l, N, x0=None, lx=None, Qn=None, lb={}, ub={}, Delta=None, ltv_guess=None, guess=None, returnSolver=False):

    N = N.copy()
    # Check specified sizes.
    try:
        for i in ["t","x"]:
            if N[i] <= 0:
                N[i] = 1
        # if e is not None and N["e"] <= 0:
        #     N["e"] = 1
    except KeyError as err:
        raise KeyError("Missing entries in N dictionary: %s" % (err.message,))

    # Structure that will be degrees of freedom for the optimizer
    varStruct = ctools.struct_symSX([ctools.entry("x", repeat=N["t"],   shape=(N["x"], 1)),
                                     ctools.entry("u", repeat=N["t"]-1, shape=(N["u"], 1))])

    # Structure that will be fixed parameters for the optimizer
    parStruct = ctools.struct_symSX([ctools.entry("x0", shape=(N["x"], 1)),
                                     ctools.entry("Qn", shape=(N["x"], N["x"])),
                                     ctools.entry("Ad", repeat=N["t"]-1, shape=(N["x"], N["x"])),
                                     ctools.entry("Bd", repeat=N["t"]-1, shape=(N["x"], N["u"])),
                                     ctools.entry("fd", repeat=N["t"]-1, shape=(N["x"], 1))])

    # Build the objective
    obj = 0
    # First, the cost-to-go. The matrix Qn might be time varying.
    obj += lx(varStruct["x",-1],parStruct["Qn"])
    for i in range(N["t"]-1):
        obj += l(varStruct["x",i],varStruct["u",i])

    # Build the constraints
    # State evolution f.
    state_constraints = []
    # Add x0 equality contraint.
    state_constraints.append(varStruct["x",0] - parStruct["x0"])

    for t in range(N["t"]-1):
        state_constraints.append(varStruct["x", t+1] -
                                 casadi.mtimes(parStruct["Ad", t], varStruct["x", t]) -
                                 casadi.mtimes(parStruct["Bd", t], varStruct["u", t]) -
                                 # casadi.mtimes(parStruct["Gd", t], varStruct["w", t]) -
                                 parStruct["fd", t])

    con = state_constraints
    con = casadi.vertcat(*con)
###
    varVal = varStruct(0)
    parVal = parStruct(0)

    lbx = varStruct(-casadi.inf)
    for k in set(lb.keys()).intersection(lbx.keys()):
        for t in range(len(lbx[k])):
            lbx[k,t] = lb[k]

    ubx = varStruct(casadi.inf)
    for k in set(ub.keys()).intersection(ubx.keys()):
        for t in range(len(ubx[k])):
            ubx[k,t] = ub[k]

    if guess is not None:
        for k in set(guess.keys()).intersection(varVal.keys()):
            for i in range(len(varVal[k])):
                varVal[k][i] = guess[k][i]
                # print guess[k][i]
                # raw_input()

    parVal["Qn"] = Qn
    parVal["x0"] = x0

    if ltv_guess is not None:
        for k in set(ltv_guess.keys()).intersection(set(["Ad", "Bd", "fd"])):
            for t in range(len(parVal[k])):
                parVal[k,t] = ltv_guess[k,t]
                # print k, ltv_guess[k,t]
                # print k, parVal[k,t]
                # raw_input()

    # Formulate the NLP
    nlp = {'x': varStruct, 'p': parStruct, 'f': obj, 'g': con}
    opts = {"ipopt.print_level": 0, "print_time": False, 'ipopt.max_iter': 100}
    nlp_solver = casadi.nlpsol("nlpsol", "ipopt", nlp, opts)
    if returnSolver:
        return nlp_solver
    else:
        sol = nlp_solver(x0=varVal, p=parVal, lbg=0, ubg=0, lbx=lbx, ubx=ubx)
        return varStruct(sol["x"]), varVal, parVal
###

def extendCasadiSymStruct(thisStruct, copycontents=False):

    structDict = {}
    structType = type(thisStruct)
    for k in thisStruct.keys():
        structDict[k] = thisStruct.struct.getStructEntryByStructIndex([k]).dict.copy()
        if 'repeat' in structDict[k].keys():
            # print structDict[k]['repeat']
            structDict[k]['repeat'] += 1

    structArgs = tuple([ctools.entry(name, **args) for (name, args) in structDict.items()])
    # extStruct = ctools.struct([structArgs])
    if isinstance(thisStruct, casadi.tools.structure.DMStruct):
        extStruct = ctools.struct_symSX([structArgs])
        extStruct = extStruct(0)
    else:
        extStruct = structType([structArgs])

    if copycontents:
        if isinstance(thisStruct,casadi.tools.structure.DMStruct):
            for k in thisStruct.keys():
                if isinstance(extStruct[k],list):
                    extStruct[k,0:-1] = thisStruct[k,:]
                    extStruct[k,-1] = thisStruct[k,-1]
                else:
                    extStruct[k] = thisStruct[k]

    return extStruct


def getCasadiSymStruct(allVars, theseVars, finalx=False, finaly=False):
    pass


def getCasadiFunc(f, varsizes, varnames=None, funcname="f", rk4=False,
                  Delta=1, M=1, scalar=True, casaditype=None):
    """
    Takes a function handle and turns it into a Casadi function.

    f should be defined to take a specified number of arguments and return a
    scalar, list, or numpy array. varnames, if specified, gives names to each
    of the inputs, but this is not required.

    sizes should be a list of how many elements are in each one of the inputs.

    This version is more general because it lets you specify arbitrary
    arguments, but you have to make sure you do everything properly.
    """
    # Pass the buck to the sub function.
    symbols = __getCasadiFunc(f, varsizes, varnames, funcname, scalar,
                              casaditype, allowmatrix=True)
    args = symbols["args"]
    fexpr = symbols["fexpr"]

    # Evaluate function and make a Casadi object.
    fcasadi = casadi.Function(funcname, args, [fexpr])

    # Wrap with rk4 if requested.
    if rk4:
        frk4 = util.rk4(fcasadi, args[0], args[1:], Delta, M)
        fcasadi = casadi.Function(funcname, args, [frk4])

    return fcasadi


def getCasadiIntegrator(f, Delta, argsizes, argnames=None, funcname="int_f",
                        abstol=1e-8, reltol=1e-8, wrap=True, verbosity=1,
                        scalar=True, casaditype=None):
    """
    Gets a Casadi integrator for function f from 0 to Delta.

    Argsizes should be a list with the number of elements for each input. Note
    that the first argument is assumed to be the differential variables, and
    all others are kept constant.

    wrap can be set to False to return the raw casadi Integrator object, i.e.,
    with inputs x and p instead of the arguments specified by the user.
    """
    # First get symbolic expressions.
    symbols = __getCasadiFunc(f, argsizes, argnames, funcname, scalar,
                              casaditype, allowmatrix=False)
    x0 = symbols["args"][0]
    par = symbols["args"][1:]
    fexpr = symbols["fexpr"]

    # Build ODE and integrator.
    ode = dict(x=x0, p=casadi.vertcat(*par), ode=fexpr)
    options = {
        "abstol": abstol,
        "reltol": reltol,
        "tf": Delta,
        "disable_internal_warnings": verbosity <= 0,
        "verbose": verbosity >= 2,
    }
    integrator = casadi.integrator(funcname, "cvodes", ode, options)

    # Now do the subtle bit. Integrator has arguments x0 and p, but we need
    # arguments as given by the user. First we need MX arguments.
    if wrap:
        names = symbols["names"]
        sizes = symbols["sizes"]
        wrappedx0 = casadi.MX.sym(names[0], *sizes[0])
        wrappedpar = [casadi.MX.sym(names[i], *sizes[i]) for i
                      in xrange(1, len(sizes))]
        wrappedIntegrator = integrator(x0=wrappedx0,
                                       p=casadi.vertcat(*wrappedpar))["xf"]
        integrator = casadi.Function(funcname, [wrappedx0] + wrappedpar,
                                     [wrappedIntegrator])
    return integrator


def __getCasadiFunc(f, varsizes, varnames=None, funcname="f", scalar=True,
                    casaditype=None, allowmatrix=True):
    """
    Core logic for getCasadiFunc and its relatives.

    Returns a dictionary with entries fexpr, rawargs, args, XX, names, sizes:
    - rawargs is the list of raw arguments, each a numpy array of Casadi
      scalars if scalar=True, or a single Casadi symbolic matrix if
      scalar=False.
    - args is the same list, but with all arguments converted to a single
      Casadi symbolic matrix.
    - fexpr is the casadi expression resulting from evaluating f(*rawargs).
    - XX is either casadi.SX or casadi.MX depending on what was used to create
      rawargs and args.
    - names is a list of string names for each argument.
    - sizes is a list of one- or two-element lists giving the sizes.
    """
    # Check names.
    if varnames is None:
        varnames = ["x%d" % (i,) for i in range(len(varsizes))]
    else:
        varnames = [str(n) for n in varnames]
    if len(varsizes) != len(varnames):
        raise ValueError("varnames must be the same length as varsizes!")

    # Loop through varsizes in case some may be matrices.
    realvarsizes = []
    for s in varsizes:
        goodInput = True
        try:
            s = [int(s)]
        except TypeError:
            if allowmatrix:
                try:
                    s = list(s)
                    goodInput = len(s) <= 2
                except TypeError:
                    goodInput = False
            else:
                raise TypeError("Entries of varsizes must be integers!")
        if not goodInput:
            raise TypeError("Entries of varsizes must be integers or "
                            "two-element lists!")
        realvarsizes.append(s)

    # Decide which Casadi type to use. XX is either casadi.SX or casadi.MX.
    if casaditype is None:
        casaditype = "SX" if scalar else "MX"
    XX = dict(SX=casadi.SX, MX=casadi.MX).get(casaditype, None)
    if XX is None:
        raise ValueError("casaditype must be either 'SX' or 'MX'!")

    # Now make the symbolic variables. How they are packaged depends on the
    # scalar option.
    if scalar:
        args = []
        for (name, size) in zip(varnames, realvarsizes):
            if len(size) == 2:
                thisarr = []
                for i in xrange(size[0]):
                    row = [XX.sym("%s_%d_%d" % (name, i, j)) for
                           j in xrange(size[1])]
                    thisarr.append(row)
            else:
                thisarr = [XX.sym("%s_%d" % (name, i)) for
                           i in xrange(size[0])]
            args.append(np.array(thisarr, dtype=object))
    else:
        args = [XX.sym(name, *size) for
                (name, size) in zip(varnames, realvarsizes)]
    catargs = [XX(a) for a in args]

    # Evaluate the function and return everything.
    fexpr = safevertcat(f(*args))
    return dict(fexpr=fexpr, args=catargs, rawargs=args, XX=XX, names=varnames,
                sizes=realvarsizes)


# =============
# Miscellany
# ============


def safevertcat(x):
    """
    Safer wrapper for Casadi's vertcat.

    the input x is expected to be an iterable containing multiple things that
    should be concatenated together. This is in contrast to Casadi 3.0's new
    version of vertcat that accepts a variable number of arguments. We retain
    this (old, Casadi 2.4) behavior because it makes it easier to check types.

    If a single SX or MX object is passed, then this doesn't do anything.
    Otherwise, if all elements are numpy ndarrays, then numpy's concatenate
    is called. If anything isn't an array, then casadi.vertcat is called.
    """
    symtypes = set(["SX", "MX"])
    xtype = getattr(x, "type_name", lambda: None)()
    if xtype in symtypes:
        val = x
    elif (not isinstance(x, np.ndarray) and
          all(isinstance(a, np.ndarray) for a in x)):
        val = np.concatenate(x)
    else:
        val = casadi.vertcat(*x)
    return val
