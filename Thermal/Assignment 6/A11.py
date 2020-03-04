# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:01:49 2019

@author: maxhu
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

def psi1(x,a):
    return a * np.sin(x)

def psi2(x,b):
    return b * np.sin(2*x) 

x_start = -10
x_end = 10
num = 2000

x = np.linspace(x_start,x_end,num)

fig = plt.figure(1,figsize=(40,10))

fig.add_subplot(1,3,1)
plt.plot(x, psi1(x,1)+psi2(x,2), color='black', label='$Q_1$', linestyle = '-')
plt.legend(loc='upper right')

plt.subplot(1,3,3)
plt.plot(x, psi1(x,3)+psi2(x,8), color='black', label='$Q_3$', linestyle = '-')
plt.legend(loc='upper right')

plt.subplot(1,3,2)
plt.plot(x, psi1(x,20)+psi2(x,9), color='black', label='$Q_2$', linestyle = '-')
plt.legend(loc='upper right')

plt.savefig('A11.png', dpi=300)

