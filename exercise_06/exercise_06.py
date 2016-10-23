# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:14:00 2016

@author: Kylin
"""
import math
import pylab as pl
class cannon:
    def __init__(self, dv =1,xita=0,mass=70, time_step=0.1,total_time=200, initial_velocity=1000,g=9.8,b2=4*10**(-5),v_wind=10,T=300,a=6.5*10**(-3),alpha=2.5):
        self.v = []
        self.x = [0]
        self.vx= []
        self.y = [0]
        self.vy= []
        self.v_wind = v_wind
        self.t = [0]
        self.T=T
        self.g = g
        self.b2 = b2
        self.m = mass
        self.dt = time_step
        self.time = total_time   
        self.nsteps=total_time//time_step+1
        self.a=a
        self.alpha=alpha
        self.dv=dv
        self.xita=xita
        self.minv=[]
        self.jiaodu=[]
    def run(self):
        x_goal=float(input("输入目标距离："))
        print(x_goal)
        y_goal=float(input("输入目标高度："))
        print(y_goal)
        for j in range(90):
            xita=j*math.pi/180
            for k in range(1000):
                v0=k*self.dv
                self.v=[v0]
                self.vx.append(self.v[0]*math.cos(xita))
                self.vy.append(self.v[0]*math.sin(xita))
                for i in range(2000):
                    vx1 = self.vx[i]+self.v_wind
                    v1  = (vx1**2+self.vy[i]**2)**0.5
                    vx  =  self.vx[i]-self.b2/self.m*(1-self.a*self.y[i]/self.T)**self.alpha*v1*vx1*self.dt
                    vy  =  self.vy[i]-self.b2/self.m*(1-self.a*self.y[i]/self.T)**self.alpha*v1*self.vy[i]*self.dt-self.g*self.dt
                    x   =  self.x[i] +self.vx[i]*self.dt
                    y   =  self.y[i] +self.vy[i]*self.dt    
                    self.vx.append(vx)
                    self.vy.append(vy)
                    self.x.append(x)
                    self.y.append(y)
                    if self.y[i]<0:
                        break    
                    if self.y[i-1] > y_goal:
                        if self.y[i] < y_goal:
                            if  self.vy[i] < 0:
                                if self.x[i-1] < x_goal:
                                    if self.x[i] > x_goal:
                                        r=-self.y[i]/(self.y[i+1]-10**(-6))
                                        xmax=(self.x[i]+r*self.x[i+1])/(1+r)
                                        print("最远射程:",xmax)
                                        print("初始速度:",v0)
                                        print("初始角度:",xita)
                                        self.minv.append(v0)
                                        self.jiaodu.append(xita)
                
                del self.v[:]
                del self.vx[:]
                del self.vy[:]
                del self.x[1:]
                del self.y[1:]
        min_v=min(self.minv)
        print(self.minv)
        print(min_v)
        print('结束')
a = cannon()
a.run()


