#随即系统：
##1.摘要：

随机过程是随机变量的集合，代表随时间变化的随机值系统.。这是一个确定性过程（确定性系统）的概率对应。而不是描述这一过程只能在一个方向进化（如，例如，对一个常微分方程的解），在一个随机的或随机的过程中，有一些不确定性：即使初始条件（或出发点）是已知的，有几个（通常是无限多的）在这过程中可能的发展方向。
本文主要讨论了随机系统的基本行为，探索随机系统和扩散过程的关系。做一点挖到二维Ising模型。
##2.关键字：

随机系统，扩散

##3.随机游走
###3.1分析

首先，我们应该讨论最简单也是最基本的例子，随机系统的一维随机游走。
随机游走的起源开始，而第一步是随机选择在左侧或右侧，各有0.5的概率。然后下一步选择的概率，左或右都是0.5的概率。我们将经常提到游走的位置作为时间的函数.。
在一个物理过程，如分子在溶液中的运动，步骤之间的时间大约是一个常数，所以步骤数大致成正比的时间。因此，我们将经常提到游走的位置作为时间的函数.。
一个更有趣和信息量是N个步骤后的位移的平方的平均值。这个数量的一些结果显示在上面的数字右边。我们看到他们是由一个直线，这是很好的描述：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_01.png)

其中t是时间，这里等于阶数；因子D称为扩散常数。5将这个结果与自由粒子的行为相比较，也就是说，它是以恒定速度移动的，不受其他粒子碰撞的阻碍.。对于这样一个粒子，我们知道C = VT，所以从原点的距离（起点）随时间线性增长。随机游走者的行为不同；根据（1）它的均方根
距离原点仅增长。因此，一个随机游走逃离原点比自由粒子慢得多。
这种运动可以扩展到扩散过程。

###3.2程序

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
###3.3结果
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
