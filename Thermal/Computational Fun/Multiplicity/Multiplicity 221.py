# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:14:50 2019

@author: maxhu
"""

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

u = np.linspace(-5,5,100)
v = np.linspace(-5,5,100)
U, V = np.meshgrid(u, v)

Z = ((4 * U * (1 - U))* (4 * V * (1 - V)))**N
fig = plt.figure(figsize=(20,10))
ax = fig.gca(projection="3d")
ax.plot_surface(U, V, Z, alpha=.8)

