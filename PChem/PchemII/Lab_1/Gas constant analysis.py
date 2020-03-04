# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:46:19 2020

@author: maxhu
#============================================================================#
mass_mg_l = mass of magnesium low accuracy (g)
mass_mg_h = mass of magnesium high accuracy (g)

V_HCl_l = Volume of HCl low accuracy (mL)
V_HCl_h = Volume of HCl high accuracy (mL)

V_H_2_l = Volume of H2 low accuracy (mL)
V_H_2_h = Volume of H2 high accuracy (mL)

T_H2O_l = Temperature of H2O low accuracy (K)
T_H2O_h = Temperature of H2O high accuracy (K)

P_H2O_l = Vapor pressure of H2O at low accuracy temperature (inHg)
P_H2O_h = Vapor pressure of H2O at high accuracy temperature (inHg)

P_total = Total atmospheric pressure at that time of day (inHg)

inHg_to_Pa = There are 3386.38867 Pascals per inHg. (A conversion factor)

err_XX_l = error in species XX for low accuracy
err_XX_h = error in species XX for high accuracy

mm_Mg = Molar mass of Magnesium (g/mol)
mm_H2 = Molar mass of Hydrogen gas (g/mol)

#============================================================================#
Objectives for this program are to:
    1) Determine the number of moles formed in the reaction of:
        Mg + 2HCl --> MgCL2 + H2
        
    2) Determine the gas constant, R, for two data sets. The high and low
    accuracy data sets for which I will denote the high accuracy R, R_h and
    low accuracy R, R_l.
    
    3) Determine the error propogated within each R. (err_R_h & err_R_l)
    
    4) Use class data to plot volume vs. number of moles for the class set.
    
    5) Determine slope of that line
    
    6) Propogate the error for the slope of the line. 
    
    7) Determine the variance in the data set
    
    8) Perform a q-test on the data to look for outliers
    
    9) After removing outliers, calculate the mean R, the average deviation,
    std dev, and std dev of the mean.
    
    10) Determine if the class mean is statistically different from the
    accepted R using a 95% confidence interval. IOW perform a t-test.
#============================================================================#
"""
#============================================================================#
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#============================================================================#
mass_mg_l = .025
err_mass_mg_l = .001

mass_mg_h = .0510
err_mass_mg_h = .0001

V_HCl_l = 5.0
err_V_HCl_l = .1

V_HCl_h = 5.00
err_V_HCl_h  = .01

V_H2_l = 26.3
err_V_H2_l = .1

V_H2_h = 48.57
err_V_H2_h = .01

T_H2O_l = 293.25
err_T_H2O_l = .01

T_H2O_h = 299.740
err_T_H2O_h = .001

P_H2O_l = 0.69432166
err_P_H2O_l = 0.0000001

P_H2O_h = 1.033603447
err_P_H2O_h = 0.0000001

P_total = 30.16
err_P_total = .01

inHg_to_Pa = 3386.38867 #Pascals per 1 inHg
atm_to_Pa = 101325 #Pascals per 1 atm
C_to_K = 273.15 #K in 1 C

mm_Mg = 24.305
err_mm_Mg = .001

mm_Hg = 2.01588
err_mm_Hg = .00001
#============================================================================#
def error_propogation_for_R(variable_of_interest, list_of_variables, 
                            list_of_errors):
    summer = 0
    for i in range(0,len(list_of_variables)):
        summer = summer + list_of_errors[i]**2 * list_of_variables[i]**2
        
    error_in_measurement = np.sqrt(summer)
    print('The uncertainty in {}: ,'.format(variable_of_interest),
          error_in_measurement)
    
    return error_in_measurement
#============================================================================#
n_Mg_l = mass_mg_l / mm_Mg
n_Mg_h = mass_mg_h / mm_Mg

n_H2_l = n_Mg_l
n_H2_h = n_Mg_h

P_H2_l = P_total - P_H2O_l
P_H2_h = P_total - P_H2O_h

""" 
Using:
    PV = nRT
    R = PV / nT
