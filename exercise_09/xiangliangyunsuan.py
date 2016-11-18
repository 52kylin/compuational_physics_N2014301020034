# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 00:27:03 2016

@author: Kylin
"""
import math
def mo(a):
    return (a[0]**2+a[1]**2+a[2]**2)**(1/2)

def dianji(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def chaji(a,b):
    x = a[1]*b[2]-a[2]*b[1]
    y = a[2]*b[0]-a[0]*b[2]
    z = a[0]*b[1]-a[1]*b[0]
    return [x,y,z]
    
def angle(a,b):
    s = dianji(a,b)/(mo(a)*mo(b))
    ang=math.acos(s)
    return ang

def jueduijiao(x):
    """第一象限"""
    if x[0] > 0 and x[1] > 0:
        theta = math.atan(x[1]/x[0])+math.pi*0
    """第二象限"""
    if x[0] < 0 and x[1] > 0:
        theta = math.atan(x[1]/x[0])+math.pi*1
    """第三象限"""
    if x[0] < 0 and x[1] < 0:
        theta = math.atan(x[1]/x[0])+math.pi*1
    """第四象限"""
    if x[0] > 0 and x[1] < 0:
        theta = math.atan(x[1]/x[0])+math.pi*2
        
    if x[0] == 0 and x[1] > 0:
        theta = math.pi/2
    if x[0] == 0 and x[1] < 0:
        theta = math.pi/2*3
    return theta
