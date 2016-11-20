# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math
import quyu
import erfenbijin
import fanshe
import pylab as pl
                          
a     = 0
Rx    = 10
Ry    = 10
V0    = 100
theta = math.pi/4
dt    = 0.1
Vx    = V0*math.cos(theta)
Vy    = V0*math.sin(theta)
r     = 1000

print(Rx)
print(Ry)
print(theta)

R_x=[]
V_x=[]


i=0
while 1 :
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if Ry*(Ry-Vy*dt)<0:
        k=(Ry-0)/(0-(Ry-Vy*dt))
        x0=((1+k)*Rx-k*Vx*dt)/(1+k)
        R_x+=[x0]
        V_x+=[Vx]
    if quyu.inBianyuan(Rx,Ry,r,a)==1:
        continue
    if quyu.inBianyuan(Rx,Ry,r,a)==0:
        if Rx==a:
            nx=1
            ny=0
        if Rx==-a:
            nx=-1
            ny=0
        if Ry>a:
            nx=(Rx-0)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
            ny=(Ry-a)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
        if Ry<a:
            nx=(Rx-0)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
            ny=(Ry+a)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    if quyu.inBianyuan(Rx,Ry,r,a)==-1:
        x1=Rx-Vx*dt
        y1=Ry-Vy*dt
        x2=Rx
        y2=Ry
        t=erfenbijin.Bianyuan_erFenbijin(x1,y1,x2,y2,r,a)
        Rx=t[0]
        Ry=t[1]
        if Rx==a:
            nx=1
            ny=0
        if Rx==-a:
            nx=-1
            ny=0
        if Ry>a:
            nx=(Rx-0)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
            ny=(Ry-a)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
        if Ry<a:
            nx=(Rx-0)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
            ny=(Ry+a)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    i+=1
    print(i)
    if i >10000:
        break

pl.plot(R_x, V_x,"o",label="Vx-Rx")
pl.title("Vx-Rx:r=1000,a=0,v0=100,theta=pi/4")
pl.xlabel('Rx')
pl.ylabel('Vx')
pl.legend()
pl.show()
