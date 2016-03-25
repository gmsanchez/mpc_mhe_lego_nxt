import numpy as np
import scipy.linalg
import casadi.tools as ctools


def rk4(f, x0, par, Delta=1, M=1):
    """
    Does M RK4 timesteps of function f with variables x0 and parameters par.

    The first argument of f must be var, followed by any number of parameters
    given in a list in order.

    Note that var and the output of f must add like numpy arrays.
    """
    h = Delta/M
    x = x0
    j = 0
    while j < M: # For some reason, a for loop creates problems here.
        k1 = f(x,*par)
        k2 = f(x + k1*h/2,*par)
        k3 = f(x + k2*h/2,*par)
        k4 = f(x + k3*h,*par)
        x = x + (k1 + 2*k2 + 2*k3 + k4)*h/6
        j += 1
    return x


def c2d(A, B, Delta, Bp=None, f=None, asdict=False):
    """
    Discretizes affine system (A, B, Bp, f) with timestep Delta.

    This includes disturbances and a potentially nonzero steady-state, although
    Bp and f can be omitted if they are not present.

    If asdict=True, return value will be a dictionary with entries A, B, Bp,
    and f. Otherwise, the return value will be a 4-element list [A, B, Bp, f]
    if Bp and f are provided, otherwise a 2-element list [A, B].
    """
    n = A.shape[0]
    I = np.eye(n)
    D = scipy.linalg.expm(Delta*np.vstack((np.hstack([A, I]),
                                           np.zeros((n, 2*n)))))
    Ad = D[:n, :n]
    Id = D[:n, n:]
    Bd = Id.dot(B)
    Bpd = None if Bp is None else Id.dot(Bp)
    fd = None if f is None else Id.dot(f)

    if asdict:
        retval = dict(A=Ad, B=Bd, Bp=Bpd, f=fd)
    elif Bp is None and f is None:
        retval = [Ad, Bd]
    else:
        retval = [Ad, Bd, Bpd, fd]
    return retval


def mtimes(*args, **kwargs):
    """
    Smarter version casadi.tools.mtimes.

    Matrix multiplies all of the given arguments and returns the result. If any
    inputs are Casadi's SX or MX data types, uses Casadi's mtimes. Otherwise,
    uses a sequence of np.dot operations.

    Keyword arguments forcedot or forcemtimes can be set to True to pick one
    behavior or another.
    """
    # Get keyword arguments.
    forcemtimes = kwargs.pop("forcemtimes", None)
    forcedot = kwargs.pop("forcedot", False)
    if len(kwargs) > 0:
        raise TypeError("Invalid keywords: %s" % kwargs.keys())

    # Pick whether to use mul or dot.
    if forcemtimes:
        if forcedot:
            raise ValueError("forcemtimes and forcedot can't both be True!")
        useMul = True
    elif forcedot:
        useMul = False
    else:
        useMul = False
        symtypes = set(["SX", "MX"])
        for a in args:
            atype = getattr(a, "type_name", lambda : None)()
            if atype in symtypes:
                useMul = True
                break

    # Now actually do multiplication.
    ans = ctools.mtimes(args) if useMul else reduce(np.dot, args)
    return ans


def jaccsd(fun, x, u=None):
    """ Jacobian through complex step differentiation

    :param fun: any python callable function
    :param np.multiarray.ndarray x: vector of current state of the system
    :param np.multiarray.ndarray u: vector of current input of the system
    :return: A = df(x,u)/dx, B = df(x,u)/du

    References:
    [1] http://blogs.mathworks.com/cleve/2013/10/14/complex-step-differentiation/
    [2] http://mdolab.engin.umich.edu/sites/default/files/Martins2003CSD.pdf
    """

    if u is None:
        p = 0
        z = fun(x)
        m = np.size(z)
        B = np.zeros([m, p])
    else:
        p = np.size(u)
        z = fun(x, u)
        m = np.size(z)
        B = np.zeros([m, p])

    # Just to make sure we don't touch the the original values when we convert them to complex numbers.
    u = u.astype(complex, copy=True).ravel()
    x = x.astype(complex, copy=True).ravel()

    n = np.size(x)
    A = np.zeros([m, n])

    # Get machine espsilon for floats
    h = np.finfo(np.float).eps * 100
    for k in range(n):
        x1 = x.copy()
        x1[k] += h * 1j
        if u is None:
            A[:, k] = np.imag(fun(x1)) / h
        else:
            A[:, k] = np.imag(fun(x1, u)) / h

    for k in range(p):
        u1 = u.copy()
        u1[k] += h * 1j
        B[:, k] = np.imag(fun(x, u1)) / h

    return [z, A, B]
