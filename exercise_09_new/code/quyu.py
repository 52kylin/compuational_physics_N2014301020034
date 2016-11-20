# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 09:56:26 2016

@author: Kylin
"""

def inYuan(x,y,r):
    s=(x*x+y*y)**(1/2)
    if s < r :
        return 1
    if s == r:
        return 0
    else:
        return -1
def inZhengfangxing(x,y,a):
    if x > -a and x < a and y > -a and y < a :
        return 1
    if ( x ==  a and y >= -a and y <= a ) \
    or ( x == -a and y >= -a and y <= a ) \
    or ( y ==  a and x >= -a and x <= a ) \
    or ( y == -a and x >= -a and x <= a ) :
        return 0
    else:
        return -1
def inBianyuan(x,y,r,a):
    if ( x > -r and x < r and y > -a and y < a )\
    or ( y >  a and x*x+(y-a)*(y-a) < r*r)      \
    or ( y < -a and x*x+(y+a)*(y+a) < r*r)      :
        return 1
    if ( x ==  r and y >= -a and y <= a     ) \
    or ( x == -r and y >= -a and y <= a     ) \
    or ( y >=  a and x*x+(y-a)*(y-a) == r*r ) \
    or ( y <= -a and x*x+(y+a)*(y+a) == r*r ) :
        return 0
    else:
        return -1