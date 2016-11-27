# -*- coding: utf-8 -*-
import math
def init(i):
    GMs,a,e,Mp,Ms=i[0],i[1],i[2],i[3],i[4]
    vmax=(GMs)**(1/2)*((1/a)*((1+e)/(1-e))*(1+Mp/Ms))**(1/2)
    vmin=(GMs)**(1/2)*((1/a)*((1-e)/(1+e))*(1+Mp/Ms))**(1/2)
    return vmax

Venus   =  [4*math.pi**2,0.72,0.007,4.9*10**24,2*10**30]
Earth   =  [4*math.pi**2,1.00,0.017,6.0*10**24,2*10**30]
Mars    =  [4*math.pi**2,1.52,0.093,6.6*10**23,2*10**30]
Jupiter =  [4*math.pi**2,5.20,0.048,1.9*10**27,2*10**30]
Saturn  =  [4*math.pi**2,9.54,0.056,5.7*10**26,2*10**30]


V=init(Venus)
print("Venus:",V)

V=init(Earth)
print("Earth:",V)

V=init(Mars)
print("Mars:",V)

V=init(Jupiter)
print("jupiter:",V)

V=init(Saturn)
print("Saturn:",V)