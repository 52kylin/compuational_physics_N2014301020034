# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:57:06 2016

@author: Kylin
"""
import pylab as pl
import math
class pendulum:
    def __init__(self,time_step=0.04,total_time=50):
        self.omiga0 = [0]
        self.xita0  = [0.2]
        self.t     = [0]
        self.q0    =  0.5
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
            C = self.t[i]+self.dt                         
            self.t.append(C)  
        
    def show_results(self):
        
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.t,self.xita0)
        #pl.plot(self.xita0, self.omiga0)
        pl.title('pendulum Fd=1.2', fontdict = font)
        pl.xlabel('xita ($rad$)')
        pl.ylabel('omiga ($rad$)')
        pl.show()
        
a = pendulum()
a.run()
a.show_results()
