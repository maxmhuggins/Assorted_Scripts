# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:41:40 2019

@author: maxhu
"""
#============================Modules=========================================#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
plt.style.use('seaborn-whitegrid')
#=========================Constants==========================================#

#===Parallel==========#
A_0 = 100
k_1p = 1/6
k_2p = 2/6
k_T = .5
#====Reversible=======#
k_1r = 2/6
k_2r = 1/6
#====Consecutive=pt.1==#
k_1c1 = 5/6
k_2c1 = 1/6
#====Consecutive=pt.2==#
k_1c2 = 1/6
k_2c2 = 5/6

#============================Functions=======================================#

#===Parallel==========#

def AP(t):  
    return A_0 * np.exp(-k_T * t)
def BP(t):
    return (k_1p / k_T) * A_0 * (1 - np.exp(-k_T * t))
def CP(t):
    return (k_2p / k_T) * A_0 * (1 - np.exp(-k_T * t))

#====Reversible=======#

def AR(t): 
    num = A_0 * (k_2r + k_1r * np.exp((-k_1r - k_2r) * t))
    den = k_1r + k_2r
    return num / den
def BR(t):
    num = k_1r * A_0 * (1 - np.exp((-k_1r - k_2r) * t))
    den = k_1r + k_2r
    return num / den

#====Consecutive=pt.1==#

def AC1(t):  
    return A_0 * np.exp(-k_1c1 * t)
def BC1(t):
    num = k_1c1 * A_0 * (np.exp(-k_1c1 * t) - np.exp(-k_2c1 * t))
    den = k_2c1 - k_1c1
    return num / den
def CC1(t):
    return A_0 * (1 - (k_1c1 / (k_2c1 - k_1c1)) 
                  * (np.exp(-k_1c1 * t) - np.exp(-k_2c1 * t)) 
                  - np.exp(-k_1c1 * t))

#====Consecutive=pt.2==#
    
def AC2(t):  
    return A_0 * np.exp(-k_1c2 * t)
def BC2(t):
    return (k_1c2 / k_2c2) * A_0 * (np.exp(-k_1c2 * t) - np.exp(-k_2c2 * t))
def CC2(t):
    return A_0 - A_0 * np.exp(-k_1c2 * t) - (k_1c2 / k_2c2) * A_0 * (np.exp(
            -k_1c2 * t) - np.exp(-k_2c2 * t))

#====Fitting===========#
def AP_FIT(x, c):
    return 100 * np.exp(-c*x)

def BP_FIT(x, a, c):
    return a *100 * (1 - np.exp(-c*x))

def CP_FIT(x, a, c):
    return a *100 * (1 - np.exp(-c*x))
#======================#
def AR_FIT(x, a, b):
    return (100 / (a + b)) * (b + a * np.exp((-a - b) * x))

def BR_FIT(x, a, b, c):
    return (a * 100 * (1 - np.exp((-a - b) * x))) / (a + b)
#======================#
def AC_FIT(x, a):
    return 100 * np.exp(-a*x)

def BC_FIT(x, b):
    return (0.83333333 / (b - 0.83333333)) * 100 * (
            np.exp(-0.83333333 * x) - np.exp(-b * x))

def CC_FIT(x, b):
    return 100 * (1 - (0.83333333 / (b - 0.83333333)) * (
            np.exp(-0.83333333 * x) - np.exp(-b * x)) - 
        np.exp(-0.83333333 * x))
#======================#
def AC_FIT2(x, a):
    return 100 * np.exp(-a*x)

def BC_FIT2(x, b):
    return (.16666667 / (b - .16666667)) * 100 * (
            np.exp(-.16666667 * x) - np.exp(-b * x))

def CC_FIT2(x, b):
    return 100 * (1 - (.16666667 / (b - .16666667)) * (
            np.exp(-.16666667 * x) - np.exp(-b * x)) - 
        np.exp(-.16666667 * x))

#==================================Data======================================#

Par_data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx', 
                      sheet_name='Parallel')
Rev_data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx', 
                      sheet_name='Reversible')
Cons1_data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx', 
                      sheet_name='Consecutive pt. 1')
Cons2_data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx', 
                      sheet_name='Consecutive pt. 2')

#=====Making some lists with my data====#

A_p = pd.DataFrame(Par_data, columns= ['A'])
B_p = pd.DataFrame(Par_data, columns= ['B'])
C_p = pd.DataFrame(Par_data, columns= ['C'])

A_p = A_p.values.tolist()
B_p = B_p.values.tolist()
C_p = C_p.values.tolist()

A_p  = [val for sublist in A_p for val in sublist]
B_p  = [val for sublist in B_p for val in sublist]
C_p  = [val for sublist in C_p for val in sublist]

#=========#

A_r = pd.DataFrame(Rev_data, columns= ['A'])
B_r = pd.DataFrame(Rev_data, columns= ['B'])

A_r = A_r.values.tolist()
B_r = B_r.values.tolist()

A_r  = [val for sublist in A_r for val in sublist]
B_r  = [val for sublist in B_r for val in sublist]

#=========#

A_c1 = pd.DataFrame(Cons1_data, columns= ['A'])
B_c1 = pd.DataFrame(Cons1_data, columns= ['B'])
C_c1 = pd.DataFrame(Cons1_data, columns= ['C'])

A_c1 = A_c1.values.tolist()
B_c1 = B_c1.values.tolist()
C_c1 = C_c1.values.tolist()

A_c1  = [val for sublist in A_c1 for val in sublist]
B_c1  = [val for sublist in B_c1 for val in sublist]
C_c1  = [val for sublist in C_c1 for val in sublist]

#=========#

A_c2 = pd.DataFrame(Cons2_data, columns= ['A'])
B_c2 = pd.DataFrame(Cons2_data, columns= ['B'])
C_c2 = pd.DataFrame(Cons2_data, columns= ['C'])

A_c2 = A_c2.values.tolist()
B_c2 = B_c2.values.tolist()
C_c2 = C_c2.values.tolist()

A_c2  = [val for sublist in A_c2 for val in sublist]
B_c2  = [val for sublist in B_c2 for val in sublist]
C_c2  = [val for sublist in C_c2 for val in sublist]


#===========================Plotting=========================================#

#======Parallel=========#
t_values = np.linspace(0, 8)
t_data = np.linspace(0, 8, 9)

fig = plt.figure(1,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Parallel Reactions', fontsize = '15')
#Computational Values
plt.plot(t_values, AP(t_values), color = 'r', label = 'Computational [A]', 
         linestyle = '--')
plt.plot(t_values, BP(t_values), color = 'g', label = 'Computational [B]', 
         linestyle = '--')
plt.plot(t_values, CP(t_values), color = 'b', label = 'Computational [C]', 
         linestyle = '--')
#Actual Data
plt.plot(t_data, A_p, color = 'r', label = 'Data [A]')
plt.plot(t_data, B_p, color = 'g', label = 'Data [B]')
plt.plot(t_data, C_p, color = 'b', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2PARALLEL', dpi=300)

#=====Reversible========#

t_values = np.linspace(0, 8)
t_data = np.linspace(0, 9, 10)

fig = plt.figure(2,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Reversible Reactions', fontsize = '15')
#Computational Values
plt.plot(t_values, AR(t_values), color = 'r', label = 'Computational [A]', 
         linestyle = '--')
plt.plot(t_values, BR(t_values), color = 'g', label = 'Computational [B]', 
         linestyle = '--')
#Actual Data
plt.plot(t_data, A_r, color = 'r', label = 'Data [A]')
plt.plot(t_data, B_r, color = 'g', label = 'Data [B]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2REVERSIBLE', dpi=300)

#=====Consecutive 1=====#

t_values = np.linspace(0, 24)
t_data = np.linspace(0, 24, 25)

fig = plt.figure(3,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Consecutive Reactions Part 1', fontsize = '15')
#Computational Values
plt.plot(t_values, AC1(t_values), color = 'r', label = 'Computational [A]', 
         linestyle = '--')
plt.plot(t_values, BC1(t_values), color = 'g', label = 'Computational [B]', 
         linestyle = '--')
plt.plot(t_values, CC1(t_values), color = 'b', label = 'Computational [C]', 
         linestyle = '--')
#Actual Data
plt.plot(t_data, A_c1, color = 'r', label = 'Data [A]')
plt.plot(t_data, B_c1, color = 'g', label = 'Data [B]')
plt.plot(t_data, C_c1, color = 'b', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2CONSECUTIVE1', dpi=300)

#=====Consecutive 2======#

t_values = np.linspace(0, 57)
t_data = np.linspace(0, 57, 58)

fig = plt.figure(4,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Consecutive Reactions Part 2', fontsize = '15')
#Computational Values
plt.plot(t_values, AC2(t_values), color = 'r', label = 'Computational [A]', 
         linestyle = '--')
plt.plot(t_values, BC2(t_values), color = 'g', label = 'Computational [B]', 
         linestyle = '--')
plt.plot(t_values, CC2(t_values), color = 'b', label = 'Computational [C]', 
         linestyle = '--')
#Actual Data
plt.plot(t_data, A_c2, color = 'r', label = 'Data [A]')
plt.plot(t_data, B_c2, color = 'g', label = 'Data [B]')
plt.plot(t_data, C_c2, color = 'b', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2CONSECUTIVE2', dpi=300)

#============================================================================#

#===========================Plotting=best fit lines with data================#

#======Parallel=========#
t_values = np.linspace(0, 8)
t_data = np.linspace(0, 8, 9)
#Fits
popt, pcov = curve_fit(AP_FIT, t_data, AP(t_data))

fig = plt.figure(5,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Parallel Reactions Fit Functions', fontsize = '15')
#Computational Values
plt.plot(t_data, AP_FIT(t_data, *popt), color = 'c', label = 'Fit for [A]', 
         linestyle = '--')
print(popt)
popt, pcov = curve_fit(BP_FIT, t_data, BP(t_data))

plt.plot(t_data, BP_FIT(t_data, *popt), color = 'k', label = 'Fit for [B]', 
         linestyle = '--')
print(popt)

popt, pcov = curve_fit(CP_FIT, t_data, CP(t_data))

plt.plot(t_data, CP_FIT(t_data, *popt), color = 'm', label = 'Fit for [C]', 
         linestyle = '--')
print(popt)

#Actual Data
plt.scatter(t_data, A_p, color = 'c', label = 'Data [A]')
plt.scatter(t_data, B_p, color = 'k', label = 'Data [B]')
plt.scatter(t_data, C_p, color = 'm', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2PARALLELFITS', dpi=300)

#=====Reversible========#

t_values = np.linspace(0, 8)
t_data = np.linspace(0, 9, 10)

popt, pcov = curve_fit(AR_FIT, t_data, AR(t_data))

fig = plt.figure(6,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Parallel Reactions Fit Functions', fontsize = '15')
#Computational Values
plt.plot(t_data, AR_FIT(t_data, *popt), color = 'c', label = 'Fit for [A]', 
         linestyle = '--')
print(popt)
popt, pcov = curve_fit(BR_FIT, t_data, BR(t_data))

plt.plot(t_data, BR_FIT(t_data, *popt), color = 'k', label = 'Fit for [B]', 
         linestyle = '--')
print(popt)

#Actual Data
plt.scatter(t_data, A_r, color = 'c', label = 'Data [A]')
plt.scatter(t_data, B_r, color = 'k', label = 'Data [B]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2REVERSIBLEFITS', dpi=300)

#=====Consecutive 1=====#

t_values = np.linspace(0, 24)
t_data = np.linspace(0, 24, 25)

popt, pcov = curve_fit(AC_FIT, t_data, AC1(t_data), maxfev=4000)

fig = plt.figure(7,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Parallel Reactions Fit Functions', fontsize = '15')
#Computational Values
plt.plot(t_data, AC_FIT(t_data, *popt), color = 'c', label = 'Fit for [A]', 
         linestyle = '--')
print(popt)
popt, pcov = curve_fit(BC_FIT, t_data, BC1(t_data), maxfev=4000)

plt.plot(t_data, BC_FIT(t_data, *popt), color = 'k', label = 'Fit for [B]', 
         linestyle = '--')
print(popt)

popt, pcov = curve_fit(CC_FIT, t_data, CC1(t_data), maxfev=2000)

plt.plot(t_data, CC_FIT(t_data, *popt), color = 'm', label = 'Fit for [C]', 
         linestyle = '--')
print(popt)


#Actual Data
plt.scatter(t_data, A_c1, color = 'c', label = 'Data [A]')
plt.scatter(t_data, B_c1, color = 'k', label = 'Data [B]')
plt.scatter(t_data, C_c1, color = 'm', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2CONSECUTIVE1FITS', dpi=300)

#=====Consecutive 2=====#

t_values = np.linspace(0, 57)
t_data = np.linspace(0, 57, 58)

popt, pcov = curve_fit(AC_FIT2, t_data, AC2(t_data), maxfev=4000)

fig = plt.figure(8,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Parallel Reactions Fit Functions', fontsize = '15')
#Computational Values
plt.plot(t_data, AC_FIT2(t_data, *popt), color = 'c', label = 'Fit for [A]', 
         linestyle = '--')
print(popt)
popt, pcov = curve_fit(BC_FIT2, t_data, BC2(t_data), maxfev=4000)

plt.plot(t_data, BC_FIT2(t_data, *popt), color = 'k', label = 'Fit for [B]', 
         linestyle = '--')
print(popt)

popt, pcov = curve_fit(CC_FIT2, t_data, CC2(t_data), maxfev=2000)

plt.plot(t_data, CC_FIT2(t_data, *popt), color = 'm', label = 'Fit for [C]', 
         linestyle = '--')
print(popt)


#Actual Data
plt.scatter(t_data, A_c2, color = 'c', label = 'Data [A]')
plt.scatter(t_data, B_c2, color = 'k', label = 'Data [B]')
plt.scatter(t_data, C_c2, color = 'm', label = 'Data [C]')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('Concentration (M/# of Dice)', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2CONSECUTIVE2FITS', dpi=300)

#============================================================================#

t_values = np.linspace(0, 8)
t_data = np.linspace(0, 8, 9)
BC = []
length = len(B_p)
for i in range(length):
    BC.append(B_p[i]/C_p[i])
#Fits

fig = plt.figure(9,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Is [B]/[C] = to $k_1/k_2$?', fontsize = '15')
#Computational Values
plt.ylim(0,.9)
plt.plot(t_values, BP(t_values)/CP(t_values), color = 'k', label = '[B]/[C] Analytical')
plt.scatter(t_data, BC, color = 'g', label = '[B]/[C] Simulation Data')
my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('[B]/[C]', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML2PARALLELBC', dpi=300)
