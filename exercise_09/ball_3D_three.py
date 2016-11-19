# -*- coding: utf-8 -*-
from visual import *

display(title=u"撞了南墙要回头".encode("gb2312"), width=600, height=600)

ball1 = sphere(pos=(-5,0,0), radius=0.5, color=color.red)
ball2 = sphere(pos=(-5,0,0), radius=0.5, color=color.yellow)
ball3 = sphere(pos=(-5,0,0), radius=0.5, color=color.blue)
wall_right   = box(pos=(+6,0,0), size=(0.1,12,12), color=color.green)
wall_left    = box(pos=(-6,0,0), size=(0.1,12,12), color=color.green)
wall_top     = box(pos=(0,+6,0), size=(12,0.1,12), color=color.green)
wall_bottom  = box(pos=(0,-6,0), size=(12,0.1,12), color=color.green)
wall_front   = box(pos=(0,0,+6), size=(12,12,0.1), color=color.green,opacity = 0)
wall_back    = box(pos=(0,0,-6), size=(12,12,0.1), color=color.green)

dt = 0.05
ball1.velocity = vector(6,4,3)
ball2.velocity = vector(4,2,5)
ball3.velocity = vector(8,2,3)

while True:
    rate(1/dt)
    ball1.pos = ball1.pos + ball1.velocity*dt
    if ball1.x > wall_right.x-ball1.radius or ball1.x < wall_left.x+ball1.radius:
        ball1.velocity.x *= -1
    if ball1.y > wall_top.y-ball1.radius or ball1.y < wall_bottom.y+ball1.radius:
        ball1.velocity.y *= -1
    if ball1.z > wall_front.z-ball1.radius or ball1.z < wall_back.z+ball1.radius:
        ball1.velocity.z *= -1
    ball2.pos = ball2.pos + ball2.velocity*dt
    if ball2.x > wall_right.x-ball2.radius or ball2.x < wall_left.x+ball2.radius:
        ball2.velocity.x *= -1
    if ball2.y > wall_top.y-ball2.radius or ball2.y < wall_bottom.y+ball2.radius:
        ball2.velocity.y *= -1
    if ball2.z > wall_front.z-ball2.radius or ball2.z < wall_back.z+ball2.radius:
        ball2.velocity.z *= -1
    ball3.pos = ball3.pos + ball3.velocity*dt
    if ball3.x > wall_right.x-ball3.radius or ball3.x < wall_left.x+ball3.radius:
        ball3.velocity.x *= -1
    if ball3.y > wall_top.y-ball3.radius or ball3.y < wall_bottom.y+ball3.radius:
        ball3.velocity.y *= -1
    if ball3.z > wall_front.z-ball3.radius or ball3.z < wall_back.z+ball3.radius:
        ball3.velocity.z *= -1
