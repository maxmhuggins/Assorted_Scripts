# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:22:57 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

def D(t,c):
    phi = np.arctan2(-c,np.sqrt(1-c**2))
    A = 1/np.cos(phi)
    return A*np.exp(-2*np.pi*t*c)*np.cos(2*np.pi*t*np.sqrt(1-c**2)+phi)

t_start = 0
t_end = 10
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, D(time,.1), color='darkblue', label='c=.2', linestyle = '-')

my_fig = fig.add_subplot(1,1,1)

my_fig.set_xlabel('t/T')
my_fig.set_ylabel('x')
my_fig.set_title('Displacement of an Underdamped Oscillator')
plt.legend(loc='best')
plt.savefig('#3Graph1')


fig = plt.figure (2)
plt.plot(time, D(time,.2), color='darkblue', label='c=.2', linestyle = '-')
my_fig = fig.add_subplot(1,1,1)

my_fig.set_xlabel('t/T')
my_fig.set_ylabel('x')
my_fig.set_title('Displacement of an Underdamped Oscillator')
plt.legend(loc='best')
plt.savefig('#3Graph2')

fig = plt.figure (3)
plt.plot(time, D(time,.3), color='purple', label='c=.3', linestyle = '-')
my_fig = fig.add_subplot(1,1,1)

my_fig.set_xlabel('t/T')
my_fig.set_ylabel('x')
my_fig.set_title('Displacement of an Underdamped Oscillator')
plt.legend(loc='best')
plt.savefig('#3Graph3')
