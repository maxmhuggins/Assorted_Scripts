# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:19:51 2019

@author: maxhu
"""
import pandas as pd

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

columns = list(df) 
  
for i in columns: 
  
    # printing the third element of the column 
    print (df[i][2]) 