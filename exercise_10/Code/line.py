# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:23:22 2016

@author: Kylin
"""
import pylab as pl
def line(Y):
    X=[]
    for i in range(len(Y)):
        X+=[i]
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
    print("纵坐标初值  y0   =",y0)
    print("线性相关度  r   =",r)
    print("X总和      sumX =",sumX)
    print("X平均值    aveX =",aveX)
    print("X平方和    sumX2=",sumX2)
    print("Y总和      sumY =",sumY)
    print("Y平均值    aveY =",aveY)
    print("Y平方和    sumY2=",sumY2)
    print("X方差      X_s2 =",X_s2)
    print("Y方差      Y_s2 =",Y_s2)
    x=X
    y=[]
    for i in range(len(x)):
        y.append(k*x[i]+y0)
    pl.plot(X,Y,'go',label="data")
    pl.plot(x,y,'r',label="line")
    pl.title('')
    pl.ylabel('')
    pl.xlabel('')
    pl.legend()
    pl.show()
