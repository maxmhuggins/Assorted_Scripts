# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 05:04:57 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.linspace(0,1,100)
v = np.linspace(1,0,100)
U, V = np.meshgrid(u, v)

Z = -(U*np.log(U)+V*np.log(V)+(1-U-V)*np.log(1-U-V))

fig = plt.figure(figsize=(20,10))
ax = fig.gca(projection="3d")
ax.plot_surface(U, V, Z, alpha=.8)


