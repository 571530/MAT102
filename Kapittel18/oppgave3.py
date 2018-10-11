# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:37:31 2018

@author: Bruker
"""

# -*- coding: utf-8 -*-
from regression import *
from scipy.optimize import fmin

import matplotlib.pyplot as plt
import numpy as np

X = [6, 11, 14,18 ,23]
Y = [10, 13, 14, 14, 7]
omega = 24
[a0,a1,b1] = sinusoidRegression(X,Y, omega)
plt.figure(1)
plt.scatter(X,Y)
xplot = np.array(list(range(0,25)))
yplot = a0+a1*np.cos(np.multiply(2*np.pi/omega,xplot))+b1*np.sin(np.multiply(2*np.pi/omega,xplot))

plt.plot(xplot,yplot)
Sy2 = sum((Y-np.mean(Y))**2)
SSESinus = sum((Y-(a0+a1*np.cos(np.multiply(2*np.pi/omega,X))+b1*np.sin(np.multiply(2*np.pi/omega,X))))**2)
r2Sinus =(Sy2-SSESinus)/Sy2

# ddx = -a1 * pi / omega * 2 * sin(pi / omega * 2 *  X) + b1 * pi / omega * 2 * cos(pi / omega * 2 * X) 
# ddx = 0, b1 * pi / omega * 2 * cos(pi / omega * 2 *  X) = a1 * pi / omega * 2 * sin(pi / omega * 2 * X)
# b1 / a1 * cos(pi / omega * 2 *  X) = sin(pi / omega * 2 * X)
# b1 / a1 = tan(pi / omega * 2 * X)
# arctan(b1 / a1) = pi / omega * 2 * X + pi * k
# arctan(b1 / a1) * omega / 2 / pi = X + k * omega / 2

x0 = np.arctan(b1 / a1) * omega / 2 / np.pi
x1 = x0 + 1 * omega / 2
x = [x0 , x1] 
y = a0+a1*np.cos(np.multiply(2*np.pi/omega,x))+b1*np.sin(np.multiply(2*np.pi/omega,x))

plt.scatter(x, y)

print(x, y)

print(r2Sinus)
