# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:22:03 2018

@author: Bruker
"""

from scipy.special import erf
import numpy as np

def less_than (x) :
    return 0.5 + 0.5 * erf(x / np.sqrt(2))

def bigger_than (x) :
    return 1 - less_than(x)

def interval (x0, x1) :
    return less_than(x1) - less_than(x0)

print(1.2, less_than(1.2))

print(0.3, bigger_than(0.3))

print(-0.2, 1.5, interval(-0.2, 1.5))