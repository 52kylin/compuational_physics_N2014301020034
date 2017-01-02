import pylab as pl
import numpy as np
x,y,t,c,d,m=0,0,0,[0],[0],[0]
for i in range(1,1000000):
    a=int(np.random.uniform(0,4))
    if   a==0:
        x+=1
    elif a==1:
        x-=1
    elif a==2:
        y+=1
    else:
        y-=1
    m.append(t)
    c.append(x)
    d.append(y) 
pl.scatter(c,d,s=1)
pl.grid(True)
pl.show()
