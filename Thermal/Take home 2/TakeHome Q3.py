# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:25:51 2019

@author: maxhu
"""
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

N_a = 300
N_b = 200                                          #Number of oscillators
q_a = np.linspace(0,100,101)                      #Units of energy values
q_b = np.linspace(100,0,101)
ep = 10                                         #Energy per quanta

def mult(qa,qb,na,nb):                                 #Multiplicity function for ES
    return sp.binom(qa + qb + na + nb - 1, qa + qb)

multiplicity_a = np.array(mult(q_a,0,N_a,0))              #Multiplicity values

S_a = np.array(np.log(mult(q_a,0,N_a,0)))                 #Entropy Values

multiplicity_b = np.array(mult(0,q_b,0,N_b))              #Multiplicity values

S_b = np.array(np.log(mult(0,q_b,0,N_b)))

U_a = np.array(q_a*ep)                              #Energy Values
U_b = np.array(q_b*ep)

du_a = []                                         #Change in energy initialized
du_b = []

for i in range(len(U_a)):                         #Centered Difference of U
    if i == len(U_a)-1:
        du_a.append(20)
        break
    if i == 0:
        du_a.append(20)
    else:
        du_a.append(U_a[i+1]-U_a[i-1])
    
d_U_a = np.array(du_a)                              #Change in energy values

for i in range(len(U_b)):                         #Centered Difference of U
    if i == len(U_b)-1:
        du_b.append(20)
        break
    if i == 0:
        du_b.append(20)
    else:
        du_b.append(U_b[i+1]-U_b[i-1])
    
d_U_b = np.array(du_b)

ds_a = []                                         #Change in entropy initialized
ds_b = []

for i in range(len(S_a)):                         #Centered Difference of S
    if i == len(S_a)-1:
        ds_a.append(0)
        break
    if i == 0:
        ds_a.append(1)
    else:
        ds_a.append(S_a[i+1]-S_a[i-1])

d_S_a = np.array(ds_a)                              #Change in entropy values

for i in range(len(S_b)):                         #Centered Difference of S
    if i == len(S_b)-1:
        ds_b.append(0)
        break
    if i == 0:
        ds_b.append(1)
    else:
        ds_b.append(S_b[i+1]-S_b[i-1])

d_S_b = np.array(ds_b)

t_a = []
t_b = []

for i in range(len(U_a)):                         #Calculating Temperature vals
    if i == len(U_a)-1:
        t_a.append(t_a[i-1])
        break
    if i == 0:
        t_a.append(0)
    else:
        t_a.append(d_U_a[i]/(ep*d_S_a[i]))
    
T_a = np.array(t_a)                                 #Temperature values

for i in range(len(U_b)):                         #Calculating Temperature vals
    if i == len(U_b)-1:
        t_b.append(t_b[i-1])
        break
    if i == 0:
        t_b.append(0)
    else:
        t_b.append(d_U_b[i]/(ep*d_S_b[i]))
    
T_b = np.array(t_b)                                 #Temperature values


dt_a = []                                         #Change in temp initialized
dt_b = []


for i in range(len(T_a)):                         #Centered Difference of T
    if i == len(T_a)-1:
        dt_a.append(dt_a[i-1])
        break
    if i == 0:
        dt_a.append(0)
    else:
        dt_a.append(T_a[i+1]-T_a[i-1])

d_T_a = np.array(dt_a)                              #Change in temperature values


for i in range(len(T_b)):                         #Centered Difference of T
    if i == len(T_b)-1:
        dt_b.append(dt_b[i-1])
        break
    if i == 0:
        dt_b.append(0)
    else:
        dt_b.append(T_b[i+1]-T_b[i-1])

d_T_b = np.array(dt_b)

c_a = []                                          #Heat capacity initialized
c_b = []                                          #Heat capacity initialized

for i in range(len(U_a)):
    if i == len(U_a)-1:
        c_a.append(c_a[i-1])
        break
    if i == 0:
        c_a.append(0)
    elif i == len(U_a)-2:
        c_a.append(c_a[i-2])
    else:
        c_a.append(d_U_a[i]/(N_a*d_T_a[i]))

for i in range(len(U_b)):
    if i == len(U_b)-1:
        c_b.append(c_b[i-1])
        break
    if i == 0:
        c_b.append(0)
    elif i == len(U_b)-2:
        c_b.append(c_b[i-2])
    else:
        c_b.append(d_U_b[i]/(N_b*d_T_b[i]))

C_a = np.array(c_a)
C_b = np.array(c_b)                                #Heat capacity values
ax = plt.figure(figsize=(30,10))
plt.subplot(121)
plt.scatter(q_a,T_a, s=10, color = 'black')
plt.scatter(q_a,T_b, s=10,color = 'm')

plt.legend(loc='best')
plt.title('Temperature as a Function of $q_a$', fontsize = 16)
plt.ylabel('$kT/\epsilon$', fontsize = 16)
plt.xlabel('$q_a$', fontsize = 16)
plt.savefig('Tvq')
#=============================================================================#
ax = plt.figure(figsize=(30,10))
plt.subplot(121)
plt.scatter(q_a,C_a, s=10, color = 'black')
plt.scatter(q_a,C_b, s=10,color = 'm')

plt.legend(loc='best')
plt.title('Heat Capacity as a Function of $q_a$', fontsize = 16)
plt.ylabel('$C/k$', fontsize = 16)
plt.xlabel('$q_a$', fontsize = 16)
plt.savefig('Cvq')

