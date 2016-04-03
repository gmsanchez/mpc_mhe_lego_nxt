import casadi
import casadi.tools as ctools
import model_lego as model
import numpy as np
from collections import deque
from itertools import islice
from itertools import tee, izip


f = model.F
h = model.H

Nx = model.Nx
Nu = model.Nu
Nw = model.Nw
Ny = model.Ny
Nv = model.Nv

Delta = 0.1
Nt = 10         # Horizon size
Nsim = 80


def window0(seq, n=2, fillvalue=None):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def window1(seq, n=2, fillvalue=None):
    seq[0:-1] = seq[1:-1]
    seq[-1] = fillvalue
    return seq


def window2(seq, n=3):
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win


def window3(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)

ltvStruct = ctools.struct_symSX([ctools.entry("y", repeat=Nt + 1, shape=(Ny, 1)),
                                 ctools.entry("u", repeat=Nt, shape=(Nu, 1)),
                                 ctools.entry("x0bar", shape=(Nx, 1)),
                                 ctools.entry("P0", shape=(Nx, Nx)),
                                 ctools.entry("Ad", repeat=Nt, shape=(Nx, Nx)),
                                 ctools.entry("Bd", repeat=Nt, shape=(Nx, Nu)),
                                 ctools.entry("Gd", repeat=Nt, shape=(Nx, Nw)),
                                 ctools.entry("fd", repeat=Nt, shape=(Nx, 1))])


ltv_val = ltvStruct(0)
ltv_key = "Ad"
for k in range(len(ltv_val[ltv_key])):
    ltv_val[ltv_key,k,:] = k

print ltv_val[ltv_key]

new_val = 10*np.ones((Nx, Nx))

ltv_dict = {ltv_key: np.tile(new_val,Nt)}

a0 = window0(ltv_val[ltv_key], Nt, new_val)
a1 = window1(ltv_val[ltv_key], Nt, new_val)
a2 = window2(ltv_val[ltv_key], Nt)
a3 = window3(ltv_val[ltv_key], Nt)