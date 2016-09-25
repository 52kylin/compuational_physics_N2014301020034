import time
import os

a=("############\n")
b=("############")
c=("            \n")
d=("            ")
li0=[2*d+a,d+2*b+a,b+d+b+d+a,2*d+a,2*d+a]
li1=[2*d+a,3*d+a,4*b+a,3*d+a,2*d+a]
li2=[2*d+a,2*d+a,b+d+b+d+a,d+2*b+a,2*d+a]
li3=[2*d+a,d+a,4*b+a,d+a,2*d+a]


i=0
while i<5:
    j=0
    while j<16:
        print(li0[i])
        j=j+1
    i=i+1
time.sleep(1)
os.system('cls')

k=0
while k<5:
    j=0
    while j<16:
        print(li1[k])
        j=j+1
    k=k+1
time.sleep(1)
os.system('cls')

l=0
while l<5:
    j=0
    while j<16:
        print(li2[l])
        j=j+1
    l=l+1
time.sleep(1)
os.system('cls')

m=0
while m<5:
    j=0
    while j<16:
        print(li3[i])
        j=j+1
    m=m+1
time.sleep(1)
os.system('cls')
