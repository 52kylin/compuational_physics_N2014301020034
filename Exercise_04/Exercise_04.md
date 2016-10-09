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
  
  
    
根据题设可以解出Na和Nb的数学表达式：

  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/1.5_2.JPG)
</div>

[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/problem1.5_1.py)

[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/problem1.5_2.py)   
   
##4.结论

程序运行结果1

  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/result1.5_1.JPG)
</div>

程序运行结果2

  <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_04/result1.5_2.JPG)
</div>


##5.致谢


