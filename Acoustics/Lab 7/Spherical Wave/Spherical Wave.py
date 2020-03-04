# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:32:37 2018

@author: marhu
"""


import numpy as np
import matplotlib.pyplot as plt

#Define some constants
 #Unphysical characteristic impedence
p0 = 1  #Acoustic pressure amplitude
j = np.complex(0,1)
freq = 4
omega = 2*np.pi*freq
c = 1
k = omega/c
pc = .5

def u(x,y,t):
    r = np.sqrt(x**2+y**2)
    z = ((pc*(k*r)**2)/(1+(k*r)**2))+((j*pc*k*r)/(1+(k*r)**2))
    return np.real((p0/((z * r)))*np.exp(j*(omega*t-k*r)))

N = 10000

x_values = np.random.randint (-1000,1000,N)/1000
y_values = np.random.randint(-1000,1000,N)/1000


Period = 1/freq

t_values = np.linspace(0,4*Period,1000)
    
tstep = 4*Period/100

file_name = '{:03d}_spherical_wave.jpg'

for i in range(len(t_values)):
    
    p = x_values + u(x_values,y_values,t_values[i])*np.cos(np.arctan2(y_values, x_values))*tstep
    q = y_values + u(x_values,y_values, t_values[i])*np.sin(np.arctan2(y_values, x_values))*tstep
    fig = plt.figure()
    my_fig = fig.add_subplot(111,aspect='equal')
    my_fig.set_xlabel('x-position')
    my_fig.set_ylabel('y-position')
    my_fig.set_title('Spherical Wave')
    plt.ylim(-1.0, 1.0)
    plt.xlim(-1.0, 1.0)
    plt.scatter (p, q, s = 1, color = 'b', marker='.')
    plt.savefig(file_name. format(i))
    plt.close()
    
