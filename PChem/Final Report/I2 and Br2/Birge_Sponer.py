# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:51:48 2019

@author: maxhu
"""
#============================================================================#
import numpy as np
import matplotlib.pyplot as plt
import LinearRegressionClass as LR
#============================================================================#
convert = 83.593

w_n = []
#============================================================================#
lines = np.loadtxt('I2_mins.txt', delimiter=',')
for line in lines:
    w_n.append(1e7/line[0])
    
del_E = []
for i in range(0,len(w_n)):
    if i == len(w_n)-1:
        break
    else:
        del_E.append(w_n[i+1]-w_n[i])

v = np.linspace(0,len(w_n)-1,len(w_n)-1)
#============================================================================#

x_int=86
v_lin = np.linspace(0,x_int,x_int)
LR.linear_regression(v,del_E)

size = 10
fig = plt.figure(1,figsize=(10,8))
plt.title('Birge-Sponer Plot for $I_2$', fontsize=15)
plt.plot(v_lin,LR.my_fit(v_lin), color='black', label=r'$\Delta \tilde{G}(\nu)$ from linear regression')
plt.scatter(v,del_E, color ='m', label=r'$\Delta \tilde{G}(\nu)$ from raw data')
plt.ylabel(r'$\Delta \tilde{G}(\nu)(cm^{-1})$', fontsize=size)
plt.xlabel(r'$\nu$', fontsize=size)
plt.legend(loc='best', fontsize=size)
#plt.savefig('I_2_Birge_Sponer.png', dpi=900)
plt.legend(loc='best')

#============================================================================#
summer=0
for i in range(0,len(v)-1):
    b_1 = del_E[i]
    b_2 = del_E[i+1]
    h = v[i+1]-v[i]
    summer = .5*(b_1+b_2)*h + summer
print(r'$\tilde{D}_e$ for $I_2$ raw: ',summer, r'$(cm^{-1})$')

summer=0
for l in range(0,len(LR.my_fit(v_lin))):
    b_1 = LR.my_fit(v_lin)[i]
    b_2 = LR.my_fit(v_lin)[i+1]
    h = v_lin[i+1]-v_lin[i]
    summer = .5*(b_1+b_2)*h + summer
print(r'$\tilde{D}_e$ for $I_2$ extrapolated: ',summer, r'$(cm^{-1})$')
#============================================================================#


#============================================================================#
w_n = []

lines = np.loadtxt('Br2_mins.txt', delimiter=',')
for line in lines:
    w_n.append(1e7/line[0])
    
del_E = []
for i in range(0,len(w_n)):
    if i == len(w_n)-1:
        break
    else:
        del_E.append(w_n[i+1]-w_n[i])

v = np.linspace(0,len(w_n)-1,len(w_n)-1)
#============================================================================#
x_int=102
v_lin = np.linspace(0,x_int,x_int)
LR.linear_regression(v,del_E)

fig = plt.figure(2,figsize=(10,8))
plt.title('Birge-Sponer Plot for $Br_2$', fontsize=15)
plt.plot(v_lin,LR.my_fit(v_lin), color='black', label=r'$\Delta \tilde{G}(\nu)$ from linear regression')
plt.scatter(v,del_E, color ='m', label=r'$\Delta \tilde{G}(\nu)$ from raw data')
plt.ylabel(r'$\Delta \tilde{G}(\nu)(cm^{-1})$', fontsize=size)
plt.xlabel(r'$\nu$', fontsize=size)
plt.legend(loc='best', fontsize=size)
#plt.savefig('Br_2_Birge_Sponer.png', dpi=900)
plt.legend(loc='best')

#============================================================================#
summer=0
for i in range(0,len(v)-1):
    b_1 = del_E[i]
    b_2 = del_E[i+1]
    h = v[i+1]-v[i]
    summer = .5*(b_1+b_2)*h + summer
print(r'$\tilde{D}_e$ for $Br_2$ raw: ',summer, r'$(cm^{-1})$')

summer=0
for l in range(0,len(LR.my_fit(v_lin))):
    b_1 = LR.my_fit(v_lin)[i]
    b_2 = LR.my_fit(v_lin)[i+1]
    h = v_lin[i+1]-v_lin[i]
    summer = .5*(b_1+b_2)*h + summer
print(r'$\tilde{D}_e$ for $Br_2$ extrapolated: ',summer, r'$(cm^{-1})$')
#============================================================================#
