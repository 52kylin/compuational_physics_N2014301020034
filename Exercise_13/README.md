
[TOC]

#摘要

在本篇文章中，我将波动方程和中央采用一端固定条件研究高斯波包演化，三角波和方波包的包。另外，我比较R = 1.2和R = 0.8的结果之间的差异，我发现R = 1.2结果大幅偏离随着时间的推移和R = 0.8可使结果相对稳定。

#背景

波动方程
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.1.JPG )
</div>
这通常被称为波动方程，这个方程出现在许多情况下，包括在字符串中，波的电磁波，在湖面波和声波。虽然我们的方法和结论也适用于其它条件一样，在这里，我们将使用一个适当的语言对一个字符串的波。
从弦上的波浪运动中推导出方程是没有用的，下面的图说明了线段上的力.。
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.2.JPG )
</div>
根据牛顿第二定律：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.3.JPG )
</div>
然后使用有限差分近似的角度：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.4.JPG )
</div>从而有：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.5.JPG )
</div>
我们的主要目标是开发了一种数值方法求解（6.1）。我们终于可以得到这种方法：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.6.JPG )
</div>

此处![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/13.7.JPG )

由于我们的算法只需要的电流值，在以前的时间步长值，因此我们只需要三的时间指标值。我们让Y1对应Y在以前的时间步长，对应于Y Y2和Y3在当前时间步对应于Y在下一时间步骤。在每次迭代之后，我们得到的值Y1 Y2 Y2 Y3的价值得到实现的价值观的更新。

#内容
编写如下代码：
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 23:17:04 2016

@author: Kylin
"""

from math import*
from matplotlib.pyplot import*

y1,y2,y3,x,X,Y=[],[],[],[],[],[]
for i in range(1000):
    y1 += [ 0.1*exp(-(0.03*i-5)**2) ]
    y2 += [ 0.1*exp(-(0.03*i-5)**2) ]
    y3 += [ 0.1*exp(-(0.03*i-5)**2) ]
    x  += [ i ]

def run(t):
    for i in range(t):
        for j in range(1,999):
            y3[j]=-y1[j]+y2[j+1]+y2[j-1]
        for k in range(1000):
            y1[k]=y2[k]
            y2[k]=y3[k]
    X.append(x);Y.append(y3)

for i in range(5):
    m=260+i*5
    n=511+i*1
    run(m)
    p1=subplot(n)
    p1.plot(X[i],Y[i],'k')
    p1.set_ylabel('Amplitude')
show()
```

运行结果：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/figure_3.png )
</div>
编写如下代码：
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 23:52:55 2016

@author: Kylin
"""

from math import*
from matplotlib.pyplot import*


class run():
    def __init__(self,r=1.2):
        self.r=r
        self.y1=[]
        self.y2=[]
        self.y3=[]
        self.x=[]
        self.X=[]
        self.Y=[]
        
        for i in range(1000):
            if i < 500:
                self.y1 += [0.01*i]
                self.y2 += [0.01*i]
                self.y3 += [0.01*i]
            else:
                self.y1 += [10-0.01*i]
                self.y2 += [10-0.01*i]
                self.y3 += [10-0.01*i]
            self.x += [i]

    def calcu(self,t):
        for i in range(t):
            for j in range(1,999):
                self.y3[j]=2*(1-r**2)*self.y2[j]-self.y1[j]+(self.y2[j+1]+self.y2[j-1])*r**2
            for k in range(1000):
                self.y1[k]=self.y2[k]
                self.y2[k]=self.y3[k]
        self.X.append(self.x);self.Y.append(self.y3)
        
    def show(self):
        for i in range(5):
            m=i*50
            n=511+i
            b=run()
            b.calcu(t=m)
            p1=subplot(n)
            p1.plot(self.X[i],self.Y[i],'k')
            p1.set_ylabel('Amplitude')
        show()
a=run()
a.show()
```
运行结果：

   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/figure_4.png )
</div>

将r改成1.2：
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/figure_5.png )
</div>



[俩行波叠加：](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Code/code.py)
   <div align=center>
    ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_13/Picture/figure_0.gif )
</div>
