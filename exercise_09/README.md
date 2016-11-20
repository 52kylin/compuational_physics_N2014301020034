#第九次作业


**部分程序需要将必要的python文件放在同一文件夹下才能运行**

##一 边界的处理


**用二分法处理边界【以正方形为例（不考虑球的半径，若要考虑，则减去球的半径即可）】**
###1，首先划分区域：
- 内部为 1
- 边界为 0
- 外部为-1
```python
def inZhengfangxing(x,y,a):
    if x > -a and x < a and y > -a and y < a :
        return 1
    if ( x ==  a and y >= -a and y <= a ) \
    or ( x == -a and y >= -a and y <= a ) \
    or ( y ==  a and x >= -a and x <= a ) \
    or ( y == -a and x >= -a and x <= a ) :
        return 0
    else:
        return -1
```

###2，通过取中点的办法逼近边界

(x1,y1)在正方形内部，(x2,y2)在正方形外部
```python
def Zhengfangxing_erFenbijin(x1,y1,x2,y2,r,a):
    x0=0
    y0=0
    while 1 :
        x0=(x1+x2)/2
        y0=(y1+y2)/2
        if inZhengfangxing(x0,y0,a) ==  1:
            x1=x0
            y1=y0
            continue
        if inZhengfangxing(x0,y0,a) == -1:
            x2=x0
            y2=y0
            continue
        if inZhengfangxing(x0,y0,a) ==  0:
            break  
    return [x0,y0]
```
返回值(x0,y0)在边界上




##二 平面碰撞演示

**正方形区域**
[[源代码1.0版本](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/fantan_zhengfangxing_old.py)]
[[源代码2.0版本](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/fantan_zhengfangxing_new.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/zfxquyu.gif)
   </div>




**圆形区域**
[[源代码1.0版本](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/circle.py)]
[[源代码2.0版本](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/fantan_yuan.py)]

   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/turtle.gif)
   </div>


**破缺圆**
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/fantan_poqueyuan.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/poqueyuan.gif)
   </div>


*椭圆区域*
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/tuoyuan.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/tuoyuan.gif)
   </div>

##三 速度位置关系

[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/poYuan.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_1.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_2.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_3.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_4.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_5.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_6.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_7.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_8.png)
   </div>
显然，a/r>=0.1时出先混沌现象

部分椭圆的v-x图像
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_10.png)
   </div>
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/figure_11.png)
   </div>



##四 vpython演示
一维碰撞
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_1D.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_1D.gif)
   </div>
二维碰撞
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_2D.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_2D.gif)
   </div>
三维碰撞
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_3D.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_3D.gif)
   </div>
三维碰撞多球
[[源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_3D_three.py)]
   <div align=center>
![](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/exercise_09/ball_3D_three.gif)
   </div>


**经过多次尝试章终于通过安装[python(xy)](http://www.softpedia.com/get/Programming/Other-Programming-Files/Python-x-y.shtm)成功安装vpython并实现动画演示**
