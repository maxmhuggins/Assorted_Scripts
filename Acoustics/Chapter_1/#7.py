# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import matplotlib.pyplot as plt
import numpy as np

def Theta(x):
    num = x*(1 - (1/x)**2)
    dem = 0.2
    return np.arctan2(num,dem)

def phi(x):
    num = 0.2
    dem = 1 - (1/x)**2
    return np.arctan2(num,dem)

def U(x):
    num = np.sqrt((1 - (1/x)**2)**2 + 0.04)
    dem = np.sqrt(0.04*(1/x)**2 + (1-(1/x)**2)**2)
    return num/dem

def response(x,t):
    return U(x)*np.exp(-0.1*1*t)*np.cos(1*t + phi(x)) + np.sin(x*t - Theta(x))

t_start = 0
t_end = 40.0
num = 1000

t_values = np.linspace(t_start,t_end,num)
fig = plt.figure()
my_fig = fig.add_subplot(1,1,1)

plt.plot(t_values ,response(3,t_values), color='black', label='$\\omega/\omega_d = 3$', linestyle = '-')

my_fig.set_xlabel('$t$')
my_fig.set_ylabel('$x(t)/(F/\omega Z_m)$')
my_fig.set_title('Transient Response')
plt.legend(loc='upper right')

plt.savefig('#7 plot', dpi=300)