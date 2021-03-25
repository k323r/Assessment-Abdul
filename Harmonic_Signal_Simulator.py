# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:10:45 2021

@author: Abdul Hameed
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#time axis
t = np.linspace(0, 1, 201)


#orignal Signal with 1Hz frequency
x = np.sin(2 * np.pi * t)

#Harmonics with 100Hz 200Hz and 300Hz
x1 = np.sin(2 * np.pi * 100 * t)
x2 = np.sin(2 * np.pi * 200 * t)
x3 = np.sin(2 * np.pi * 300 * t)

#Signal with Harmonics
xh = x + x1 + x2 + x3

#introducing random noise to the Signal with Harmonics
xn = xh + np.random.normal(t)

#Filtering
#Creating a 8th order Low pass butterworth filter
b, a = signal.butter(8, 0.05)

#Applying filter to the noisy signal
y = signal.filtfilt(b, a, xn)

#Plotting
plt.figure()
plt.plot(t, xh, 'r', label='Orignal Signal')
plt.plot(t,xn, 'b-', label = 'Noisy signal')
plt.plot(t,y, 'r.', markersize = 3, label = 'Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
