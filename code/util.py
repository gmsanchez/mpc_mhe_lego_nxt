import numpy as np
import scipy.linalg
import casadi.tools as ctools


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
