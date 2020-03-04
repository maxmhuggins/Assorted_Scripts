# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:48:08 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 1
m = 1
A = 1
h = 1
k = 1

u = np.linspace(-.5,.5,10000)
v = np.linspace(-.5,.5,10000)
U, V = np.meshgrid(u, v)

#Z = ((N / np.sqrt(np.pi*2))*np.exp(-N*U**2) * (N / np.sqrt(np.pi*2))*np.exp(-N*V**2))
#fig = plt.figure(figsize=(20,10))
#ax = fig.gca(projection="3d")
#ax.plot_surface(U, V, Z, alpha=.8)

#ax.view_init(30, 30)
file_name = './Multiplicity/{:06d}_Multiplicity.jpg'

for i in np.arange(0,100000,1000):
    Z = ((i / np.sqrt(np.pi*2))*np.exp(-i*U**2) * (i / np.sqrt(np.pi*2))*np.exp(-i*V**2))
    fig = plt.figure(figsize=(20,10))
    ax = fig.gca(projection="3d")
    ax.plot_wireframe(U, V, Z, alpha=.8)
    plt.savefig(file_name. format(i))

    