# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 03:30:36 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

def y(x,t):
    return 5*np.cos(6*t-3*x)
 
x_start = .1
x_end = 10
num = 2000

displacement = np.linspace(x_start,x_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)

plt.plot(displacement, y(displacement,1), color='purple', label='t=1', linestyle = '-')
plt.plot(displacement, y(displacement,2), color='green', label='t=2', linestyle = '--')
plt.plot(displacement, y(displacement,3), color='b', label='t=3', linestyle = '-.')
plt.plot(displacement, y(displacement,4), color='blue', label='t=4', linestyle = ':')
plt.legend(loc='upper right')
plt.savefig('#5 Ch2 HW.png', dpi=300)
