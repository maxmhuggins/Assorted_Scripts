# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:47:00 2019

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:04:42 2019

@author: maxhu
"""
#=========================================================#
import numpy as np
import matplotlib.pyplot as plt
import ThermalDataAcquisition as DtA
#=========================================================#
#plt.style.use('seaborn')
#=========================================================#
n = 1000
tot = 1001
#=========================================================#
N_u = np.linspace(n,0,tot)
N = np.arange(0,tot,1)
U_uB = np.arange(-n,tot,2)
m_Nu = np.linspace(-1,1,tot)
#=========================================================#
du = []
ds = []
dt = []

t = []
c = []
#=========================================================#      
sigma = np.array(DtA.mult(n,N_u))
s_k = DtA.sk(sigma)
DtA.centered_difference(s_k,ds)
#=========================================================#    
for i in range(0,n):
    if i == 0:
        du.append(0)
    if i == n-1:
        du.append(0)
        break
    du.append(4)
#=========================================================#
d_U = np.array(du)
d_S = np.array(ds)
#=========================================================#
for i in range(len(d_S)):
    t.append(d_U[i]/(d_S[i]))

T = np.array(t)

DtA.centered_difference(T,dt)

d_T = np.array(dt)

for i in range(len(d_T)):
    c.append(d_U[i]/(n * d_T[i]))

C = np.array(c)
#=========================================================#
fig = plt.figure(figsize=(10,20))
ax = fig.add_subplot(2, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-10,10)

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(T,s_k, 'black')
plt.xlabel('$kT/{\mu}B$', fontsize=14)
plt.ylabel('$S/k$', fontsize=14)
#=========================================================#
t = []

for i in range(len(d_S)):
    t.append(d_U[i]/(5*d_S[i]))

T = np.array(t)
ax_2 = fig.add_subplot(2, 1, 2)
ax_2.spines['left'].set_position('center')
ax_2.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax_2.spines['right'].set_color('none')
ax_2.spines['top'].set_color('none')
ax_2.set_xlim(-10,10)
# Show ticks in the left and lower axes only
ax_2.xaxis.set_ticks_position('bottom')
ax_2.yaxis.set_ticks_position('left')
ax_2.plot(T,s_k, 'black', label = 'Large B-Field')
ax_2.set_xlabel('$kT/{\mu}B$',fontsize=14)
ax_2.set_ylabel('$S/k$', fontsize=14)
ax_2.legend(loc='right')

plt.savefig('HW20Q4.png')
#=========================================================#



