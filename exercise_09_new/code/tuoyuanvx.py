# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
import erfenbijin
import fanshe
import pylab as pl

a         =  200
Rx        =  0
Ry        =  0
V0        =  200
theta     =  -math.pi/6
dt        =  0.05
Vx        =  V0*math.cos(theta)
Vy        =  V0*math.sin(theta)


a0        =  300
b0        =  200
c0        =  ((a0)**2-(b0)**2)**(1/2)


Rx        = -10
Ry        = 0

R_x=[]
V_x=[]
i=0
while 1 :
    Rx    = Rx+Vx*dt
    Ry    = Ry+Vy*dt
    if Ry*(Ry-Vy*dt)<0 and (Ry-Vy*dt)!=0:
        k=(Ry-0)/(0-(Ry-Vy*dt))
        x0=((1+k)*Rx-k*Vx*dt)/(1+k)
        R_x+=[x0]
        V_x+=[Vx]
    if (Rx/a0)**2+(Ry/b0)**2 <  1:
        continue
    if (Rx/a0)**2+(Ry/b0)**2 == 1:

        rn = ((Rx/a0**2)**2+(Ry/b0**2)**2)**(1/2)
        nx = ( Rx/a0**2)/rn
        ny = ( Ry/b0**2)/rn
        
        t  = fanshe.fanshe(Vx,Vy,nx,ny)
        Vx = t[0]
        Vy = t[1]
        #continue
    if (Rx/a0)**2+(Ry/b0)**2 >  1:
        x1 = Rx-Vx*dt
        y1 = Ry-Vy*dt
        x2 = Rx
        y2 = Ry
        t  = erfenbijin.tuoyuan_erFenbijin(x1,y1,x2,y2,a0,b0)
        Rx = t[0]
        Ry = t[1]
        
        rn = ((Rx/a0**2)**2+(Ry/b0**2)**2)**(1/2)
        nx = ( Rx/a0**2)/rn
        ny = ( Ry/b0**2)/rn
        
        t  = fanshe.fanshe(Vx,Vy,nx,ny)
        Vx = t[0]
        Vy = t[1]
        #continue
    i+=1
    print(i)
    if i >10000:
        break
pl.plot(R_x, V_x,"o",label="Vx-Rx")
pl.title("Vx-Rx")
pl.xlabel('Rx')
pl.ylabel('Vx')
pl.legend()
pl.show()
