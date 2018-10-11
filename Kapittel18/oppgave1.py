# -*- coding: utf-8 -*-
from regression import *

import matplotlib.pyplot as plt
import numpy as np

# Oppgave A
#x = [0, 1, 1, 2]
#y = [3, 2, 4, 5]
# Oppgave B 
#x = [-2, -1, 0, 1, 2]
#y = [4.2, 0.8, -0.3, 0.7, 3.7]
# Oppgave C
x = [2, 3, 5, 7]
y = [3.4, 4.3, 8.6, 10]



plt.scatter(x, y)

[a_lin, b_lin] = linearRegression(x, y)

Sy2_lin = sum((y - np.mean(y))**2)
SSE_lin = sum((y - (np.dot(a_lin, x) + b_lin))**2)
R2_lin = (Sy2_lin - SSE_lin) / Sy2_lin

xplot = np.array(list(range(min(x) - 2, max(x) + 3)))
yplot = np.dot(xplot, a_lin) + b_lin

print("Determinantkoeffisient for lineære ", R2_lin)

plt.plot(xplot, yplot)


[a_kva, b_kva, c_kva] = quadraticRegression(x, y)

Sy2_kva = sum((y - np.mean(y))**2)
SSE_kva = sum((y - (np.dot(a_kva, np.power(x, 2)) + np.dot(b_kva, x) + c_kva))**2)
R2_kva = (Sy2_kva - SSE_kva) / Sy2_kva

yplot = np.dot(a_kva, np.power(xplot,2)) + np.dot(b_kva, xplot) + c_kva

print("Determinantkoeffisient for kvadratisk ", R2_kva)

plt.plot(xplot, yplot)


