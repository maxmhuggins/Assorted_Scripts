# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:08:16 2019

@author: maxhu
"""
#============================================================================#
import pandas as pd
import numpy as np
#============================================================================#
test = []
#=====Making some lists with my data====#
def list_maker(path, sheet, column, name_of_list):
    data = pd.read_excel(path, sheet_name = sheet)
    data_list = pd.DataFrame(data, columns= [column])
    lister = []
    lister = data_list.values.tolist()    
    name_of_list[:] = [val for sublist in lister for val in sublist]
#============================================================================#   
path = r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx'
list_maker(path, 'Parallel', 'A', test)
