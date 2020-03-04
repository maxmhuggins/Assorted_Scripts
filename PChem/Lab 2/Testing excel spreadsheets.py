# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:00:57 2019

@author: maxhu
"""

import pandas as pd

data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 2\Lab2.xlsx', sheet_name='Parallel')
df = pd.DataFrame(data, columns= ['A'])
test = df.values.tolist()
flattened  = [val for sublist in test for val in sublist]
print(flattened)
