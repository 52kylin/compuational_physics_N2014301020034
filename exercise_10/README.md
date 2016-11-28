
# exercise_10

标签（空格分隔）： 计算物理

---

###习题4.8 
>Verify Kepler's third law elliptical orbits.Run the planetary motion program with initial conditions chosen to give orbits that are noncircular Calculate T2/a3 and compare with the values given in Table 4.2

###TABLE4.2 
>Comfirmation of Kepler's third law. The results obtained using the planetary orbits program to calculate the periods of several planets.

   <div align=center>
        ![](http://oggi1a58q.bkt.clouddn.com/Table4.2.PNG)
   </div>



##正文

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:39:30 2016

@author: Kylin
"""
import math
import pylab as pl
pi = math.pi
Rx,Ry,Vx,Vy,Rr = [1],[0],[0],[2*pi],[]
dt = 0.002
T=1
n=T//dt+1
i  = 0
while 1:
    Rr += [ (Rx[i]**2+Ry[i]**2)**(1/2) ]
    Vx += [  Vx[i]-(4*pi**2*Rx[i])/(Rr[i]**3)*dt ]
    Rx += [  Rx[i]+Vx[i+1]*dt ]
    Vy += [  Vy[i]-(4*pi**2*Ry[i])/(Rr[i]**3)*dt ]
    Ry += [  Ry[i]+Vy[i+1]*dt ]
    i  += 1
    if i>=n:
        break

pl.plot(Rx,Ry,'g',label="Earth")
pl.title('')
pl.ylabel('')
pl.xlabel('')
pl.legend()
pl.show()
```
   <div align=center>
      ![](http://oggi1a58q.bkt.clouddn.com/Earth.png)
   </div>

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:39:30 2016

@author: Kylin
"""
import math
import turtle 
chuangkou = turtle.Screen()                     
wugui = turtle.Turtle()                           
wugui.shape('circle')  
wugui1 = turtle.Turtle()                           
wugui1.shape('circle')
pi = math.pi
Rx,Ry,Vx,Vy,Rr = [1],[0],[0],[2*pi],[]
dt = 0.002
wugui.penup()
wugui.goto(300*Rx[0],300*Ry[0])
wugui.pendown()
i  = 0
while 1:
    Rr += [ (Rx[i]**2+Ry[i]**2)**(1/2) ]
    Vx += [  Vx[i]-(4*pi**2*Rx[i])/(Rr[i]**3)*dt ]
    Rx += [  Rx[i]+Vx[i+1]*dt ]
    Vy += [  Vy[i]-(4*pi**2*Ry[i])/(Rr[i]**3)*dt ]
    Ry += [  Ry[i]+Vy[i+1]*dt ]
    wugui.goto(300*Rx[i+1],300*Ry[i+1])
    i  += 1
chuangkou.exitonclick() 
```
   <div align=center>
       ![](http://oggi1a58q.bkt.clouddn.com/theSolarSystem_Earth.gif)
   </div>

用以判断相同时间间隔内扫过面积大小并生成图像的程序
```python
#此文件必须命名为lineCalculate.py
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:23:22 2016

@author: Kylin
"""
import pylab as pl
def line(Y):
    X=range(len(Y))
    def sum2(M,N):
        s=0
        for i in range(len(M)):
            s=s+M[i]*N[i]
        return s
    def fangcha(M,N):
        s=0
        for i in range(len(M)):
            s=s+(M[i]-sum(M)/len(M))*(N[i]-sum(N)/len(N))
        return s/len(M)
    n=len(X)
    sumX=sum(X)
    aveX=sum(X)/len(X)
    sumX2=sum2(X,X)
    sumY=sum(Y)
    aveY=sum(Y)/len(Y)
    sumY2=sum2(Y,Y)
    sumXY=sum2(X,Y)
    X_s2=fangcha(X,X)
    Y_s2=fangcha(Y,Y)
    k =(n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
    y0=(sumY*sumX2-sumX*sumXY)/(n*sumX2-sumX*sumX)
    r =(fangcha(X,Y))/((fangcha(X,X))*(fangcha(Y,Y)))**(1/2)
    print("斜率        k   =",k)
    #print("纵坐标初值  y0   =",y0)
    print("线性相关度  r   =",r)
    #print("X总和      sumX =",sumX)
    #print("X平均值    aveX =",aveX)
    #print("X平方和    sumX2=",sumX2)
    #print("Y总和      sumY =",sumY)
    print("Y平均值    aveY =",aveY)
    #print("Y平方和    sumY2=",sumY2)
    #print("X方差      X_s2 =",X_s2)
    print("Y方差      Y_s2 =",Y_s2)
    x=X
    y=[]
    for i in range(len(x)):
        y.append(k*x[i]+y0)
    pl.plot(X,Y,'g',label="data")
    pl.plot(x,y,'r',label="line")
    pl.title('')
    pl.ylabel('')
    pl.xlabel('')
    pl.legend()
    pl.show()
```
###Earth
```python
# -*- coding: utf-8 -*-
import lineCalculate
import math
import pylab as pl
pi = math.pi
def theSolarSystem(Rx,Ry,Vx,Vy,Rr,T):
    ds=[]
    dt = 0.002
    ns = T//dt+1
    i  = 0
    while 1:
        Rr += [ (Rx[i]**2+Ry[i]**2)**(1/2) ]
        Vx += [ Vx[i]-(4*pi**2*Rx[i])/(Rr[i]**3)*dt ]
        Rx += [ Rx[i]+Vx[i+1]*dt ]
        Vy += [ Vy[i]-(4*pi**2*Ry[i])/(Rr[i]**3)*dt ]
        Ry += [ Ry[i]+Vy[i+1]*dt ]
        if i >= 2:
            ds += [ 0.5*abs(Rx[i]*Ry[i+1]-Rx[i+1]*Ry[i]) ]
        i  += 1
        if i>ns:
            break
    a=(max(Rx)-min(Rx))/2
    b=(max(Ry)-min(Ry))/2
    e=(1-(b/a)**2)**(1/2)
    k=T**2/a**3
    return k,a,b,e,ds,Rx,Ry
Rx,Ry,Vx,Vy,Rr,T = [1],[0],[0],[2*math.pi],[],1
planet = theSolarSystem(Rx,Ry,Vx,Vy,Rr,T)
print("T^2/a^3=",planet[1])
lineCalculate.line(planet[4])
x,y=planet[5],planet[6]
pl.plot(x,y)
pl.xlabel("x(AU)")
pl.ylabel("y(AU)")
#pl.legend()
pl.show()
```
   <div align=center>
   ![](http://oggi1a58q.bkt.clouddn.com/Earth_1.PNG)
   
   结果显示：T^2/a^3=1.00004
   
   ![](http://oggi1a58q.bkt.clouddn.com/Earth_2.PNG)
   
   此图及上图中数据的方差可以得出相同时间间隔内扫过面积相等
   
   ![](http://oggi1a58q.bkt.clouddn.com/Earth_3.PNG)
   
   此图显示地球轨道为椭圆
   </div>

