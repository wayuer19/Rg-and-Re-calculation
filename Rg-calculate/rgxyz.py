#!/usr/bin/python

###this script is used to calculate the rdf of PS-P2VP micelle
import sys,os,subprocess
import string, math
import numpy
import random
import linecache

f_xyz = open("rg.xyz","r")

np = 6000
nab = 30
nmol = np/30

points = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    for i in range(1,4):
        line[i] = float(line[i])
    points.append(line)
f_xyz.close()

##calculate Rg
Rgx,Rgy,Rgz, Res = [], [], [], []
Vees = []
for i in range(nmol):
    sumx, sumy, sumz = 0, 0, 0
    for p in range(nab):
        idx = i*nab + p
        sumx = sumx + points[idx][1]
        sumy = sumy + points[idx][2]
        sumz = sumz + points[idx][3]
    rcx, rcy, rcz = float(sumx/nab), float(sumy/nab), float(sumz/nab)
    dx,dy,dz = 0,0,0
    for j in range(nab):
        idx = i*nab + j
        dx = dx + pow((points[idx][1]-rcx),2)
        dy = dy + pow((points[idx][2]-rcy),2)
        dz = dz + pow((points[idx][3]-rcz),2)
    Rx, Ry, Rz = float(dx/nab), float(dy/nab), float(dz/nab)
    Rgx.append(Rx)
    Rgy.append(Ry)
    Rgz.append(Rz)
print numpy.mean(Rgx),numpy.std(Rgx), numpy.mean(Rgy),numpy.std(Rgy), numpy.mean(Rgz),numpy.std(Rgz)
exit
