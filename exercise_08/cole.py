import pylab as pl
import math

"""设置初始值"""
omiga = []
xita  = []
t     = []
X     = []
Y     = []
q     = 1/2
om    = 2/3
g     = 9.8
l     = 9.8
dt    = math.pi/100
pi = math.pi
def sin(z):
    return math.sin(z)
    
"""设计主体"""
for j in range(150):
    Fd = 1.35 + 0.001*j
    t.append(0)
    xita.append(0.2)
    omiga.append(0)
    for i in range(12000):
        A = omiga[i]-(g/l*sin(xita[i])+q*omiga[i]+Fd*sin(om*t[i]))*dt
        omiga.append(A)
        B = xita[i]+omiga[i+1]*dt
        while B >  pi:
            B = B -2*pi
        while B <= -pi:
            B = B +2*pi
        xita.append(B)
        t.append(t[i]+dt)
        if i >= 9000 and i % 300 == 0 :
            X.append(Fd)
            Y.append(B)
    del t[:]
    del xita[:]
    del omiga[:]
    
"""生成图像"""
pl.plot(X,Y,'o')
pl.title('pendulum Fd=1.2')
pl.xlabel('Fd ($N$)')
pl.ylabel('theta ($rad$)')
pl.xlim(1.35,1.50)
pl.ylim(0.00,pi)
pl.show()
