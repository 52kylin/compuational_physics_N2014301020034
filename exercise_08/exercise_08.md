# 计算物理

标签（空格分隔）： 计算物理

---

#第八次作业

##题目
**3.20**
calculate the bifurcation diagram for the pendulum in the     vicinity of F<sub>D</sub>=1.35 to 1.5. Make a magnified a plot of the diagram (as compare to figure 3.11) and obtain an estimate of the Feigenbaum parameter.

##分析
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
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_08/figure_1.png)
</div>
