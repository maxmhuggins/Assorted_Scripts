# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 05:09:39 2019

@author: maxhu
"""
import numpy as np
import scipy.misc

def mult(n,k):
    return scipy.misc.binom(n,k)

def sigma(n,k):
    num = scipy.misc.factorial(n + k)
    den = scipy.misc.factorial(k)*scipy.misc.factorial(n)
    return num/den

def sk(l):
    return np.log(l)

def centered_difference(function,new_values):
    count = 0
    for l in range(len(function)):
        if count + 1 >= len(function):
            new_values.append(0)
            break
        if count < 1:
            new_values.append(0)
        else:
            new_values.append(function[l+1] - function[l-1])
        count = count + 1
