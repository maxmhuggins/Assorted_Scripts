# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:08:57 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

L = 1.0
l = np.linspace(0.1,L,1000)
g = 9.8

def T(l):
    return 2*np.pi*np.sqrt(l/g)

fig = plt.figure (1)
my_fig = fig.add_subplot(1,1,1)
plt.plot(T(l), color='darkblue', linestyle = '-')
my_fig.set_xlabel('t/T')
my_fig.set_ylabel('x')
my_fig.set_title('Displacement of an Underdamped Oscillator')
plt.legend(loc='best')
plt.savefig('#3Graph1')
