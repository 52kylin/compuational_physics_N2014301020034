
##习题5.7 
Write two programs to solve the capacitor problem of Figure 5.6 and 5.7, one 
using Jacobi method and one using simultaneous over relaxation (SOR) algrithem . For a fixed accuracy
compare the number of iterations,N<sub>iter</sub>, that 
each algrithm requires as a function of the number of grid elements, L. Show 
that for Jacobi method N<sub>iter</sub>~L<sup>2</sup>, while with SOR N<sub>iter</sub>~L .

##摘要
在这个练习中，我们采用两种方法解决电容器的问题，一个是雅可比的方法，而另一个是SOR算法。

##背景
等电位线和电场
等势线提供二维查看电位的定量方法。
在一个给定的线的每一个点是在相同的电位。
这样的地图可以被认为是地形图。
例如，考虑在Rawah荒野地图右边。
在同一条直线上所有的点都在同一海拔高度，
就像在同一等势线的所有点都在同一电压。
水总是向下流动，因此河流总是垂直于线路上的地形图，
类似于电场线总是垂直于等势线的方式。当线紧密，坡陡，如悬崖，
只是接近表明强电场等势线。湖泊处于同一高度，在同一方向上的导体是相同的电位。


##内容
###分析
正如我们所知，电位满足拉普拉斯方程的空间中，没有任何电荷！
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E1.PNG)
</div>
数值上，我们得到的：
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E2.PNG)
</div>
特别是，对于2维的情况下：
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E3.PNG)
</div>
雅可比的方法

如果我们只使用旧的潜力来计算新的，公式成为：
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E4.PNG)
</div>
SOR算法

显然，我们可以利用新的价值观，因为他们成为可用，这意味着：
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E5.PNG)
</div>
然后，我们可以考虑
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E6.PNG)
</div>
为改变推荐由高斯赛德尔算法。然而，这个选择太保守了。因此，为了加快收敛，我们将改变他潜在的更大的金额计算根据
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/E7.PNG)
</div>
这就是我们所谓的SOR算法。一般来说，我们设置的Dirichlet边界条件。
   <div align=center>
   ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/figure_2.png)
   </div>
   <div align=center>
   ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/figure_3.png)
   </div>

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 01:39:23 2016

@author: Kylin
"""

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

global error
error=1e-5
def method_Jacobi(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0
    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0
    V=[]
    V += [v]
    s=0
    while 1:
        V += [v]
        for i in range(1,L-1):
            for j in range(1,L-1):
                V[s+1][i][j]=(V[s][i+1][j]+V[s][i-1][j]+V[s][i][j+1]+V[s][i][j-1])/4.0
        for i in [x]:
            for j in range(x,y+1):
                V[s+1][j][i]=1.0
        for i in [y]:
            for j in range(x,y+1):
                V[s+1][j][i]=-1.0
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
def method_GS(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0

    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0   
    V=[]
    V+=[V]
    s=0
    while 1:
        V+=[V]
        for i in range(1,L-1):
            for j in range(1,L-1):
                V[s+1][i][j]=(V[s][i+1][j]+V[s+1][i-1][j]+V[s][i][j+1]+V[s+1][i][j-1])/4.0
        for i in [x]:
            for j in range(x,y+1):
                V[s+1][j][i]=1.0
        for i in [y]:
            for j in range(x,y+1):
                V[s+1][j][i]=-1.0
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
def method_SOR(L):
    v=[0]*L
    v=[v]*L
    x=int(2*(L-1)/5)
    y=int(3*(L-1)/5)
    for i in [x]:
        for j in range(x,y+1):
            v[j][i]=1.0

    for i in [y]:
        for j in range(x,y+1):
            v[j][i]=-1.0   
    V=[]
    V+=[V]
    alpha=2.0/(1+pi/L)
    s=0
    while 1:
        V+=[V]
        for i in range(1,L-1):
            for j in range(1,L-1):               
                V[s+1][j][i]=(V[s][j+1][i]+V[s+1][j-1][i]+V[s][j][i+1]+V[s+1][j][i-1])/4.0
                if i==a and j>a-1 and j<b+1:
                    V[s+1][j][i]=1.0
                if i==b and j>a-1 and j<b+1:
                    V[s+1][j][i]=-1.0
                V[s+1][j][i]=alpha*(V[s+1][j][i]-V[s][j][i])+V[s][j][i] 
        V[s]=np.array(V[s])
        V[s+1]=np.array(V[s+1])
        DV=V[s+1]-V[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                 dV=dV+abs(DV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>1:
            break
    return s
L    = []
M    = []
N    = []
O    = []
f=open('data_of_problem5.7.txt','w')
for i in range(6,61,5):
    J=method_Jacobi(i)
    G=method_GS(i)
    S=method_SOR(i)
    L    += [i]
    M    += [J]
    N    += [G]
    O    += [S]
f.close()
plot(L,M)
plot(L,N)
plot(L,O)
scatter(L,M)
scatter(L,N)
scatter(L,O)
legend(('Jacobi method','GS method','SOR  method'))
title('3 different methods')
xlabel('L')
ylim(0,1000)
ylabel('N')
savefig('methods.png')
show()
```
   <div align=center>
   ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/figure_1.png)
   </div>
   <div align=center>
   ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/figure_4.png)
   </div>
   <div align=center>
   ![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_12/picture/figure_5.png)
   </div>



##结论
有一个雅可比的方法更快的收敛速度比为SOR算法解决电容器的问题。
更重要的是，对于雅可比的方法近似的；而与SOR。
