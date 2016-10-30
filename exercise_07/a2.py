# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:57:06 2016

@author: Kylin
"""
import pylab as pl
class pendulum:
    def __init__(self,time_step=0.04,total_time=10):
        self.omiga = [1]
        self.xita  = [0]
        self.t     = [0]
        self.g     = 9.8
        self.m     = 10
        self.l     = 1
        self.dt    = time_step
        self.time  = total_time
        self.nsteps= int(total_time//time_step+1)
    def run(self):
        for i in range(self.nsteps):
            self.omiga.append(self.omiga[i]-self.g/self.l*self.xita[i]*self.dt)
            self.xita.append(self.xita[i]+self.omiga[i+1]*self.dt)                               
            self.t.append(self.t[i]+self.dt)     
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.t, self.xita)
        pl.title('pendulum', fontdict = font)
        pl.xlabel('t ($s$)')
        pl.ylabel('xita ($rad$)')
        pl.show()
        
a = pendulum()
a.run()
a.show_results()