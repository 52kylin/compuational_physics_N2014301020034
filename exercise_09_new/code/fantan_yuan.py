# -*- coding: utf-8 -*-

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
import fanshe
import pylab as pl
chuangkou = turtle.Screen()                     
wugui = turtle.Turtle()                           
wugui.shape('turtle')                             
a     = 200
Rx    = (random.random()-1/2)*a
Ry    = (random.random()-1/2)*a
V0    = 100
theta = random.random()*2*math.pi
dt    = 0.1
Vx    = V0*math.cos(theta)
Vy    = V0*math.sin(theta)

theta1 = 1
r = a
l = 2*r*math.sin(theta1/2*math.pi/180)

wugui.penup()
wugui.forward(r)
wugui.left(90+theta1/2)
wugui.pendown()

i=0
while 1:
    wugui.forward(l)
    wugui.left(theta1)
    i+=1
    if i > int(360/theta1):
        break
wugui.penup()
wugui.goto(Rx,Ry)
wugui.pendown()

R_x=[]
V_x=[]


i=0
while 1 :
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if quyu.inYuan(Rx,Ry,a)==1:
        wugui.goto(Rx,Ry)
        #continue
    if  quyu.inYuan(Rx,Ry,a)==0:
        wugui.goto(Rx,Ry)
        nx=Rx/(Rx*Rx+Ry*Ry)**(1/2)
        ny=Ry/(Rx*Rx+Ry*Ry)**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    if quyu.inYuan(Rx,Ry,a)==-1:
        x1=Rx-Vx*dt
        y1=Ry-Vy*dt
        x2=Rx
        y2=Ry
        t=erfenbijin.yuan_erFenbijin(x1,y1,x2,y2,0,a)
        Rx=t[0]
        Ry=t[1]
        wugui.goto(Rx,Ry)
        nx=Rx/(Rx*Rx+Ry*Ry)**(1/2)
        ny=Ry/(Rx*Rx+Ry*Ry)**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    R_x+=[Rx]
    V_x+=[Vx]
    i+=1
    print(i)
    if i >10000:
        break

pl.plot(R_x, V_x,"o",label="V_x-R_x")
pl.title("V_x-R_x")
pl.xlabel('R_x')
pl.ylabel('V_x')
pl.legend()
pl.show()

chuangkou.exitonclick() 