# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:03:32 2019

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

spacing = 10
x = np.linspace(-10,10,1000)
x_e = np.linspace(-10,10,10)
E_1 = np.linspace(spacing,spacing,10)
y = x**2
y2 = 2*x**2
y3 = 5*x**2


fig = plt.figure(1,figsize=(10, 6.5))
my_fig = fig.add_subplot(111)
size=10
plt.plot(x,y, color='black', label='$k_f=1x$')
plt.plot(x,y2, color='m', label='$k_f=2x$')
plt.plot(x,y3, color='c', label='$k_f=5x$')
plt.plot(x_e,E_1, linestyle='--', alpha=.3, label='$E_0$')
plt.plot(x_e,E_1+spacing, linestyle='--', alpha=.3, label='$E_1$')
plt.plot(x_e,E_1+2*spacing, linestyle='--', alpha=.3, label='$E_2$')
plt.plot(x_e,E_1+3*spacing, linestyle='--', alpha=.3, label='$E_3$')
plt.plot(x_e,E_1+4*spacing, linestyle='--', alpha=.3, label='$E_4$')




plt.ylim(0,100)
plt.ylabel('V(x)', fontsize=size)
plt.xticks(color='w')
plt.yticks(color='w')
plt.xlabel('Internuclear Seperation', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.title('Sketch of Harmonic Oscillator Potential', fontsize=size)
plt.savefig('Sketch_harmonic.png', dpi=900)