# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:07:48 2016

@author: Kylin
"""
import quyu
def yuan_erFenbijin(x1,y1,x2,y2,r,a):
    x0=0
    y0=0
    while 1 :
        x0=(x1+x2)/2
        y0=(y1+y2)/2
        if abs(x1-x2)<0.000001 and abs(y1-y2)<0.000001:
            break
        if quyu.inYuan(x0,y0,r) ==  1:
            x1=x0
            y1=y0
            continue
        if quyu.inYuan(x0,y0,r) == -1:
            x2=x0
            y2=y0
            continue
        if quyu.inYuan(x0,y0,r) ==  0:
            break 
    return [x0,y0]
def tuoyuan_erFenbijin(x1,y1,x2,y2,a0,b0):
    x0=0
    y0=0
    while 1 :
        x0=(x1+x2)/2
        y0=(y1+y2)/2
        if abs(x1-x2)<0.000001 and abs(y1-y2)<0.000001:
            break
        if (x0/a0)**2+(y0/b0)**2< 1:
            x1=x0
            y1=y0
            continue
        if (x0/a0)**2+(y0/b0)**2> 1:
            x2=x0
            y2=y0
            continue
        if (x0/a0)**2+(y0/b0)**2==1:
            break 
    return [x0,y0]
def Zhengfangxing_erFenbijin(x1,y1,x2,y2,r,a):
    x0=0
    y0=0
    while 1 :
        x0=(x1+x2)/2
        y0=(y1+y2)/2
        if quyu.inZhengfangxing(x0,y0,a) ==  1:
            x1=x0
            y1=y0
            continue
        if quyu.inZhengfangxing(x0,y0,a) == -1:
            x2=x0
            y2=y0
            continue
        if quyu.inZhengfangxing(x0,y0,a) ==  0:
            break  
    return [x0,y0]
def Bianyuan_erFenbijin(x1,y1,x2,y2,r,a):
    x0=0
    y0=0
    while 1 :
        x0=(x1+x2)/2
        y0=(y1+y2)/2
        if abs(x1-x2)<0.000001 and abs(y1-y2)<0.000001:
            break
        if quyu.inBianyuan(x0,y0,r,a) ==  1:
            x1=x0
            y1=y0
            continue
        if quyu.inBianyuan(x0,y0,r,a) == -1:
            x2=x0
            y2=y0
            continue
        if quyu.inBianyuan(x0,y0,r,a) ==  0:
            break 
    return [x0,y0]