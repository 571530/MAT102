# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:31:17 2018

@author: Bruker
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:22:03 2018

@author: Bruker
"""

from scipy.special import erf
import numpy as np

def less_than (x, u, sigma) :
    return 0.5 + 0.5 * erf((x-u) / (sigma * np.sqrt(2)))

def bigger_than (x, u, sigma) :
    return 1 - less_than(x, u, sigma)

def interval (x0, x1, u, sigma) :
    return less_than(x1, u, sigma) - less_than(x0, u, sigma)

print(1.2, less_than(1.2, 0, 2))

print(0.3, bigger_than(0.3, 0, 2))

print(-0.2, 1.5, interval(-0.2, 1.5, 0, 2))