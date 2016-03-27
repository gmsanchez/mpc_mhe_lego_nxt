# -*- coding: utf-8 -*-

# import casadi
import casadi.tools as ctools
import tools

Nx=3
Ny=2
Nu=1
Nt=2
Nw=Nx

parStruct = ctools.struct([ctools.entry("y", repeat=Nt+1, shape=(Ny, 1)),
                           ctools.entry("u", repeat=Nt, shape=(Nu, 1)),
                           ctools.entry("x0bar", shape=(Nx, 1)),
                           ctools.entry("P0", shape=(Nx, Nx)),
                           ctools.entry("Ad", repeat=Nt, shape=(Nx, Nx)),
                           ctools.entry("Bd", repeat=Nt, shape=(Nx, Nu)),
                           ctools.entry("Gd", repeat=Nt, shape=(Nx, Nw)),
                           ctools.entry("fd", repeat=Nt, shape=(Nx, 1))])


parStructSX = ctools.struct_symSX([ctools.entry("y", repeat=Nt+1, shape=(Ny, 1)),
                                   ctools.entry("u", repeat=Nt, shape=(Nu, 1)),
                                   ctools.entry("x0bar", shape=(Nx, 1)),
                                   ctools.entry("P0", shape=(Nx, Nx)),
                                   ctools.entry("Ad", repeat=Nt, shape=(Nx, Nx)),
                                   ctools.entry("Bd", repeat=Nt, shape=(Nx, Nu)),
                                   ctools.entry("Gd", repeat=Nt, shape=(Nx, Nw)),
                                   ctools.entry("fd", repeat=Nt, shape=(Nx, 1))])

parVal = parStruct(1)

parStruct1 = tools.extendCasadiSymStruct(parStruct)
parStructSX1 = tools.extendCasadiSymStruct(parStructSX)
parVal1 = tools.extendCasadiSymStruct(parVal, copycontents=True)

print type(parStruct)
print type(parStruct1)
print type(parStructSX)
print type(parStructSX1)
print type(parVal)
print type(parVal1)
