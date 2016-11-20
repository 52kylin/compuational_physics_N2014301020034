# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
import quyu
import erfenbijin
import pylab as pl
                           
a     = 200
Rx    = 10
Ry    = 20
V0    = 100
theta = math.pi/5
dt    = 0.1
Vx    = V0*math.cos(theta)
Vy    = V0*math.sin(theta)
R_x   = []
V_x   = []
i     = 0  
while 1 :
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if Ry*(Ry-Vy*dt)<0:
        k=(Ry-0)/(0-(Ry-Vy*dt))
        x0=((1+k)*Rx-k*Vx*dt)/(1+k)
        R_x+=[x0]
        V_x+=[Vx]
    if quyu.inZhengfangxing(Rx,Ry,a)==1\
    or quyu.inZhengfangxing(Rx,Ry,a)==0:
        continue
    if quyu.inZhengfangxing(Rx,Ry,a)==-1:
        x1=Rx-Vx*dt
        y1=Ry-Vy*dt
        x2=Rx
        y2=Ry
        t=erfenbijin.Zhengfangxing_erFenbijin(x1,y1,x2,y2,0,a)
        Rx=t[0]
        Ry=t[1]
        #continue
    if quyu.inZhengfangxing(Rx,Ry,a)==0:
        if (Rx== a or Rx==-a) and Ry>-a and Ry<a:
            Vx=-Vx
            Vy= Vy
        if (Ry== a or Ry==-a) and Rx>-a and Rx<a:
            Vx= Vx
            Vy=-Vy
        if (Rx== a and Ry== a)or(Rx==-a and Ry==a)or(Rx==a and Ry==-a)or(Rx==-a and Ry==-a):
            Vx=-Vx
            Vy=-Vy
    i+=1
    print(i)
    if i>10000:
        break
pl.plot(R_x, V_x,"o",label="Vx-Rx")
pl.title(u"正方形".encode("gb2312"))
pl.xlabel('Rx')
pl.ylabel('Vx')
pl.legend()
pl.show()

