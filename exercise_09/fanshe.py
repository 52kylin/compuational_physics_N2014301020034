# -*- coding: utf-8 -*-
import math
import xiangliangyunsuan
def fanshe(Vx,Vy,nx,ny):
    V=[Vx,Vy]           #y
    N=[nx,ny]           #y
    
    thetaV=xiangliangyunsuan.jueduijiao(V)
    thetaN=xiangliangyunsuan.jueduijiao(N)

    V=(Vx*Vx+Vy*Vy)**(1/2)  #y
    
    Vnx =  V*math.cos(thetaV-thetaN)*math.cos(thetaN)    #y
    Vny =  V*math.cos(thetaV-thetaN)*math.sin(thetaN)    #y
    Vtx = -V*math.sin(thetaV-thetaN)*math.sin(thetaN)    #y
    Vty =  V*math.sin(thetaV-thetaN)*math.cos(thetaN)    #y

    Vx=-Vnx+Vtx             #y
    Vy=-Vny+Vty             #y
    return [Vx,Vy]          #y
