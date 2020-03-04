# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:51:13 2018

@author: maxhu
"""
import matplotlib.pyplot as plt
import numpy as np
#Constants

r = 1
c = 1

#Defining transmission angles from snells law
def costhetat(x, c):
    return np.sqrt(np.complex(1.0,0)-(c)**2 * (np.sin(x))**2)
#Function for the complex pressure reflection coefficient
def R(x,c,r):
    n = r - costhetat(x, c)/np.cos(x)
    d = r + costhetat(x, c)/np.cos(x)
    return n/d
#Defining the hypotenous or magnitude from the imaginary and real values for R
def Rmag(x,c,r):
    return np.sqrt(R(x,c,r).real**2 + R(x,c,r).imag**2)
#Defining the phase angle for R
def Rphase(x,c,r):
    return np.arctan2(R(x,c,r).imag, R(x,c,r).real)*180/np.pi


#x_plot = np.arange(0,90)
Thetai_start = 0*np.pi/180
Thetai_end = 90*np.pi/180
num  = 500
thetai = np.linspace(Thetai_start,Thetai_end,num)
Theta_start = 0
Theta_end = 90
theta = np.linspace(Theta_start,Theta_end,num)

fig = plt.figure(1,figsize=(15, 5))
my_fig = fig.add_subplot(1,2,1)
my_fig.plot(theta, Rmag(thetai,.9,.9), color = 'red', label = "$c_2/c_1 = .9$   $r_2/r_1 = .9$")
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Magnitude')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')

my_fig = fig.add_subplot(1,2,2)
my_fig.plot(theta, Rphase(thetai,.9,.9), color = 'red', label = "$c_2/c_1 = .9$   $r_2/r_1 = .9$", linestyle = '--')
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Phase angle')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')


fig = plt.figure(2,figsize=(15, 5))
my_fig = fig.add_subplot(1,2,1)
my_fig.plot(theta, Rmag(thetai,.9,1.1), color = 'orange', label = "$c_2/c_1 = .9$   $r_2/r_1 = 1.1$")
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Magnitude')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')

my_fig = fig.add_subplot(1,2,2)
my_fig.plot(theta, Rphase(thetai,.9,1.1), color = 'orange', label = "$c_2/c_1 = .9$   $r_2/r_1 = 1.1$", linestyle = '--')
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Phase angle')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')


fig = plt.figure(3,figsize=(15, 5))
my_fig = fig.add_subplot(1,2,1)
my_fig.plot(theta, Rmag(thetai,1.1,1.1), color = 'blue', label = "$c_2/c_1 = 1.1$   $r_2/r_1 = 1.1$")
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Magnitude')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')

my_fig = fig.add_subplot(1,2,2)
my_fig.plot(theta, Rphase(thetai,1.1,1.1), color = 'blue', label = "$c_2/c_1 = 1.1$   $r_2/r_1 = 1.1$", linestyle = '--')
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Phase angle')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')


fig = plt.figure(4,figsize=(15, 5))
my_fig = fig.add_subplot(1,2,1)
my_fig.plot(theta, Rmag(thetai,1.1,.9), color = 'green', label = "$c_2/c_1 = 1.1$   $r_2/r_1 = .9$")
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Magnitude')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')

my_fig = fig.add_subplot(1,2,2)
my_fig.plot(theta, Rphase(thetai,1.1,.9), color = 'green', label = "$c_2/c_1 = 1.1$   $r_2/r_1 = .9$", linestyle = '--')
my_fig.set_xlabel('Angle of incidence')
my_fig.set_ylabel('Phase angle')
my_fig.set_title('Pressure Reflection')
plt.legend(loc='best')
