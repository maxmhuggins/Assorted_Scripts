# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 01:36:16 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

Q = 1

def A(t,Q):
    return t**(-2)*(1/Q)*(t**(-2)*(1/Q**2)+(1 - t**(-2))**2)**(-(1/2))

def V(t,Q):
    return t**(-1)*Q**(-1)*(t**(-2)*Q**(-2)+(1-(t**-2))**2)**(-1/2)

def P(t,Q):
    return t**(-2)*(1/Q**2)*(t**(-2)*(1/Q**2)+(1 - t**(-2))**2)**(-(1))

def O(t,Q):
    return np.arctan(Q*t*(1 - t**2))

t_start = .1
t_end = 10
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)


plt.plot(time, A(time,1), color='purple', label='Q=1', linestyle = '-')
plt.plot(time, A(time,2), color='green', label='Q=2', linestyle = ':')
my_fig = fig.add_subplot(1,1,1)

plt.xscale("log")
my_fig.set_xlabel('$\omega/\omega_o$')
my_fig.set_ylabel('$x/x_res$')
my_fig.set_title('Dimensionless Displacement for Damped Driven Oscillator')
plt.legend(loc='best')
plt.savefig('#4Graph1')

fig = plt.figure(2)
plt.plot(time, V(time,1), color='black', label='Q=1', linestyle = '-')
plt.plot(time, V(time,2), color='red', label='Q=2', linestyle = ':')
my_fig = fig.add_subplot(1,1,1)

plt.xscale("log")
my_fig.set_xlabel('$\omega/\omega_o$')
my_fig.set_ylabel('$x/x_res$')
my_fig.set_title('Dimensionless Displacement for Damped Driven Oscillator')
plt.legend(loc='best')
plt.savefig('#4Graph2')


fig = plt.figure(3)
plt.plot(time, P(time,1), color='c', label='Q=1', linestyle = '-')
plt.plot(time, P(time,2), color='b', label='Q=2', linestyle = ':')
my_fig = fig.add_subplot(1,1,1)

plt.xscale("log")
my_fig.set_xlabel('$\omega/\omega_o$')
my_fig.set_ylabel('$x/x_res$')
my_fig.set_title('Dimensionless Displacement for Damped Driven Oscillator')
plt.legend(loc='best')
plt.savefig('#4Graph3')


fig = plt.figure(4)
plt.plot(time, O(time,1), color='darkblue', label='Q=1', linestyle = '-')
plt.plot(time, O(time,2), color='lightblue', label='Q=2', linestyle = ':')
my_fig = fig.add_subplot(1,1,1)

plt.xscale("log")
my_fig.set_xlabel('$\omega/\omega_o$')
my_fig.set_ylabel('$x/x_res$')
my_fig.set_title('Dimensionless Displacement for Damped Driven Oscillator')
plt.legend(loc='best')
plt.savefig('#4Graph4')

