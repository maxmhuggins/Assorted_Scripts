# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:54:29 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:49:21 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:03:43 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

rate,data = wavfile.read('B.wav')
print('The data rate is = ', rate)
print('The shape of the data file is =',data.shape)
print('The data type is = ',data.dtype)
data_scaled = []
for element in data:
    data_scaled.append(element/(2**16.0))
    
plt.xlim(1,100000)
data_fft_abs = abs(fft(data_scaled))
d = len(data_fft_abs)/2
plt.plot(data_fft_abs, 'r')
plt.show()
index_value = np.where(data_fft_abs == np.max(data_fft_abs))
print(index_value)
plt.savefig('Flyback_discharge.png', dpi=300)


#Set some values for waveform
k = np.arange(len(data_fft_abs))
T = len(data_fft_abs)/rate
freqlabel = k/T
plt.xlim(0,20000)

plt.plot(freqlabel, data_fft_abs, 'r')
plt.show()
plt.savefig('FlybackDischargefull.png', dpi=300)
