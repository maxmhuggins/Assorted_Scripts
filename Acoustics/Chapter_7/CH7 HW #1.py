# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:56:30 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
def b(theta,kL):
    v = .5*kL*np.sin(theta)
    H = np.abs(np.sinc(v/np.pi))
    b = 20*np.log10(H)
    return b

num = 500
theta_values = np.linspace(0,2*np.pi,num)

#w, h = plt.figaspect(1.)
fig = plt.figure(1,figsize=(15, 15))
my_fig = fig.add_subplot(5,3,2,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, kL=24), color='black', linestyle='-')
my_fig.set_title('beam pattern for line source: $kL=24$', y=1.4)
###############################################################################
#w, h = plt.figaspect(1.)
#fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(5,3,7,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, kL=1), color='black', linestyle='-')
my_fig.set_title('beam pattern for line source: $kL=1$', y=1.4)
###############################################################################
#w, h = plt.figaspect(1.)
#fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(5,3,8,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, kL=10), color='black', linestyle='-')
my_fig.set_title('beam pattern for line source: $kL=10$', y=1.4)
###############################################################################
#w, h = plt.figaspect(1.)
#fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(5,3,9,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, kL=20), color='black', linestyle='-')
my_fig.set_title('beam pattern for line source: $kL=20$', y=1.4)
###############################################################################
#w, h = plt.figaspect(1.)
#fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(5,3,14,projection='polar', aspect='equal')
my_fig.plot(theta_values, b(theta_values, kL=50), color='black', linestyle='-')
my_fig.set_title('beam pattern for line source: $kL=50$', y=1.4)
plt.savefig('Q1.png', dpi=300)
###############################################################################

