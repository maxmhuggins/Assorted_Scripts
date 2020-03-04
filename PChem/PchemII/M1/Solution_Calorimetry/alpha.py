# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:59:29 2020

Problem Set #3

@author: maxhu
"""
import numpy as np
#===================Constants================================================#
R = 8.314 #J / mol*K
atmToPascal = 101325 #Pa / 1 atm

#===================Question 1===============================================#
n = 1
T = 27+273
p_i = 3 * atmToPascal
p_f = 1 * atmToPascal

WorkForPartA = - n * R * T * np.log(p_i / p_f)
