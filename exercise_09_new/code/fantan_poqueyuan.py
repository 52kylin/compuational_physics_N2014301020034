# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
#import turtle                                      
import random
import quyu
import erfenbijin
import fanshe
import pylab as pl
#chuangkou = turtle.Screen()                     
#wugui = turtle.Turtle()                           
#wugui.shape('turtle')                             
a     = 1
Rx    = (random.random()-1/2)*a
Ry    = (random.random()-1/2)*a
V0    = 100
theta = random.random()*2*math.pi
dt    = 0.1
Vx    = V0*math.cos(theta)
Vy    = V0*math.sin(theta)

theta1 = 1
r = 1000
l = 2*r*math.sin(theta1/2*math.pi/180)
'''
wugui.penup()
wugui.forward(r)
wugui.pendown()
wugui.left(90)
wugui.forward(a)
#wugui.left(theta1/2)
i=1
while 1:
    wugui.forward(l)
    wugui.left(theta1)
    i+=1
    if i > int(180/theta1):
        break
wugui.forward(a)
wugui.forward(a)
#wugui.left(theta1/2)
i=1
while 1:
    wugui.forward(l)
    wugui.left(theta1)
    i+=1
    if i > int(180/theta1):
        break
wugui.forward(a)
wugui.penup()
wugui.goto(Rx,Ry)
wugui.pendown()
'''

R_x=[]
V_x=[]



while 1 :
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if Ry*(Ry-Vy*dt)<0:
        k=(Ry-0)/(0-(Ry-Vy*dt))
        x0=((1+k)*Rx-k*Vx*dt)/(1+k)
        R_x+=[x0]
        V_x+=[Vx]
    if quyu.inBianyuan(Rx,Ry,r,a)==1:
        #wugui.goto(Rx,Ry)
       #continue
    if quyu.inBianyuan(Rx,Ry,r,a)==0:
        #wugui.goto(Rx,Ry)
        if Rx==a:
            nx=1
            ny=0
        if Rx==-a:
            nx=-1
            ny=0
        if Ry>a:
            nx=(Rx-0)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
            ny=(Ry-a)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
        if Ry<a:
            nx=(Rx-0)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
            ny=(Ry+a)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    if quyu.inBianyuan(Rx,Ry,r,a)==-1:
        x1=Rx-Vx*dt
        y1=Ry-Vy*dt
        x2=Rx
        y2=Ry
        t=erfenbijin.Bianyuan_erFenbijin(x1,y1,x2,y2,r,a)
        Rx=t[0]
        Ry=t[1]
        #wugui.goto(Rx,Ry)
        if Rx==a:
            nx=1
            ny=0
        if Rx==-a:
            nx=-1
            ny=0
        if Ry>a:
            nx=(Rx-0)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
            ny=(Ry-a)/(Rx*Rx+(Ry-a)*(Ry-a))**(1/2)
        if Ry<a:
            nx=(Rx-0)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
            ny=(Ry+a)/(Rx*Rx+(Ry+a)*(Ry+a))**(1/2)
        t=fanshe.fanshe(Vx,Vy,nx,ny)
        Vx=t[0]
        Vy=t[1]
        #continue
    
    i+=1
    print(i)
    if i >10000:
        break

pl.plot(R_x, V_x,"o",label="V_x-R_x")
pl.title("V_x-R_x:r=200,a=10")
pl.xlabel('R_x')
pl.ylabel('V_x')
pl.legend()
pl.show()

#chuangkou.exitonclick() 