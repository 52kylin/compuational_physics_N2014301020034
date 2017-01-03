#随机系统：
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

##4.扩散过程
###4.1分析
一种方法来描述相同的物理涉及的颗粒的密度，它可以方便地定义，如果该系统包含大量的粒子。为粗粒化，是考虑的空间区域，大到足以容纳大量的颗粒，密度（=质量/体积）地定义。的密度，然后每单位时间的单位体积的概率，表示由z，t），找到一个粒子在（t，y，z）在时间t，因此，P和P服从相同的方程。要找到这个方程，我们专注于个人随机游走。我们假设它被限制在一个简单的立方晶格上采取步骤，它使一个“步”每一个时间步长。P（I，j，k，n）是在时间N（，j，k）的粒子的概率，因为我们是在一个简单的立方晶格，有6个不同的最近邻站点。如果沃克是在这些网站上的时间N - 1，有一个概率为1 / 6，然后将移动到站点（I，j，K）在时间N，因此，总概率到达（I，j，K）是：
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_02.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_03.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_04.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_05.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_06.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_07.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_08.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_09.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_010.png)
###4.2程序
```python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:12:22 2016
@author: Kylin
"""
import pylab as plt
import numpy as np 
N=101
dx=2./(N-1)
dt=0.1
D=1./4*(dx**2)/dt
class diffusion:
 	def __init__(self,step):
 		self.step=step
 		self.x=np.linspace(-1,1,N)
 		self.y=np.linspace(0,0,N)
 		self.Y=np.linspace(0,0,N)
 		self.y[50]=1
 	def run(self):
 		for i in range(N):
 			self.Y[i]=self.y[i]
 		for i in range(1,N-1):
 			self.y[i]=self.Y[i]+D*dt/(dx**2)*(self.Y[i+1]+self.Y[i-1]-2*self.Y[i])
 	def show(self):
 		for i in range(self.step):
 			self.run()
 			i+=1
 		plt.plot(self.x,self.y,label="step="+str(self.step))
for i in range(4):
    i=(i+1)
    A=diffusion(10**i)
    A.show()
plt.legend(loc="best")
plt.show()
```

###4.3结果

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_5.png)



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

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_011.png)
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_012.png)

1000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_4.png)

10000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_3.png)

100000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_2.png)

1000000步：

![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/final_exam/Picture/figure_1.png)
