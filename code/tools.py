import casadi
import numpy as np
import util


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
