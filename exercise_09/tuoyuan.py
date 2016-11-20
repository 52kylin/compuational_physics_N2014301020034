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
chuangkou =  turtle.Screen()                     
wugui     =  turtle.Turtle()                           
wugui.shape('circle')

a         =  200
Rx        =  (random.random()-1/2)*a
Ry        =  (random.random()-1/2)*a
V0        =  200
theta     =  random.random()*2*math.pi
dt        =  0.05
Vx        =  V0*math.cos(theta)
Vy        =  V0*math.sin(theta)


a0        =  300
b0        =  200
c0        =  ((a0)**2-(b0)**2)**(1/2)
wugui.penup()
wugui.goto(a0,0)
wugui.pendown()
for i in range(720):
    x     =  a0*math.cos(i*math.pi/360)
    y     =  b0*math.sin(i*math.pi/360)
    wugui.goto(x,y)
wugui.penup()
wugui.goto(Rx,Ry)
wugui.pendown()

#Rx        = c0
#Ry        = 0

while 1 :
    Rx    = Rx+Vx*dt
    Ry    = Ry+Vy*dt
    if (Rx/a0)**2+(Ry/b0)**2 <  1:
        wugui.goto(Rx,Ry)
        continue
    if (Rx/a0)**2+(Ry/b0)**2 == 1:
        wugui.goto(Rx,Ry)
        
        rn = ((Rx/a0**2)**2+(Ry/b0**2)**2)**(1/2)
        nx = ( Rx/a0**2)/rn
        ny = ( Ry/b0**2)/rn
        
        t  = fanshe.fanshe(Vx,Vy,nx,ny)
        Vx = t[0]
        Vy = t[1]
        continue
    if (Rx/a0)**2+(Ry/b0)**2 >  1:
        x1 = Rx-Vx*dt
        y1 = Ry-Vy*dt
        x2 = Rx
        y2 = Ry
        t  = erfenbijin.tuoyuan_erFenbijin(x1,y1,x2,y2,a0,b0)
        Rx = t[0]
        Ry = t[1]
        wugui.goto(Rx,Ry)
        
        rn = ((Rx/a0**2)**2+(Ry/b0**2)**2)**(1/2)
        nx = ( Rx/a0**2)/rn
        ny = ( Ry/b0**2)/rn
        
        t  = fanshe.fanshe(Vx,Vy,nx,ny)
        Vx = t[0]
        Vy = t[1]
        continue
    
chuangkou.exitonclick() 