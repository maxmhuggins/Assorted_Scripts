# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:57:29 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:56:30 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

ka = 10

def f(n):
    return np.math.factorial(n)

def b(theta, ka):
    v = ka*np.sin(theta)
    J = 0
    for i in range(100):
        J_1 =( ((-1)**i) / (2**(2*i+1) *f(i) *f(1+i)) ) * v**(2*i+1)
        J += J_1
    H = np.abs((2*J)/v)
    b = 20*np.log10(H)
    return b
    


num = 1000
theta_values = np.linspace(0,2*np.pi,num)

fig = plt.figure(1,figsize=(12, 12))
my_fig = fig.add_subplot(1,3,2,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, ka = 10), color='black', linestyle='-')
my_fig.set_title('beam pattern for circular plane piston: $ka=10$', y=1.1)
##########################################################################
fig = plt.figure(2,figsize=(20, 20))
my_fig = fig.add_subplot(5,3,1,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, ka = 1), color='black', linestyle='-')
my_fig.set_title('beam pattern for circular plane piston: $ka=1$', y=1.25)
##########################################################################
fig = plt.figure(2,figsize=(20, 20))
my_fig = fig.add_subplot(5,3,2,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, ka = 10), color='black', linestyle='-')
my_fig.set_title('beam pattern for circular plane piston: $ka=10$', y=1.25)
##########################################################################
fig = plt.figure(2,figsize=(20, 20))
my_fig = fig.add_subplot(5,3,3,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, ka = 20), color='black', linestyle='-')
my_fig.set_title('beam pattern for circular plane piston: $ka=20$', y=1.25)
##########################################################################
fig = plt.figure(2,figsize=(20, 20))
my_fig = fig.add_subplot(5,3,7,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, ka = 50), color='black', linestyle='-')
my_fig.set_title('beam pattern for circular plane piston: $ka=50$', y=1.25)
##########################################################################
plt.savefig('Q3&4.png', dpi=300)

