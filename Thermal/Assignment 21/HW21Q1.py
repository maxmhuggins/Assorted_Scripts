# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 02:41:42 2019

@author: maxhu
"""

#=========================================================#
import numpy as np
import matplotlib.pyplot as plt
import ThermalDataAcquisition as DtA
#=========================================================#
N = 50
#=========================================================#
q = np.linspace(0,N,N+1)
#=========================================================#
kT_e = []
ds = []
du = []
t = []
dt = []
c = []
#=========================================================#      
sigma = np.array(DtA.mult(q+N-1,q))
S_k = DtA.sk(sigma)
DtA.centered_difference(S_k,ds)
#=========================================================#    
for i in range(0,N):
    if i == 0:
        du.append(0)
    if i == N-1:
        du.append(0)
        break
    du.append()
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
    c.append(d_U[i]/(N * d_T[i]))

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
plt.plot(T,S_k, 'black')
plt.xlabel('$kT/{\mu}B$', fontsize=14)
plt.ylabel('$S/k$', fontsize=14)
#=========================================================#
