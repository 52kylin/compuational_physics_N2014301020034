



```python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:39:23 2016

@author: Kylin
"""
import random
import pylab as pl
n=100
X=[0]*n
x2=[0]
x=0
for i in range(n):
    r=random.randrange(0,2)
    if r == 0:
        dx =-1
    if r == 1:
        dx = 1
    x = x + dx
    X[i] = x
    if i < n-1:
        x2 += [x2[-1]+x*x]
for i in range(len(x2)):
    if i==0:
        x2[i]=x2[i]
    if i>=1:
        x2[i]=x2[i]/i
t = range(n)
pl.plot(t,X,'o',label='$x$ versus time')
pl.legend(frameon=True)
pl.show()
pl.plot(t,x2,label='$<x^2>$ versus time')
pl.plot(t,t)
pl.legend(frameon=True)
pl.show()
```
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_6.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_7.png)






```python
import pylab as pl
import numpy as np
x,y,t,c,d,m=0,0,0,[0],[0],[0]
for i in range(1,1000):
    a=int(np.random.uniform(0,4))
    if   a==0:
        x+=1
    elif a==1:
        x-=1
    elif a==2:
        y+=1
    else:
        y-=1
    m.append(t)
    c.append(x)
    d.append(y) 
pl.scatter(c,d,s=1)
pl.grid(True)
pl.show()
```

1000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_4.png)

10000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_3.png)

100000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_2.png)

1000000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_1.png)
