# -*- coding: utf-8 -*-
from visual import *

display(title=u"撞了南墙要回头".encode("gb2312"), width=600, height=600)

ball1 = sphere(pos=(-5,0,0), radius=0.5, color=color.red)
wall_right   = box(pos=(+6,0,0), size=(0.1,12,12), color=color.green)
wall_left    = box(pos=(-6,0,0), size=(0.1,12,12), color=color.green)

dt = 0.05
ball1.velocity = vector(6,0,0)

while True:
    rate(1/dt)
    ball1.pos = ball1.pos + ball1.velocity*dt
    if ball1.x > wall_right.x-ball1.radius or ball1.x < wall_left.x+ball1.radius:
        ball1.velocity.x *= -1

