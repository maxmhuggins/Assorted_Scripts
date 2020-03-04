# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:48:06 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

#Define some constants
z = 1 #Unphysical characteristic impedence
p0 = 1  #Acoustic pressure amplitude
j = np.complex(0,1)
freq = 4 
omega = 2*np.pi*freq
c =1 
k = omega/c


def u(x,t):
    return np.real((p0/z)*np.exp(j*(omega*t-k*x)))

N = 5500

x_values = np.random.randint (0,100,N)/100
y_values = np.random.randint(0,100,N)/100


Period = 1/freq

t_values = np.linspace(0,4*Period,100)
    
tstep = 4*Period/100

file_name = '{:03d}_plane_wave.jpg'

for i in range(len(t_values)):
    fig = plt.figure()
    my_fig = fig.add_subplot(1,1,1)
    my_fig.set_xlabel('x-position')
    my_fig.set_ylabel('y-position')
    my_fig.set_title('Plane Wave')
    plt.ylim(0, 1.0)
    plt.xlim(0, 1.0)
    plt.scatter(x_values+u(x_values,t_values[i])*tstep, y_values, s = 5, color = 'b', marker='.')
    plt.savefig(file_name.format(i))
    plt.close()
