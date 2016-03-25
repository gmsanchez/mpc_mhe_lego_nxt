import numpy as np
import scipy.linalg


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