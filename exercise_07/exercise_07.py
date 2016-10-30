# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:59:09 2016

@author: Kylin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:57:06 2016

@author: Kylin
"""
import pylab as pl
import math
class pendulum:
    def __init__(self,time_step=0.04,total_time=100):
        self.omiga0 = [0]
        self.xita0  = [0.2]
        self.omiga1 = [0]
        self.xita1  = [0.2]
        self.t     = [0]
        self.dxita = [0]
        self.dxitamax = []
        self.dtmax = []
        self.T =[]
        self.F =[]
        self.q0    =  0.5+0.1
        self.q1    =  0.5
        self.Fd    =  0.5
        self.om    =  2/3
        self.g     = 9.8
        self.m     = 10
        self.l     = 9.8
        self.dt    = time_step
        self.time  = total_time
        self.nsteps= int(total_time//time_step+1)
    def run(self):
        for i in range(self.nsteps):
            A0 = self.omiga0[i]-(self.g/self.l*math.sin(self.xita0[i])+self.q0*self.omiga0[i]+self.Fd*math.sin(self.om*self.t[i]))*self.dt
            self.omiga0.append(A0)
            B0 = self.xita0[i]+self.omiga0[i+1]*self.dt
            self.xita0.append(B0)
            A1 = self.omiga1[i]-(self.g/self.l*math.sin(self.xita1[i])+self.q1*self.omiga1[i]+self.Fd*math.sin(self.om*self.t[i]))*self.dt
            self.omiga1.append(A1)
            B1 = self.xita1[i]+self.omiga1[i+1]*self.dt
            self.xita1.append(B1)
            C = self.t[i]+self.dt                         
            self.t.append(C)  
            D = (abs(self.xita0[i+1]-self.xita1[i+1]))
            self.dxita.append(D)
        for i in range(len(self.dxita)):
            if i >1:
                self.F.append(math.log10(self.dxita[i]))
                self.T.append(self.t[i])
        for i in range(len(self.F)):
            if i > 1 and i < len(self.F)-1:
                if self.F[i+1] < self.F[i] and self.F[i] >= self.F[i-1]:
                    self.dxitamax.append(self.F[i])
                    self.dtmax.append(self.T[i]) 

        del self.dxitamax[0:2]
        del self.dtmax[0:2]
        
    def show_results(self):
        
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.T,self.F)
        pl.plot(self.dtmax, self.dxitamax)
        pl.title('pendulum', fontdict = font)
        pl.xlabel('t ($s$)')
        pl.ylabel('log10(dertaxita) ($e-10$)')
        pl.show()
        
a = pendulum()
a.run()
a.show_results()