# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:34:05 2018

@author: maxhu
"""

# pythonprogramminglanguage.com
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('qt5agg')

import matplotlib.pyplot as plt
import numpy as np

m_vals = [0, 5, 10, 15, 20, 25, 30]
Resf_nb_vals = [39.1, 37.1, 35.7, 34.7, 31.2, 29.8, 29.0]

# Create random data
x = m_vals
y = Resf_nb_vals

# Create model
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 30, 7)
yfit = model.predict(xfit[:, np.newaxis])

# plot
plt.scatter(x, y)
plt.plot(xfit, yfit);
plt.show()
