# Exercise_04:The decay of two kinds of particles

##1.摘要

完成习题1.5
  
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are
  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/1.5_1.JPG)
</div>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , . Solve the system of equations for the numbers of nuclei, and , as functions of time. Consider different initial confitions, such as , , etc., and take s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which and are constant. In such a steady state, the time derivatives and should vanish.

##2.背景介绍

  解决1章放射性衰变和测试程序的问题后，我们可以使用Python，matplotlib和数学的欧拉方法制定出一个通用的解决这类问题。

##3.正文
  
现编一个程序模拟衰变过程A和B两种原子数量的变化过程
[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/problem1.5_1.py)


下面的程序是两种计算方法的比较
[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/problem1.5_2.py)   
   
##4.结论

程序运行结果1

  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/result1.5_1.JPG)
</div>
从结果来看，两种原子，A原子逐渐减少，B原子逐渐增加，最后处于稳定


程序运行结果2

  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/result1.5_2.JPG)
</div>
两种方法有差别，偏差来自高阶小量的舍弃与否

##5.致谢