"""

R_l = (P_H2_l * inHg_to_Pa * (V_H2_l / 1000)*1e-3) / (n_H2_l * T_H2O_l)
R_h = (P_H2_h * inHg_to_Pa * (V_H2_h / 1000)*1e-3) / (n_H2_h * T_H2O_h)
print('R_l= ', R_l)
print('R_h= ', R_h)

R_l_variables_list = [P_total, P_H2O_l, V_H2_l, mass_mg_l, mm_Mg, T_H2O_l]
R_l_errors_list = [err_P_total, err_P_H2O_l, err_V_H2_l, err_mass_mg_l, 
                   err_mm_Mg, err_T_H2O_l]


R_h_variables_list = [P_total, P_H2O_h, V_H2_h, mass_mg_h, mm_Mg, T_H2O_h]
R_h_errors_list = [err_P_total, err_P_H2O_h, err_V_H2_h, err_mass_mg_h, 
                   err_mm_Mg, err_T_H2O_h]

error_propogation_for_R('R_l', R_l_variables_list, R_l_errors_list)
error_propogation_for_R('R_h', R_h_variables_list, R_h_errors_list)

#============================================================================#
data = pd.read_excel (
        r'C:\Users\maxhu\Documents\PChem\PchemII\Lab_1\Lab_1_Gas_Constant.xlsx'
        , sheet_name='Class_data')

df = pd.DataFrame(data, columns= ['mass Mg used (g)'])
temp = df.values.tolist()
mass_mg_h_class  = [val for sublist in temp for val in sublist]

df = pd.DataFrame(data, columns= ['Temp (Celcius)'])
temp = df.values.tolist()
T_H2O_h_class  = [val for sublist in temp for val in sublist]

df = pd.DataFrame(data, columns= ['Volume of H2 (mL)'])
temp = df.values.tolist()
V_H2_h_class  = [val*1e-3*1e-3 for sublist in temp for val in sublist]

df = pd.DataFrame(data, columns= ['P totals (atm)'])
temp = df.values.tolist()
P_total_class  = [val for sublist in temp for val in sublist]

df = pd.DataFrame(data, columns= ['P(H2O)  (atm)'])
temp = df.values.tolist()
P_H2O_h_class  = [val for sublist in temp for val in sublist]

df = pd.DataFrame(data, columns= ['P(H2) (atm)'])
temp = df.values.tolist()
P_H2_h_class  = [val for sublist in temp for val in sublist]
#============================================================================#
""" 
Using:
    PV = nRT
    V(n) = n * (RT / P)
    therefore, the slope is equal to RT / P
    if each n value is multiplied by the corresponding T / P value, then the
    slope is truly R.
    V(n') = n * (T/P) * R
    V(n') = n' * R
"""
n_H2_h_class = []
for i in mass_mg_h_class:
    n_H2_h_class.append(i / mm_Mg)
    
modified_n_values = []
for i in range(0,len(n_H2_h_class)):
    modified_n_values.append(n_H2_h_class[i] * ((T_H2O_h_class[i] + C_to_K) / 
                             (P_H2_h_class[i] * atm_to_Pa)))
#============================================================================#
def linear_regression_plot(x, b, m):
    std_dev = std_err * np.sqrt(len(modified_n_values))
    print('The R value from the slope is: ', m)
    print('The uncertainty in R is: ', std_dev)
    return m*x + b

slope, intercept, r_value, p_value, std_err = stats.linregress(
        modified_n_values,V_H2_h_class)

x_values = np.linspace(1e-6,6.5e-6)

size = 10
fig = plt.figure(1,figsize=(10,6))
fig.suptitle('Volume as a Function of nT/P', fontsize=15)
my_fig = fig.add_subplot(111)
plt.plot(x_values, linear_regression_plot(x_values, intercept, slope), 
         color='black', label='Fit')
plt.scatter(modified_n_values,V_H2_h_class,color='m', label='Class Data')
plt.ylabel('$Volume (m^3)$', fontsize=size)
plt.xlabel('nT/P', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.savefig('Report_1.png', dpi=600)
plt.legend(loc='best')
plt.show
#============================================================================#
q_ref = 0.396

def q_test(data, q_ref):
    data.sort()
    q_exp_lower = (data[1] - data[0]) / (data[len(data)-1] - data[0])
    q_exp_higher = (data[len(data)-1] - 
                         data[len(data)-2]) / (data[len(data)-1] - data[0])
    
    if q_exp_lower > q_ref:
        print('Reject ', data[0])
        return data.remove(data[0])
    else:
        print('Do not reject ', data[0])
        
    if q_exp_higher > q_ref:
        print('Reject ', data[len(data)-1])
        return data.remove(data[len(data)-1])
    else:
        print('Do not reject ', data[len(data)-1])
        
R_class_values = []
for i in range(0,len(V_H2_h_class)):
    R_class_values.append((P_H2_h_class[i] * atm_to_Pa * V_H2_h_class[i]) / 
                          (n_H2_h_class[i] * (T_H2O_h_class[i] + C_to_K)))

q_test(R_class_values, q_ref)
array_for_R_values = np.array(R_class_values)

mean = np.average(array_for_R_values)
def ave_deviation(data):
    summer = 0
    for i in data:
        summer = summer + np.abs(i - mean)
    return (1 / len(data))*summer

average = np.average(array_for_R_values)
average_deviation = ave_deviation(R_class_values)
standard_deviation = np.std(array_for_R_values)
standard_deviation_mean = np.std(array_for_R_values) / np.sqrt(len(
        R_class_values))
print('The mean or average for R is: ', average)
print('The average deviation for R is: ', average_deviation)
print('The standard deviation is: ', standard_deviation)
print('The standard deviation of the mean is: ', standard_deviation_mean)

def t_test(data, known_value, standard_deviation_mean, t_acceptable):
    t = (mean - known_value) / (standard_deviation_mean)
    print('The t-value is: ', t)
    if t > t_acceptable:
        print('Since the calculated t is greater than the 95% confidence '
             ' interval t, the value is statistically different than '
             'the known R.')
    return t
t_acceptable = 1.94
t_test(average, 8.31446261815324, standard_deviation_mean, t_acceptable)
    
