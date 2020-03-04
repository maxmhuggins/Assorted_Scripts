# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:32:17 2019

@author: maxhu
"""
#============================================================================#
import pandas as pd
import numpy as np
import LinearRegressionClass as LR
import matplotlib.pyplot as plt
#============================================================================#
path = r'C:\Users\maxhu\Documents\PChem\Lab 3\Report_3.xlsx'

A_1 = []
A_2 = []
A_3 = []

t_1 = []
t_2 = []
t_3 = []
#============================================================================#   
def list_maker(path, sheet, column, name_of_list):
    data = pd.read_excel(path, sheet_name = sheet)
    data_list = pd.DataFrame(data, columns= [column])
    lister = []
    lister = data_list.values.tolist()    
    name_of_list[:] = [val for sublist in lister for val in sublist]
#============================================================================#   
list_maker(path, 'Solution_1', '1/A', A_1)
A_1_array = np.array(A_1)
list_maker(path, 'Solution_2', '1/A', A_2)
A_2_array = np.array(A_2)
list_maker(path, 'Solution_3', '1/A', A_3)
A_3_array = np.array(A_3)

list_maker(path, 'Solution_1', 'Time', t_1)
t_1_array = np.array(t_1)
list_maker(path, 'Solution_2', 'Time', t_2)
t_2_array = np.array(t_2)
list_maker(path, 'Solution_3', 'Time', t_3)
t_3_array = np.array(t_3)
#============================================================================#
fig = plt.figure(1,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Inverse of Absorbance versus Time', fontsize = '15')
   
LR.linear_regression(t_1, A_1)
plt.scatter(t_1, A_1, label = 'Solution 1')
plt.plot(t_1, LR.my_fit(t_1_array), label = '1/A=6.3e-5x+.8', linestyle='-.')

LR.linear_regression(t_2, A_2)
plt.scatter(t_2, A_2, label = 'Solution 2')
plt.plot(t_2, LR.my_fit(t_2_array), label = '1/A=6.5e-5x+.8', linestyle='--')

LR.linear_regression(t_3, A_3)
plt.scatter(t_3, A_3, label = 'Solution 3')
plt.plot(t_3, LR.my_fit(t_3_array), label = '1/A=1.2e-4x+.8')

my_fig.set_xlabel('Time (s)', fontsize = '13')
my_fig.set_ylabel('1/A', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('PCHEML3INVERSEABS', dpi=300)
#============================================================================#