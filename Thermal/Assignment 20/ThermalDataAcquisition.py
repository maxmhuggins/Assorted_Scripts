# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 05:09:39 2019

@author: maxhu
"""
import numpy as np
import scipy.special as sp

def mult(n,k):
    return sp.binom(n,k)

def sk(l):
    return np.log(l)

def centered_difference(function,new_values):
    count = 0
    for l in range(len(function)):
        if count + 1 >= len(function):
            new_values.append(1)
            break
        if count < 1:
            new_values.append(1)
        else:
            new_values.append(function[l+1] - function[l-1])
        count = count + 1
