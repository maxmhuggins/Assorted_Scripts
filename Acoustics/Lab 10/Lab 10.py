# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:03:43 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

def DFT(f_n):
    N = len(f_n)
    f_k = np.zeros((N), dtype=np.complex128)
    j = complex(0,1)
    for k in range(N):
        for n in range(N):
            f_k[k] += f_n[n]*np.exp(-2.0*np.pi*j*n*k/N)
            
    return f_k

#Set some values for waveform
k_val_1 = 10
k_val_2 = 3
const = 5
N = 1000
t_initial = 0
t_final = 1
t = np.linspace(t_initial, t_final, N, endpoint = False)
data = const + np.cos(2*np.pi*k_val_1*t) + 2*np.sin(2*np.pi*k_val_2*t)
fig = plt.figure()
my_fig = fig.add_subplot(1,1,1)
plt.plot(t, data, color = 'black')
my_fig.set_xlabel('Amplitude')
my_fig.set_ylabel('time (s)')
my_fig.set_title('Wavefom')
plt.savefig('DFT_1_waveform.png', dpi=300)
plt.show()
plt.close()

fk_real = DFT(data).real
fk_imag = DFT(data).imag

fig = plt.figure()
my_fig = fig.add_subplot(1,1,1)
index_values = range(len(data))
plt.plot(index_values, fk_real, color='red')
plt.plot(index_values, fk_imag, color='blue')
my_fig.set_xlabel('index value')
my_fig.set_ylabel('counts')
my_fig.set_title('Discrete Fourier Transform')
plt.savefig('DFT_1_real_imag.png', dpi=300)
plt.show()
plt.close()

fk_mag = np.abs(DFT(data))
rate = len(data)/(t_final - t_initial)
k = np.arange(len(data))
T = len(data)/rate
freq_values = k/T

fig = plt.figure()
my_fig = fig.add_subplot(1,1,1)
index_values = range(len(data))
plt.plot(freq_values[0:20], fk_mag[0:20], color='green')
plt.plot(index_values, fk_imag, color='blue')
my_fig.set_xlabel('index value')
my_fig.set_ylabel('counts')
my_fig.set_title('Discrete Fourier Transform')
plt.savefig('DFT_1_mag.png', dpi=300)
plt.show()
plt.close()
