# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:55:16 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t,n_max):
    f_value = 0
    for n in range(1, n_max):
        f_value = (f_value - 2/n*(np.sin(n*t)*(-1)**n))
    return f_value

t_start = 0
t_end = 6
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)



plt.plot(time, f(time,10), color='black', label='n=17', linestyle = '-')

my_fig.set_xlabel('t')
my_fig.set_ylabel('x')
my_fig.set_title('Sawtooth Waveform')
plt.legend(loc='best')
plt.savefig('#6Graph1')