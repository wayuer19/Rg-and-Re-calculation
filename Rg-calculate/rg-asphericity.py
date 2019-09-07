#!/usr/bin/python

###this script is used to calculate the matrix of Rg
from __future__ import division
import string, math
import numpy
import random
import linecache

f_xyz = open("rg.xyz","r")
f_asp = open("asphs.dat","w")

np = 30000
nab = 30
nmol = int(np/30)

pts = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    for i in range(1,4):
        line[i] = float(line[i])
    pts.append(line)
f_xyz.close()

##calculate Rg
Rg2s = []
asphs = []  ## asphericity
for i in range(nmol):
    sumx, sumy, sumz = 0, 0, 0
    for p in range(nab):
        idx = i*nab + p
        sumx = sumx + pts[idx][1]
        sumy = sumy + pts[idx][2]
        sumz = sumz + pts[idx][3]
    rcx, rcy, rcz = float(sumx/nab), float(sumy/nab), float(sumz/nab)
    Sxx,Sxy,Sxz,Syx,Syy,Syz,Szx,Szy,Szz = 0,0,0,0,0,0,0,0,0
    for j in range(nab):
        idx = i*nab + j
        xic = pts[idx][1]-rcx
        yic = pts[idx][2]-rcy
        zic = pts[idx][3]-rcz
        Sxx = Sxx + xic*xic
        Sxy = Sxy + xic*yic
        Sxz = Sxz + xic*zic
        Syx = Syx + yic*xic
        Syy = Syy + yic*yic
        Syz = Syz + yic*zic
        Szx = Szx + zic*xic
        Szy = Szy + zic*yic
        Szz = Szz + zic*zic
    S = [[Sxx/nab,Sxy/nab,Sxz/nab],[Syx/nab,Syy/nab,Syz/nab],[Szx/nab,Szy/nab,Szz/nab]]
    S_eig,S_vec = numpy.linalg.eig(S)   ##characteristic values and characteristic vector of the Matrix S
#mean square of lambda can be calculated from the diagonalization of S
#    D = S_vec[1]
#    S_diag = numpy.dot(numpy.dot(numpy.linalg.inv(D),S),D)
#    S_diag = numpy.around(S_diag, decimals = 8, out=None)
#    lam1, lam2, lam3 = S_diag[2][2], S_diag[1][1], S_diag[0][0]
##mean squre of lambda can also be calculated from the characteristic values of matrix S, lambda**2 = characteristic value
    lam1, lam2, lam3 = S_eig[0], S_eig[1], S_eig[2]
    Rg2 = lam1+lam2+lam3
    Rg2s.append(Rg2)
    asph = float(((lam1-lam2)**2+(lam1-lam3)**2+(lam2-lam3)**2)/(2*((lam1+lam2+lam3)**2)))
    asphs.append(asph)
print numpy.mean(Rg2s),numpy.std(Rg2s)
print numpy.mean(asphs), numpy.std(asphs)

##calculate the distribution of asphericity
delt = 0.05
maxbin = int(1.0/delt)+1
nums = [0]*maxbin
for i in range(nmol):
    bin_i = int(asphs[i]/delt)
    nums[bin_i]+=1
for bin_i in range(maxbin):
    if nums[bin_i] != 0:
        frac = nums[bin_i]/nmol
        print >> f_asp, bin_i*delt, frac
f_asp.close()
exit
