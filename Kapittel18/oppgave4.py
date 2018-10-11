# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:09:49 2018

@author: Bruker
"""

import numpy as np

M = np.array([[12, 14, 12, 21], [6, 9, 15, 6]]) # observert
M = M / 95
X = sum(M)

X = np.reshape(X,(1,4))
Y = sum(np.transpose(M))
Y = np.reshape(Y,(2,1))
N = np.dot(Y,X) # fordeling om de er uavhengige

M = 100*np.reshape(M,(8,1))
N = 100*np.reshape(N,(8,1))

Q = sum([(x-y)**2/y for x,y in zip(M,N)])

print(Q[0])

# H0 x og y er uavhengige
# H1 x og y er avhengine
# Q = r2 = kji2_(4-1)(2-1) = kji2_3 = 6.91612
# a = 0.05, påsta h1 om Q > z0.05,3 = 7.81

print("x og y er uavhengige" if Q[0] < 7.81 else "x og y er avhengige") 