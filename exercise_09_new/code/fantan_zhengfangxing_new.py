# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
import turtle                                      
import random
import quyu
import erfenbijin
import pylab as pl
chuangkou = turtle.Screen()                     
wugui = turtle.Turtle()                           
wugui.shape('turtle')                             
a     = 200
Rx    = (random.random()-1/2)*2*a
Ry    = (random.random()-1/2)*2*a
V0    = 100
theta = random.random()*2*math.pi
dt    = 0.1
Vx    = V0*math.cos(theta)
Vy    = V0*math.sin(theta)

wugui.penup()
wugui.goto(a,a)
wugui.pendown()
wugui.left(90)
for i in range(4):
    wugui.left(90)
    wugui.forward(2*a)
wugui.penup()
wugui.goto(Rx,Ry)
wugui.pendown()

if Rx ==  Ry and theta == math.pi*1/4 :
    while 1 :
        wugui.goto(a,a)
        wugui.goto(-a,-a)
if Rx ==  Ry and theta == math.pi*5/4 :
    while 1 :
        wugui.goto(-a,-a)
        wugui.goto(a,a)
if Rx == -Ry and theta == math.pi*3/4 :
    while 1 :
        wugui.goto(-a,a)
        wugui.goto(a,-a)
if Rx == -Ry and theta == math.pi*7/4 :
    while 1 :
        wugui.goto(a,-a)
        wugui.goto(-a,a)

R_x=[]
V_x=[]
i=0  
while 1 :
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if quyu.inZhengfangxing(Rx,Ry,a)==1\
    or quyu.inZhengfangxing(Rx,Ry,a)==0:
        wugui.goto(Rx,Ry)
        #continue
    if quyu.inZhengfangxing(Rx,Ry,a)==-1:
        x1=Rx-Vx*dt
        y1=Ry-Vy*dt
        x2=Rx
        y2=Ry
        t=erfenbijin.Zhengfangxing_erFenbijin(x1,y1,x2,y2,0,a)
        Rx=t[0]
        Ry=t[1]
        wugui.goto(Rx,Ry)
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
    R_x+=[Rx]
    V_x+=[Vx]
    i+=1
    print(i)
    if i>10000:
        break
pl.plot(R_x, V_x,"o",label="V_x-R_x")
pl.title("V_x-R_x")
pl.xlabel('R_x')
pl.ylabel('V_x')
pl.legend()
pl.show()

chuangkou.exitonclick() 