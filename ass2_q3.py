# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 01:09:42 2016

@author: Amey P Gaikwad
"""

import matplotlib.pyplot as plt
import numpy as np

f=open('linear1.txt','r')                                                                  #open the file     
temp=[]                                                                                    #stores the temperatures             
i=0                                             
for line in f:
    temp.append(float(line))
    i+=1
##print (i)
g=open('linear2.txt','r')                                                                  #opens the second file containing the lengths                 
length=[]                                                                                  #stores the lengths of the rod                             
j=0
for line in g:
    length.append(float(line))
    j+=1
##print (j)
plt.figure(1)                                                                              #in figure 1 subplot the scatter plot has been plotted             
plt.subplot(211)
plt.scatter(temp,length,marker='o')
plt.xlabel('Temperature')
plt.ylabel('Length')
plt.title('Scatter Plot')
plt.savefig('a_scatter.png')                                                                  #scatter plot of temperrature vs the length of the rod at that temperature 
plt.figure(2)                                                                              #in figure 2 the best fit line is plotted using pythons inbuilt function 
plt.plot(np.unique(temp), np.poly1d(np.polyfit(temp, length, 1))(np.unique(temp)),'r')
plt.title('Python algorithm')
plt.xlabel('Temperature')
plt.ylabel('Length')
plt.savefig('b_inbuilt.png')
length_bar=np.sum(length)/50.0                                                             #algorithm for the calculation     
temp_bar=np.sum(temp)/50.0                                                                 #of the best estimates for the slope                      
slope_num=np.sum([length[z]*temp[z] for z in range(50)])-50.0*length_bar*temp_bar          #and the intercept  of the 
slope_denom=np.sum([temp[w]**2 for w in range(50)])-50.0*temp_bar**2                       #best fit line for the 
slope=slope_num/slope_denom                                                                #scatter plot obtained above
intercept=length_bar-slope*temp_bar
y=[]
for r in range(50):
    y.append(intercept+slope*temp[r])
plt.figure(3)                                                                              #figure 3 subplot has been used for plotting the best fit line obtained from the above algorithm             
plt.plot(temp,y,'b')
plt.title('Customised algorithm')
plt.xlabel('Temperature')
plt.ylabel('Length')
plt.savefig('c_customised.png')
plt.figure(4)                                                                              #scatter plt along with the best fit line has been plotted in figure 4 subplot 
plt.scatter(temp,length,marker='o')
plt.plot(temp,y,'b')
plt.title('Scatter plot along with the best fit line from customised algorithm' )
plt.xlabel('Temperature')
plt.ylabel('Length')
print('Best estimate for the length of the rod at 0 degrees celsius')                      #the required calculations are done and printed 
print (intercept)
print('Coefficient of linear expansion in mm/Kelvin')
print (slope)
print('Assuming linear extrapolation , length of rod at 15 degrees' )
print (intercept+slope*15)
error=np.sqrt(np.sum([(length[t]-y[t])**2 for t in range(50)])/48.0)                       #error on the length at 15 degrees is calculated using the readings and the best fit line which is extrapolated upto 15 degrees      
print ('Error \n' , error)
"""arr=[]
a=[]
b=[]
for k in range(0,1000):
    a.append(950+np.random.random_sample(100))
    b.append(np.random.random_sample(1))

for m in range(1000):
    su=0
    for l in range(50):
        su=su+((length[l]-(a[m]+b[m]*temp[l]))**2)
    arr.append(su)
print(arr[0]) 
q=0
for i in arr[0]:
    q+=1
print (q)
mi=arr[0]
ind=0
for f in range(1000):
    if(mi>arr[f]):
        mi=arr[f]
        ind=f
index=ind
##print(q)
y=[]
###print (a[index])
for h in range():
    
    y.append(a[index]+b[index]*temp[h])
plt.plot(temp,y,'r')"""
f.close()                                                                                    #close the text files                       
g.close()
plt.savefig('d_final.png')                                                                   #saves the figure   
plt.show()                                                                                   #shows the graph                       
