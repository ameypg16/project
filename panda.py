# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:51:10 2016

@author: Amey P Gaikwad
"""
import matplotlib.pyplot as plt
import numpy as np
##import scipy as sc

a=[]
f=open('pandas.txt','r')
for line in f:
    a.append(float(line))
sum=0.0
for j in range(1000):
    sum=sum+a[j]
mean=sum/1000.0
print ('mean weight : ')
print (mean)
err=0.0
for j in range (1000):
    err=err+((a[j]-mean)**2)
mean_error=np.sqrt(err/(1000.0*999.0))
print('Error on the mean value : ')
print (mean_error)
error= np.sqrt(err/999.0)
print ('error on each individual panda : ' )
print (error)
b=[]
c=[]
for j in range(1000):
    b.append(j)
    c.append(abs(a[j]-mean))
plt.plot(b,c)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fluctuation')
print ('plot for the fluctuation in the weight of panda' )
plt.savefig('panda.png')

plt.show()




    