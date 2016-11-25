# -*- coding: utf-8 -*-
import line
import math
import pylab as pl
pi = math.pi

def theSolarSystem(Rx,Ry,Vx,Vy,T):
    Rr = []
    ds=[]
    dt = 0.002
    ns = T//dt+1
    i  = 0
    while 1:
        Rr += [ (Rx[i]**2+Ry[i]**2)**(1/2) ]
        Vx += [ Vx[i]-(4*pi**2*Rx[i])/(Rr[i]**3)*dt ]
        Rx += [ Rx[i]+Vx[i+1]*dt ]
        Vy += [ Vy[i]-(4*pi**2*Ry[i])/(Rr[i]**3)*dt ]
        Ry += [ Ry[i]+Vy[i+1]*dt ]
        if i >= 2:
            ds += [ 0.5*abs(Rx[i]*Ry[i+1]-Rx[i+1]*Ry[i]) ]
        i  += 1
        if i>ns:
            break
    pl.plot(Rx,Ry,label="locat")
    pl.xlabel("x(AU)")
    pl.ylabel("y(AU)")
    pl.legend()
    pl.show()
    a=(max(Rx)-min(Rx))/2
    b=(max(Ry)-min(Ry))/2
    e=(1-(b/a)**2)**(1/2)
    k=T**2/a**3
    return k,a,b,e,ds 
Rx=[1]
Ry=[0]
Vx=[0]
Vy=[2*pi]
T =1
earth = theSolarSystem(Rx,Ry,Vx,Vy,T)
print("(k,a,b,e,Ds)=",earth)
line.line(earth[4])

"""
pl.xlabel("x(AU)")
pl.ylabel("y(AU)")
pl.legend()
pl.show()
"""
