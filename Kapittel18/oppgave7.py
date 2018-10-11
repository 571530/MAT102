# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:32:07 2018

@author: Bruker
"""

import numpy as np
import scipy as sp

n = 3
p = 0.2

# Oppgave A
expected = []

for k in range(0, n + 1) : # passe på å få med k=n
    expected.append(sp.special.binom(n, k) * np.power(p, k) * np.power((1-p), n-k))

print(expected)

# Oppgave B

N = list(map(lambda x: round(x * 100), expected))

M = [55, 37, 8, 0]

Q = sum([(x - y)**2 / y for x, y in zip(M, N)])

print(Q)

# Oppgave C

# z0.05,3 = 7.81.

# H0 målingen følger referansetabellen
# H1 målingen følger ikke referansetabellen
# Påstå H1 om Q > z0.05,3

print(Q < 7.81) # Om målingen følger referansetabellen
