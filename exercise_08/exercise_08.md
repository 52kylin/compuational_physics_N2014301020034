# 计算物理

标签（空格分隔）： 计算物理

---

#第八次作业

##题目
**3.21**
Investigate the bifurcation diagrams found for the pendulum with other values of the drive frequency and damping parameter.(warning: this can easily become an ambitious project! 

##分析

**常微分方程：**

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/1.PNG)
</div>

**方程可改写成：**
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/2.PNG)
</div>

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/3.PNG)
</div>

**Eular_cromer method编程**

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/4.PNG)
</div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/5.PNG)
</div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/6.PNG)
</div>






##代码

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:57:06 2016

@author: Kylin
"""
import pylab as pl
import math
class pendulum:
    def __init__(self,time_step=math.pi/100,total_time=60):
        self.omiga = []
        self.xita  = []
        self.t     = []
        self.X     = []
        self.Y     = []
        self.q     = 1/2
        self.Fd    = 1.35
        self.om    = 2/3
        self.g     = 9.8
        self.l     = 9.8
        self.dt    = math.pi/100
        self.time  = total_time
        self.nsteps= int(total_time//time_step+1)
    def run(self):
        for j in range(150):
            self.Fd = 1.35+0.001*j
            self.t.append(0)
            self.xita.append(0.2)
            self.omiga.append(0)
            for i in range(120000):
                A = self.omiga[i]-(self.g/self.l*math.sin(self.xita[i])+self.q*self.omiga[i]+self.Fd*math.sin(self.om*self.t[i]))*self.dt
                self.omiga.append(A)
                B = self.xita[i]+self.omiga[i+1]*self.dt
                while B > math.pi:
                    B = B -2*math.pi
                while B <= -math.pi:
                    B = B +2*math.pi
                self.xita.append(B)
                #if self.t[i] >= 900*math.pi and self.t[i] % (3*math.pi) <= self.dt:
                if i >= 90000 and i%300 == 0 :
                    self.X.append(self.Fd)
                    self.Y.append(B)
                self.t.append(self.t[i]+self.dt)
            del self.xita[:]
            del self.omiga[:]
            del self.t[:]
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.X,self.Y,'o')
        pl.title('pendulum Fd=1.2', fontdict = font)
        pl.xlabel('Fd ($N$)')
        pl.ylabel('theta ($rad$)')
        pl.show()
a = pendulum()
a.run()
a.show_results()
print("game over")
```

##结果
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/figure_2.png)
</div>

##代码
```python
import pylab as pl
import math

"""设置初始值"""
omiga = []
xita  = []
t     = []
X     = []
Y     = []
q     = 1/2
om    = 2/3
g     = 9.8
l     = 9.8
dt    = math.pi/100
pi = math.pi
def sin(z):
    return math.sin(z)
    
"""设计主体"""
for j in range(1500):
    Fd = 0.001*j
    t.append(0)
    xita.append(0.2)
    omiga.append(0)
    for i in range(12000):
        A = omiga[i]-(g/l*sin(xita[i])+q*omiga[i]+Fd*sin(om*t[i]))*dt
        omiga.append(A)
        B = xita[i]+omiga[i+1]*dt
        while B >  pi:
            B = B -2*pi
        while B <= -pi:
            B = B +2*pi
        xita.append(B)
        t.append(t[i]+dt)
        if i >= 9000 and i % 300 == 0 :
            X.append(Fd)
            Y.append(B)
    del t[:]
    del xita[:]
    del omiga[:]
    
"""生成图像"""
pl.plot(X,Y,'o')
pl.title('pendulum Fd=1.2')
pl.xlabel('Fd ($N$)')
pl.ylabel('theta ($rad$)')
pl.xlim(1.35,1.50)
pl.ylim(0.00,pi)
pl.show()

```

##结果
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/figure_3.png)
</div>


###注：vpthon多次安装失败，可视化演示未成功完成。
