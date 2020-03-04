# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:55:16 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t,n_max):
    f_value = 0
    for n in range(1, n_max, 2):
        f_value = (f_value + (4/np.pi)*(np.sin(2*np.pi*n*t)/n))
    return f_value

t_start = .1
t_end = 1
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)

plt.plot(time, f(time,2), color='r', label='n=2', linestyle = ':')
plt.plot(time, f(time,5), color='g', label='n=5', linestyle = '--')
plt.plot(time, f(time,20), color='b', label='n=20', linestyle = '-.')
plt.plot(time, f(time,50), color='black', label='n=50', linestyle = '-')
my_fig.set_xlabel('t')
my_fig.set_ylabel('x')
my_fig.set_title('Fourier Square Wave')
plt.legend(loc='best')
plt.savefig('#5Graph1')
