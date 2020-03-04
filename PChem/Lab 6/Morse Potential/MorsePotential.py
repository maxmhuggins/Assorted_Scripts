# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 01:50:38 2019

@author: maxhu
"""
#============================================================================#
import numpy as np
import matplotlib.pyplot as plt
#=======================================#
width = 10 #width for figures
size = 12 #fontsize for labels
#============================================================================#
#Constants
h = 6.626e-34           #   m^2*kg / s
c = 3e8                 #   m/s
#=======================================#
D_e = 0                 #   m^-1
m_1 = 0                 #   kg
m_2 = 0                 #   kg
k_f = 0                 #   N/m
r_e = 0                 #   m
#============================================================================#
n = 10000
r = np.linspace(.1e-10,.4e-9,n)
#=======================================#
def V(r, D_e, k_f, r_e, m_1, m_2):
    m_eff = (m_1 * m_2) / (m_1 + m_2)
    w = np.sqrt(k_f/m_eff)
    a = np.sqrt((m_eff * w**2) / (2 * h * c * D_e))
    
    return h * c * D_e * (1 - np.exp(-a * (r - r_e)))**2
#=======================================#
#Values for HCl
D_e = 3724997           #   m^-1
m_1 = 1.6735575e-27     #   kg
m_2 = 5.8871086e-26     #   kg
k_f = 516               #   N/m
r_e = 1.27455e-10       #   m
#=======================================#
fig = plt.figure(1,figsize=(width,8))

plt.plot(r, V(r, D_e, k_f, r_e, m_1, m_2), color='black', label='$k_f$=516 N/m')
plt.plot(r, V(r, D_e, 2*k_f, r_e, m_1, m_2), color='magenta', label='$2k_f$')
plt.plot(r, V(r, D_e, 4*k_f, r_e, m_1, m_2), color='cyan', label='$4k_f$')

plt.ylim(-.005e-17,.1e-17)
plt.xlim(.5e-10,4.25e-10)

plt.title('Morse Potential for HCl', fontsize=15)
plt.ylabel('Potential Energy (J)', fontsize=size)
plt.xlabel('Internuclear distance (m)', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.savefig('Morse_Potential_for_HCl.png', dpi=900)
#============================================================================#
