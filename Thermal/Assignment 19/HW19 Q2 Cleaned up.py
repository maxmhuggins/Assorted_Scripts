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
plt.style.use('seaborn')
#=========================================================#
n = 100
tot = 101
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
    t.append(d_U[i]/d_S[i])

T = np.array(t)

DtA.centered_difference(T,dt)

d_T = np.array(dt)

for i in range(len(d_T)):
    c.append(d_U[i]/(n * d_T[i]))

C = np.array(c)
#=========================================================#
plt.figure(figsize=(15,15))
plt.subplot(221)
plt.plot(U_uB,s_k, 'black')
plt.xlabel('$U/{{\mu}B}$', fontsize=14)
plt.ylabel('$S/k$', fontsize=14)
plt.subplot(222)
plt.plot(U_uB/n, T, 'black')
plt.xlabel('$U/{N{\mu}B}$', fontsize=14)
plt.ylabel('$kT/{{\mu}B}$', fontsize=14)
plt.subplot(223)
plt.plot(T,C, 'black')
plt.xlabel('$kT/{{\mu}B}$', fontsize=14)
plt.ylabel('$C/{Nk}$', fontsize=14)
plt.xlim(0,20)
plt.subplot(224)
plt.plot(T, m_Nu, 'black')
plt.xlabel('$kT/{{\mu}B}$', fontsize=14)
plt.ylabel('$M/{N\mu}$', fontsize=14)

plt.savefig('HW19Q2.png')



