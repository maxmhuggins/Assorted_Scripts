# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:08:58 2019

@author: maxhu
"""

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
v = (2991 / 83.593) * 1000 #J/mol
D_o = 428e3 / (h * c) #J/mol
D_e = D_o + .5 * v
m_1 = 1.6735575e-27 #kg
m_2 = 5.8871086e-26 #kg
k_f = 516 #N/m
eV_conv = 6.242e+18 #eV/J
#============================================================================#
m_eff = (m_1 * m_2) / (m_1 + m_2)
a = np.sqrt((m_eff * (k_f / m_eff)) / (2 * h * c * D_e))
R = np.linspace(-10*np.pi, 64*np.pi, 1000)
R_e_vals = np.linspace(50e-12,300e-12,10)
k_vals = np.linspace(1,20)
#============================================================================#
def V(R,R_e):
    return h * c * D_e * (1 - np.exp(-a * (R - R_e)))**2
#============================================================================#
#file_name = '{:03d}_MorsePotential.jpg'
#for i in range(0,len(R_e_vals)):
#    plt.figure(1, figsize=(7,5))
#    plt.ylim(-1e4,6e5)
#    plt.title('Morse Potential')
#    plt.xlabel('Displacement (m)')
#    plt.ylabel('Potential Energy (J)')
#    plt.plot(R, V(R, R_e_vals[i]), 'm')
#    plt.savefig(file_name. format(i), dpi=200)
#    plt.close()
#============================================================================#
#plt.figure(2, figsize=(10,7))
#plt.ylim(-1e4,6e5)
#plt.title('Morse Potential') 
#plt.xlabel('Displacement (m)')
#plt.ylabel('Potential Energy (J)')
#plt.plot(R, V(R, R_e_vals[0]), 'black', label = r'$R_e = 50*10^{-12}m$')
#plt.plot(R, V(R,R_e_vals[5]), 'm', linestyle=':', label = r'$R_e = 2*10^{-10}m$')
#plt.plot(R, V(R, R_e_vals[9]), 'c', linestyle='--', label = r'$R_e = 3*10^{-10}m$')
#plt.legend(loc='best')
#plt.savefig('MorsePotentialQ3.png', dpi=500)

plt.figure(3, figsize=(10,7))
plt.title('Morse Potential') 
plt.xlabel('Displacement (m)')
plt.ylabel('Potential Energy (eV)')
plt.plot(R, V(R, R_e_vals[0])*eV_conv, 'black', label = r'$R_e = 50*10^{-12}m$')
plt.legend(loc='best')
plt.savefig('MorsePotentialQ5.png', dpi=100)