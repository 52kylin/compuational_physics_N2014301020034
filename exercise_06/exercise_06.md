#exercise_06

##Exercise
***
analysis:
air resistance
General form of air resistance (Taylor expansion) 
  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi1.PNG)
</div>
 B1v comes from Stokes’s law
 B2v2 dominates for most objects
 approximate estimate of B2
 mass of air moved in time dt is mair~ρAvdt

velocity of this air is of order v, hence its energy is Eair~mairv2/2

the work done by the drag force in time dt is Fdragvdt=Eair
  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi2.PNG)
</div>
C is known as the drag coefficient 
New equation with Euler method 
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi3.PNG)
</div>

Projectile motion

Newton’s second law in two spatial dimensions 

 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi4.PNG)
</div>

Euler method for second-order ODE
write each of these second-order equations as two firest-order differential equations 
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi5.PNG)
</div>

finite difference form 

 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi7.PNG)
</div>
Resistance

the magnitude of the drag force is given by 

 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi8.PNG)
</div>

the componets of the drag force 

 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi9.PNG)
</div>

Euler method with resistance 

 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/gongshi10.PNG)
</div>

对10000米远，高100米的目标进行打击，找出能命中目标的最小初速度

没有风阻等干扰[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/edit/master/exercise_06/untitle0.py)

各种因素综合[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/edit/master/exercise_06/exercise_06.py)

##Conclusion
***
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/jieguo1.PNG)
</div>
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/jieguo2.PNG)
</div>
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/jieguo3.PNG)
</div>
 <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/jieguo4.PNG)
</div>

将运行结果产生的能击中目标的初速度和角度储存，再从中找到最小的速度：

[运行数据](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/1.txt)

[运行数据](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_06/2.txt)

没有风阻时能击中目标的最小速度为大约315米每秒

有风阻时能击中目标的最小速度为大约315米每秒

两者很接近，原因是此模型设置的参数不够合理，目标距离很近，风阻很小等


##Acknowledge
