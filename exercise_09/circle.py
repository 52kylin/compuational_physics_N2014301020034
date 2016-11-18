# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:54:38 2016

@author: Kylin
"""
import math                                    
import turtle                                      

chuangkou = turtle.Screen()                     
wugui = turtle.Turtle()                           
wugui.shape('turtle')                             

theta = 1
r = 256
l = 2*r*math.sin(theta/2*math.pi/180)

wugui.penup()
wugui.forward(r)
wugui.left(90+theta/2)
wugui.pendown()


i=0
while 1:
    wugui.forward(l)
    wugui.left(theta)
    i+=1
    if i > int(360/theta):
        break
    
omega = 10
s = 2*r*math.cos(omega/2*math.pi/180)

wugui.left(90-theta/2-omega/2)

i=1
while i<= int(360/omega):
    wugui.forward(s)
    wugui.left(180-omega)
    i+=1

chuangkou.exitonclick() 
