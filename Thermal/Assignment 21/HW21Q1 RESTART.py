# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:25:51 2019

@author: maxhu
"""
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

N = 50                                          #Number of oscillators
q = np.linspace(0,100,101)                      #Units of energy values
ep = 10                                         #Energy per quanta

def mult(n, k):                                 #Multiplicity function for ES
    return sp.binom(n + k - 1, k)

multiplicity = np.array(mult(N,q))              #Multiplicity values

S = np.array(np.log(mult(N,q)))                 #Entropy Values

U = np.array(q*ep)                              #Energy Values

du = []                                         #Change in energy initialized

for i in range(len(U)):                         #Centered Difference of U
    if i == len(U)-1:
        du.append(20)
        break
    if i == 0:
        du.append(20)
    else:
        du.append(U[i+1]-U[i-1])
    
d_U = np.array(du)                              #Change in energy values

ds = []                                         #Change in entropy initialized

for i in range(len(S)):                         #Centered Difference of S
    if i == len(S)-1:
        ds.append(0)
        break
    if i == 0:
        ds.append(1)
    else:
        ds.append(S[i+1]-S[i-1])

d_S = np.array(ds)                              #Change in entropy values

t = []

for i in range(len(U)):                         #Calculating Temperature vals
    if i == len(U)-1:
        t.append(t[i-1])
        break
    if i == 0:
        t.append(0)
    else:
        t.append(d_U[i]/(ep*d_S[i]))
    
T = np.array(t)                                 #Temperature values

dt = []                                         #Change in temp initialized

for i in range(len(T)):                         #Centered Difference of T
    if i == len(T)-1:
        dt.append(dt[i-1])
        break
    if i == 0:
        dt.append(0)
    else:
        dt.append(T[i+1]-T[i-1])

d_T = np.array(dt)                              #Change in temperature values

c = []                                          #Heat capacity initialized

for i in range(len(U)):
    if i == len(U)-1:
        c.append(c[i-1])
        break
    if i == 0:
        c.append(0)
    elif i == len(U)-2:
        c.append(c[i-2])
    else:
        c.append(d_U[i]/(N*10*d_T[i]))

C = np.array(c)                                 #Heat capacity values
ax = plt.figure(figsize=(20,5))
plt.subplot(121)
plt.scatter(T,C, s=10, color = 'black', label = '50 oscillators')
plt.legend(loc='best')
plt.xlabel('$kT/\epsilon$')
plt.ylabel('$C/Nk$')
#=============================================================================#
N = 5000                                        #Number of oscillators
q = np.linspace(0,100,101)                      #Units of energy values
ep = 10                                         #Energy per quanta

def mult(n, k):                                 #Multiplicity function for ES
    return sp.binom(n + k - 1, k)

multiplicity = np.array(mult(N,q))              #Multiplicity values

S = np.array(np.log(mult(N,q)))                 #Entropy Values

U = np.array(q*ep)                              #Energy Values

du = []                                         #Change in energy initialized

for i in range(len(U)):                         #Centered Difference of U
    if i == len(U)-1:
        du.append(20)
        break
    if i == 0:
        du.append(20)
    else:
        du.append(U[i+1]-U[i-1])
    
d_U = np.array(du)                              #Change in energy values

ds = []                                         #Change in entropy initialized

for i in range(len(S)):                         #Centered Difference of S
    if i == len(S)-1:
        ds.append(0)
        break
    if i == 0:
        ds.append(1)
    else:
        ds.append(S[i+1]-S[i-1])

d_S = np.array(ds)                              #Change in entropy values

t = []

for i in range(len(U)):                         #Calculating Temperature vals
    if i == len(U)-1:
        t.append(t[i-1])
        break
    if i == 0:
        t.append(0)
    else:
        t.append(d_U[i]/(ep*d_S[i]))
    
T = np.array(t)                                 #Temperature values

dt = []                                         #Change in temp initialized

for i in range(len(T)):                         #Centered Difference of T
    if i == len(T)-1:
        dt.append(dt[i-1])
        break
    if i == 0:
        dt.append(0)
    else:
        dt.append(T[i+1]-T[i-1])

d_T = np.array(dt)                              #Change in temperature values

c = []                                          #Heat capacity initialized

for i in range(len(U)):
    if i == len(U)-1:
        c.append(c[i-1])
        break
    if i == 0:
        c.append(0)
    elif i == len(U)-2:
        c.append(c[i-2])
    else:
        c.append(d_U[i]/(N*10*d_T[i]))

C = np.array(c)                                 #Heat capacity values
plt.subplot(122)
plt.scatter(T,C, s=10, color = 'black', label = '5000 oscillators')
plt.legend(loc='best')
plt.xlabel('$kT/\epsilon$')
plt.ylabel('$C/Nk$')

plt.savefig('HW21Q1')