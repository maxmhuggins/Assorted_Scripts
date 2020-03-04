# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:49:28 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

#constants
A1 = 1
phase1 = 0
phase2 = 0
x01 = 0
y01 = 0
x02 = -1
y02 = -0.5
x03 = 1
x03 = -1
j =np.complex(0,1)
freq = .5
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

#def p2(x,y,t):
#    r = np.sqrt((x-x02)**2 + (y-y02)**2)
#    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
#    return np.real(p20)
#
#def p3(x,y,t):
#    r = np.sqrt((x-x03)**2 + (y-y01)**2)
#    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
#    return np.real(p10)
#
#def p4(x,y,t):
#    r = np.sqrt((x-x03)**2 + (y-y02)**2)
#    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
#    return np.real(p10)



#Making XY grid points
N = 50
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
t_values = np.linspace(0,1,N)
file_name = '{:03d}_spherical_source_contour_filled.png'

for i in range(len(t_values)):
    w, h = plt.figaspect(1.)
    fig = plt.figure(figsize=(w, h))
    my_fig = fig.add_subplot(111,aspect='equal')
    my_fig.set_xlabel('x-pos')
    my_fig.set_ylabel('y-pos')
    my_fig.set_title('Spherical Source')
    Z = pl(X,Y,t_values[i])
    n_lines = 50
    plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
    plt.tight_layout()
    plt.savefig(file_name. format(i))
    plt.close()
