# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:45:26 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
#constants
A1 = 1
phase1 = 0
x01 = 0
y01 = 0.5
j =np.complex(0,1)
freq = 1
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)
#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = .5
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 1
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 2
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 3
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
phase2 = np.pi
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = .5
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
phase2 = np.pi
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 1
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
phase2 = np.pi
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 2
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
phase2 = np.pi
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
j =np.complex(0,1)
freq = 3
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
    return np.real(p20)

#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
#constants
A1 = 1
phase1 = 0
phase2 = np.pi
phase3 = np.pi/2
x01 = 0
y01 = 0.5
x02 = 0
y02 = -0.5
x03 = .24
y03 = .42
j =np.complex(0,1)
freq = 2
omega = 2*np.pi*freq
c = 1
k = omega / c

#Define acoustic pressure amplitudes
def pl(x,y,t):
    r = np.sqrt((x-x01)**2 + (y-y01)**2)
    p10 = (A1)*np.exp(j*(omega*t - k*r + phase1))
    return np.real(p10)

def p2(x,y,t):
    r = np.sqrt((x-x02)**2 + (y-y02)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase2))
    return np.real(p20)
def p3(x,y,t):
    r = np.sqrt((x-x03)**2 + (y-y03)**2)
    p20 = (A1)*np.exp(j*(omega*t - k*r + phase3))
    return np.real(p20)


#Making XY grid points
N = 100
x_values = np.linspace(-5, 5, N)
y_values = np.linspace(-5, 5, N)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'spherical_source_contour_filled.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Spherical Source')
Z = pl(X,Y,t=0) + p2(X,Y,t=0) + p3(X,Y,t=0)
n_lines = 100
plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
