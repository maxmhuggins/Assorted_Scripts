# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 07:58:36 2018

@author: maxhu
"""
######## WARNING ########
#This is a very rugged attempt at Q2 part H in python
import matplotlib.pyplot as plt
import numpy as np
import math

L = .905
g = 9.8
w_1 = (2.4/2)*np.sqrt(g/L)
w_2 = (5.52/2)*np.sqrt(g/L)
w_3 = (8.65/2)*np.sqrt(g/L)
w_4 = (11.79/2)*np.sqrt(g/L)
w_5 = (14.93/2)*np.sqrt(g/L)

def BesselJ(n,u):
    BJ = 0
    for i in range (0,100):
        coeff = ((-1)**i)/(2**(2*i+n)*math.factorial(i)*math.factorial(n+i))
        BJ = BJ + coeff*u**(2*i+n)
    return BJ

def h(w, J):
    return J*(2*w*np.sqrt(L/g))

t_start = .1
t_end = 10
num = 2000

time = np.linspace(t_start,t_end,num)
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)


plt.plot(time, h(w_1, BesselJ(0)), color='purple', label='Q=1', linestyle = '-')
