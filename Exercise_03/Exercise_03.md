# Homework 3

##1.背景介绍：

通过调用延时函数实现了字符画面的移动，实现图像动起来。

##2.作业要求：

###（1）作业L1

在屏幕上让你的英文名字水平移动起来

###（2）作业L2 

在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）

##3.作业内容

###（1）作业L1：

可以使用如下语句把屏幕清理干净：

	import os
	i = os.system('cls')

字符移动可以用在每行前面增加空格的方法实现
	print("      ###")
	print("     #   ")
	print("     #   ")
	print("     #   ")
	print("      ###")
      
[作业L1源代码](https://github.com/52kylin/compuational_physics_N2014301020034/blob/master/Exercise_03/moving_my_name.py)
	import os  
	import time
	myname=["#      #   #####      #           "," #   #     #    #     #           ","  # #      #####      #           ","   #       #    #     #           ","   #       #####      #######     "]
	space=' '
	x=0
	while x<50:
		print(space*x+myname[0])
		print(space*x+myname[1])
    		print(space*x+myname[2])
    		print(space*x+myname[3])
    		print(space*x+myname[4])
    		x=x+1
    		time.sleep(0.1)
    		i = os.system('cls')

###（1）作业L2：

字符串变成列表
	a = "test"
	l = list(a)

列表变成字符串
	a = "".join(l)
	
##4.结果
##5.致谢
