# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:04:42 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
plt.style.use('seaborn')

n = 100
tot = 101

N_u = np.linspace(n,0,tot)
N = np.arange(0,tot,1)
U_uB = np.arange(-n,tot,2)
m_Nu = np.linspace(-1,1,tot)

du = []
ds = []
dt = []

t = []
c = []

def mult(n,k):
    return sp.binom(n,k)

def sk(l):
    return np.log(l)

sigma = np.array(mult(n,N_u))
s_k = sk(sigma)

count = 0
for l in range(len(s_k)):
    if count + 1 >= len(s_k):
        ds.append(1)
        break
    if count < 1:
        ds.append(1)
    else:
        ds.append(s_k[l+1] - s_k[l-1])
    count = count + 1
    
for i in range(0,n):
    if i == 0:
        du.append(0)
    if i == n-1:
        du.append(0)
        break
    du.append(4)

d_U = np.array(du)
d_S = np.array(ds)


for i in range(len(d_S)):
    t.append(d_U[i]/d_S[i])

T = np.array(t)
count = 0
for l in range(len(T)):
    if count + 1 >= len(T):
        dt.append(1)
        break
    if count < 1:
        dt.append(1)
    else:
        dt.append(T[l+1] - T[l-1])
    count = count + 1

d_T = np.array(dt)

for i in range(len(d_T)):
    c.append(d_U[i]/(n * d_T[i]))

C = np.array(c)

plt.plot(U_uB,s_k, 'black')
plt.xlabel('$U/{{\mu}B}$', fontsize=14)
plt.ylabel('$S/k$', fontsize=14)
plt.show()
plt.close()
plt.plot(U_uB/n, T, 'black')
plt.xlabel('$U/{N{\mu}B}$', fontsize=14)
plt.ylabel('$kT/{{\mu}B}$', fontsize=14)
plt.show()
plt.close()
plt.plot(T,C, 'black')
plt.xlabel('$kT/{{\mu}B}$', fontsize=14)
plt.ylabel('$C/{Nk}$', fontsize=14)
plt.xlim(0,20)
plt.show()
plt.close()
plt.plot(T, m_Nu, 'black')
plt.xlabel('$kT/{{\mu}B}$', fontsize=14)
plt.ylabel('$M/{N\mu}$', fontsize=14)




