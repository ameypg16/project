# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:51:10 2016

@author: Amey P Gaikwad
"""
import matplotlib.pyplot as plt
import numpy as np
##import scipy as sc

a=[]
f=open('pandas.txt','r')                                        #the text file is opened for 'reading'
for line in f:
    a.append(float(line))
sum=0.0
for j in range(1000):
    sum=sum+a[j]                                                #the sum of the weights of all the pandas is calculated
mean=sum/1000.0                                                 #the mean is calculated                                                   
print ('Mean weight : ')                                           
print (mean)
err=0.0
for j in range (1000):
    err=err+((a[j]-mean)**2)
mean_error=np.sqrt(err/(1000.0*999.0))                          #the errors on the mean weight                    
print('Error on the mean value : ')                             #of the pandas and the estimate of error on each individual panda    
print (mean_error)                                              #is calculated sticking to the conventions and formula
error= np.sqrt(err/999.0)                                       #discussed in the class
print ('Error on the weight of each individual panda : ' )      #error on each individual weight
print (error)
"""b=[]
c=[]
for j in range(1000):
    b.append(j)
    c.append(abs(a[j]-mean))
plt.plot(b,c)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fluctuation')
print ('plot for the fluctuation in the weight of panda' )""" 
f.close()                                                       #close the text file    
plt.savefig('panda.png')                                        #save the png file    
plt.show()                                                      #shows the figure




    
