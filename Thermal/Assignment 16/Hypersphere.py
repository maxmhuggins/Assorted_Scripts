# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:25:26 2019

@author: maxhu
"""
#===============================Modules==================================#
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#============================Some Constants==============================#
m_argon = 39.95 #amu
m_helium = 4.00 #amu
m_radon = 222.02 #amu

c = 1 #  In reality this is 2*U, but for all three gases this is a 
      #  constant value and on the magnitude of ~ 1
      
r = np.sqrt(c*m_argon) # This is the radius of a 'hypersphere' 
                       # in phase space
#============================Plotting====================================#
fig = plt.figure(figsize = (20,20))
ax = fig.gca(projection='3d')
ax.set_aspect("equal")
#Making arrays for momentum values
p_x = np.linspace(0,2*np.pi, 40)
p_y = np.linspace(0,np.pi, 40)
# draw sphere
u, v = np.meshgrid(p_x, p_y)
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
#These are my labels for each sphere
l_argon = "Argon Gas"
l_helium = "Helium Gas"
l_radon = "Radon Gas"
#Plotting spheres at different mass values (different radii)
ax.plot_wireframe(r*x, r*y, r*z, color="m", label = l_argon)
r = np.sqrt(c*m_helium)
ax.plot_wireframe(r*x, r*y, r*z, color="k", label = l_helium)
r = np.sqrt(c*m_radon)
ax.plot_wireframe(r*x, r*y, r*z, color="c", label = l_radon)
#Some axes labels and a title
title = 'Momentum for Different Monatomic Gases'
ax.text2D(-.033,.055, title, fontsize = 18)
ax.set_xlabel('$P_x$', fontsize = 16)
ax.set_ylabel('$P_y$', fontsize = 16)
ax.set_zlabel('$P_z$', fontsize = 16)
ax.legend(loc=6, fontsize = 16)
plt.savefig('SpheresofDifferentMass.png')
#========================================================================#
