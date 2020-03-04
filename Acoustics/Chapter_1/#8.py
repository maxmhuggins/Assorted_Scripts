# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:26:19 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

A = 5
Beta =7

def x(t,omega):
    return A*np.cos(omega*t)

t_start = 0
t_end = np.pi
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)

plt.plot(time, x(time,5)+x(time,5+1), color='purple', linestyle = '-')

my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Constructive and Destructive Interference')
plt.savefig('#8Graph1')
fig = plt.figure(2)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, x(time,5)+x(time,5+2), color='purple', linestyle = '-')
my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Constructive and Destructive Interference')
plt.savefig('#8Graph2')
fig = plt.figure(3)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, x(time,5)+x(time,5+3), color='purple', linestyle = '-')
my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Constructive and Destructive Interference')
plt.savefig('#8Graph3')

fig = plt.figure(4)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, x(time,5)+x(time,5+4), color='purple', linestyle = '-')
my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Constructive and Destructive Interference')
plt.savefig('#8Graph4')

fig = plt.figure(5)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, x(time,5)+x(time,5+5), color='purple', linestyle = '-')
my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Constructive and Destructive Interference')
plt.savefig('#8Graph5')

fig = plt.figure(6)
my_fig = fig.add_subplot(1,1,1)
plt.plot(time, x(time,5), color='purple', linestyle = '-')
my_fig.set_xlabel('Time')
my_fig.set_ylabel('Amplitude')
my_fig.set_title('Original Function')
plt.savefig('#8Graph6')
