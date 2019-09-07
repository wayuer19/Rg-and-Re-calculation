#!/usr/bin/python

###this script is used to calculate the end-to-end distance of backbone of ACPs
from __future__ import division
import sys,os,subprocess
import string, math
import numpy as np
import random
import linecache

f_xyz = open("re.xyz","r")   ##input file

tot = 4000   ##total number of CG beads
nab = 2   ## bead number of one ACP backbone
nmol = int(tot/nab) ## total number of ACP backbone

points = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    for i in range(1,4):
        line[i] = float(line[i])
    points.append(line)
f_xyz.close()

##calculate Re
Res = []
Vee = [0,0,0]
for i in range(nmol):
    p1 = i*nab
    p2 = p1 + 1
    Vee[0], Vee[1], Vee[2] = points[p1][1]-points[p2][1], points[p1][2]-points[p2][2], points[p1][3]-points[p2][3]
    Re = math.sqrt(pow(Vee[0],2) + pow(Vee[1],2) +pow(Vee[2],2))
    Res.append(Re)
print np.mean(Res), np.std(Res)

exit
