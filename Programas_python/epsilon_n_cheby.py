# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 00:22:59 2022

@author: bruno
"""

import numpy as np

f1 = 1000
f2 = 3000
norma_w = f1

f1 = f1/norma_w
f2 = f2/norma_w

alfa_min = 20
alfa_max = 2

epsilon_2 = 10**(alfa_max/10)-1
epsilon = np.sqrt(epsilon_2)
n = np.ceil(np.arccosh((np.sqrt(np.power(10, alfa_min * 0.1)) - 1) / epsilon_2) / (np.arccosh(f2)))

print('Epsilon: {:.4f}'.format(epsilon))
print('Epsilon al cuadrado: {:.4f}'.format(epsilon_2))
print('Orden del filtro: {:0.0f}'.format(n))