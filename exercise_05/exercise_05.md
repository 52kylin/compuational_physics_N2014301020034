# Exercise_05

##1.摘要

模拟炮弹的飞行过程，比较有空气阻力和没有空气阻力两种情况

##2.背景

完成习题2.6

2.6 Use the Euler method to calculate cannon shell trajettories ignoring both air drag and the ffect of air density (actually,ignoring the former automatically rules out the latter).Compare your rresults with those in Figure 2.4,and with the exact solution

##3.正文

根据条件，写出牛顿力学的表达式：

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/5_1.PNG)
</div>

据此写出没有空气阻力时的Euler方法的表达式：

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/5_2.PNG)
</div>

由于空气阻力与速度的二次方成正比：

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/5_3.PNG)
</div>

据此写出有空气阻力时的Euler方法的表达式：

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/5_4.PNG)
</div>

根据上述Euller表达式编写程序模拟炮弹的飞行g轨迹：
[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/exercise_05.py)

##4.结论

程序运行的结果：

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_05/figure_2.png)
</div>

从图中可以看出，没有空气阻力时，炮弹飞的更高更远

##5.致谢

