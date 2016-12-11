# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 01:39:23 2016

@author: Kylin
"""

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

global error
error=1e-5
def method_Jacobi(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0
    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0
    V=[]
    V += [v]
    s=0
    while 1:
        V += [v]
        for i in range(1,L-1):
            for j in range(1,L-1):
                V[s+1][i][j]=(V[s][i+1][j]+V[s][i-1][j]+V[s][i][j+1]+V[s][i][j-1])/4.0
        for i in [x]:
            for j in range(x,y+1):
                V[s+1][j][i]=1.0
        for i in [y]:
            for j in range(x,y+1):
                V[s+1][j][i]=-1.0
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
def method_GS(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0

    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0   
    V=[]
    V+=[V]
    s=0
    while 1:
        V+=[V]
        for i in range(1,L-1):
            for j in range(1,L-1):
                V[s+1][i][j]=(V[s][i+1][j]+V[s+1][i-1][j]+V[s][i][j+1]+V[s+1][i][j-1])/4.0
        for i in [x]:
            for j in range(x,y+1):
                V[s+1][j][i]=1.0
        for i in [y]:
            for j in range(x,y+1):
                V[s+1][j][i]=-1.0
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
def method_SOR(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0

    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0   
    V=[]
    V+=[V]
    alpha=2.0/(1+pi/L)
    s=0
    while 1:
        V+=[V]
        for i in range(1,L-1):
            for j in range(1,L-1):               
                V[s+1][j][i]=(V[s][j+1][i]+V[s+1][j-1][i]+V[s][j][i+1]+V[s+1][j][i-1])/4.0
                if i==a and j>a-1 and j<b+1:
                    V[s+1][j][i]=1.0
                if i==b and j>a-1 and j<b+1:
                    V[s+1][j][i]=-1.0
                V[s+1][j][i]=alpha*(V[s+1][j][i]-V[s][j][i])+V[s][j][i] 
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                 dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
L    = []
M    = []
N    = []
O    = []
f=open('data_of_problem5.7.txt','w')
for i in range(6,61,5):
    J=method_Jacobi(i)
    G=method_GS(i)
    S=method_SOR(i)
    L    += [i]
    M    += [J]
    N    += [G]
    O    += [S]
f.close()
plot(L,M)
plot(L,N)
plot(L,O)
scatter(L,M)
scatter(L,N)
scatter(L,O)
legend(('Jacobi method','GS method','SOR  method'))
title('3 different methods')
xlabel('L')
ylim(0,1000)
ylabel('N')
savefig('methods.png')
show()
