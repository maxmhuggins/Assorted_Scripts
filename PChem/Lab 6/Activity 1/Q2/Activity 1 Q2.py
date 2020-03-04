# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:19:49 2019

@author: maxhu
"""
#===================Importing modules========================================#
import numpy as np
import matplotlib.pyplot as plt
#============================================================================#
h = 6.626e-34 #m^2*kg / s
c = 3e8 #m/s
v = 2991e2 #1/m
D_o = 428e3 / (h * c) #J/mol
D_e = D_o + .5 * v
R_e = 127e-12
m_1 = 1.6735575e-27 #kg
m_2 = 5.8871086e-26 #kg
k_f = 516 #N/m
#============================================================================#
m_eff = (m_1 * m_2) / (m_1 + m_2)
R = np.linspace(-10*np.pi, 64*np.pi, 1000)
k_vals = np.linspace(1,20)
#============================================================================#
def V(R,k_f):
    return h * c * D_e * (1 - np.exp(-(np.sqrt((m_eff * (
            k_f / m_eff)) / (2 * h * c * D_e))) * (R - R_e)))**2
#============================================================================#
#file_name = '{:03d}_MorsePotential.jpg'
#for i in range(0,len(k_vals)):
#    plt.figure(1, figsize=(7,5))
#    plt.ylim(-1e4,6e5)
#    plt.title('Morse Potential')
#    plt.xlabel('Displacement (m)')
#    plt.ylabel('Potential Energy (J)')
#    plt.plot(R, V(R, k_vals[i] * k_f), 'm')
#    plt.savefig(file_name. format(i), dpi=200)
#    plt.close()
#============================================================================#
plt.figure(2, figsize=(10,7))
plt.ylim(-1e4,6e5)
plt.title('Morse Potential')
plt.xlabel('Displacement (m)')
plt.ylabel('Potential Energy (J)')
plt.plot(R, V(R, k_f), 'black', label = r'$k_f$')
plt.plot(R, V(R,2* k_f), 'm', linestyle=':', label = r'$2k_f$')
plt.plot(R, V(R, 10*k_f), 'c', linestyle='--', label = r'$10k_f$')
plt.legend(loc='best')
#plt.savefig('MorsePotential.png', dpi=500)