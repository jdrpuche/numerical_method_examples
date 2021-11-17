# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:04:23 2021

@author: jesus
"""
import numpy as np 
from matplotlib import pyplot as plt 
#defining euler's method

def euler(f,y0,t):
    y=np.zeros(len(t))
    
    y[0]=y0
    
    for k in range (len(t)-1):
        y[k+1]=y[k]+f(y[k],t[k])*(t[k+1]-t[k])
    
    return y

#testing 

t = np.linspace(0,2,50)
y0 = 1
f = lambda y,t: y

y_sim=euler(f,y0,t)

y_true=np.exp(t)

plt.plot(t,y_sim,'b.-',t,y_true,'r-')
plt.legend(['Euler','True'])
plt.axis([0,2,0,9])
plt.grid(True)
plt.title("Solution of $y'=y , y(0)=1$")
plt.show()
    