# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
import turtle                                      
import random
chuangkou = turtle.Screen()                     
wugui = turtle.Turtle()                           
wugui.shape('turtle')                             
a=200
Rx    = (random.random()-1/2)*2*a
Ry    = (random.random()-1/2)*2*a
V0    = 100*random.random()
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

while 1 :
    """在框框内运动不受限制"""
    Rx=Rx+Vx*dt
    Ry=Ry+Vy*dt
    if Rx <= a and Rx >= -a and Ry <= a and Ry >= -a:
        wugui.goto(Rx,Ry)
        
    if (Rx == a or Rx == -a) and Ry < a and Ry > -a : #x=a边界
        Vx = -Vx
        Vy =  Vy
        continue
    '''
    if Rx == -a and Ry < a and Ry > -a : #x=-a边界
        Vx = -Vx
        Vy =  Vy
        continue
    '''
    if (Ry == a or Ry == -a) and Rx < a and Rx > -a : #y=a边界
        Vx =  Vx
        Vy = -Vy
        continue
    '''
    if Ry == -a and Rx < a and Rx > -a : #y=-a边界
        Vx =  Vx
        Vy = -Vy
        continue
    '''
    if (Rx==a and Ry==a) or (Rx==-a and Ry==a) or (Rx==a and Ry==-a) or(Rx==-a and Ry==-a):
        Vx = -Vx
        Vy = -Vy
        continue
    
    if Rx > a:
        K  = (Rx-a)/(a-(Rx-Vx*dt))
        Y  = ((1+K)*Ry-K*Vy*dt)/(1+K)
        if Y > a:
            k  =  (Ry-a)/(a-(Ry-Vy*dt))
            x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
            Rx =  x0
            Ry =  a
            wugui.goto(Rx,Ry)
            Vx =  Vx
            Vy = -Vy
            continue
        if Y > -a and Y < a:
            k  = (Rx-a)/(a-(Rx-Vx*dt))
            y0 = ((1+k)*Ry-k*Vy*dt)/(1+k)
            Rx =  a
            Ry =  y0
            wugui.goto(Rx,Ry)
            Vx = -Vx
            Vy =  Vy
            continue
        if Y < -a:
            k  =  (Ry+a)/(-a-(Ry-Vy*dt))
            x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
            Rx =  x0
            Ry =  -a
            wugui.goto(Rx,Ry)
            Vx =  Vx
            Vy = -Vy
            continue
    if Rx < -a:
        K  = (Rx+a)/(-a-(Rx-Vx*dt))
        Y  = ((1+K)*Ry-K*Vy*dt)/(1+K)
        if Y > a:
            k  =  (Ry-a)/(a-(Ry-Vy*dt))
            x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
            Rx =  x0
            Ry =  a
            wugui.goto(Rx,Ry)
            Vx =  Vx
            Vy = -Vy
            continue
        if Y > -a and Y < a:
            k  = (Rx+a)/(-a-(Rx-Vx*dt))
            y0 = ((1+k)*Ry-k*Vy*dt)/(1+k)
            Rx = -a
            Ry = y0
            wugui.goto(Rx,Ry)
            Vx = -Vx
            Vy =  Vy
            continue
        if Y < -a:
            k  =  (Ry+a)/(-a-(Ry-Vy*dt))
            x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
            Rx =  x0
            Ry =  -a
            wugui.goto(Rx,Ry)
            Vx =  Vx
            Vy = -Vy
            continue
    if Ry > a and Rx < a and Rx > -a:
        k  =  (Ry-a)/(a-(Ry-Vy*dt))
        x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
        Rx =  x0
        Ry =  a
        wugui.goto(Rx,Ry)
        Vx =  Vx
        Vy = -Vy
        continue
    if Ry < -a and Rx < a and Rx > -a:
        k  =  (Ry+a)/(-a-(Ry-Vy*dt))
        x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
        Rx =  x0
        Ry =  -a
        wugui.goto(Rx,Ry)
        Vx =  Vx
        Vy = -Vy
        continue
    '''    
    if Rx >  a and Ry < a and Ry > -a: #x=a边界
        k  = (Rx-a)/(a-(Rx-Vx*dt))
        y0 = ((1+k)*Ry-k*Vy*dt)/(1+k)
        Rx =  a
        Ry =  y0
        wugui.goto(Rx,Ry)
        Vx = -Vx
        Vy =  Vy
        continue
    if Rx < -a and Ry < a and Ry > -a: #x=-a边界
        k  = (Rx+a)/(-a-(Rx-Vx*dt))
        y0 = ((1+k)*Ry-k*Vy*dt)/(1+k)
        Rx = -a
        Ry = y0
        wugui.goto(Rx,Ry)
        Vx = -Vx
        Vy =  Vy
        continue
    if Ry > a and Rx < a and Rx > -a: #y=a边界
        k  =  (Ry-a)/(a-(Ry-Vy*dt))
        x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
        Rx =  x0
        Ry =  a
        wugui.goto(Rx,Ry)
        Vx =  Vx
        Vy = -Vy
        continue
    if Ry < -a and Rx < a and Rx > -a: #y=-a边界
        k  =  (Ry+a)/(-a-(Ry-Vy*dt))
        x0 =  ((1+k)*Rx-k*Vx*dt)/(1+k)
        Rx =  x0
        Ry =  -a
        wugui.goto(Rx,Ry)
        Vx =  Vx
        Vy = -Vy
        continue
    '''
chuangkou.exitonclick() 