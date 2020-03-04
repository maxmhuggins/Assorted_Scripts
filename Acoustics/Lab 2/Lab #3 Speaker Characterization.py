## -*- coding: utf-8 -*-
#"""
#Created on Mon Oct  1 23:28:41 2018
#
#@author: maxhu
#"""
#import matplotlib.pyplot as plt
#import numpy as np
#from scipy import stats
#
##Data for Effective Mass and Stiffness
m_vals = [0,5,10,15,20,25,30]
Resf_nb_vals = [39.1,37.1,35.7,34.7,31.2,29.8,29.0]
Resf_b_nof_vals = [86.7,81.0,75.3,72.3,68.5,65.4,62.7]
Resf_b_f_vals = [80.6,74.2,71.5,66.7,63.2,60.1,56.4]

##Data for Mechanical Resistance
t_elapsed_vals = [6.4,19.2,32,44.8,56.8,68.8,80.8,93.6,105,118,131,142,154,168]
V_mag_vals = [568,-344,288,-184,152,-88,88,-48,48,-32,40,-32,24,16]
#
##Defining x and y for scatter plot
#x = m_vals
#y = Resf_nb_vals
##Making a scatter plot for no box resonant values
#def Scat_no_box(x, y, graph_filepath):
#    '''
#    http://stackoverflow.com/a/34571821/395857
#    x does not have to be ordered.
#    '''
#    # Scatter plot
#    plt.scatter(x, y)
#
#    # Add correlation line
#    axes = plt.gca()
#    m, b = np.polyfit(x, y, 1)
#    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
#    plt.plot(X_plot, m*X_plot + b, '-')
#
#    # Save figure
#    plt.savefig(graph_filepath, dpi=300, format='png', bbox_inches='tight')
#
#    # Plot
#Scat_no_box(x, y, 'scatter_plot.png')
#
#slope, intercept, r_value, p_value, std_err = stats.linregress(x['total_bill'],y['tip'])
#
## use line_kws to set line label for legend
#ax = sns.regplot(x="total_bill", y="tip", data=x, color='b', 
# line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})
#
## plot legend
#ax.legend()
#
#plt.show()

# pythonprogramminglanguage.com
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('qt5agg')

import matplotlib.pyplot as plt
import numpy as np

# Create random data
x = m_vals
y = Resf_nb_vals

# Create model
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 50, .1)
yfit = model.predict(xfit[:, np.newaxis])

# plot
plt.scatter(x, y)
plt.plot(xfit, yfit);
plt.show()
