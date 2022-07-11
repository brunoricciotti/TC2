# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 19:40:53 2022

@author: bruno
"""

import numpy as np
import math

amax = 0.5
amin = 20

w0 = 1
ws = 2

ep = math.sqrt(10**(amax/10) - 1)

n = math.ceil(np.log((10**(amin/10) - 1)/(ep**2))/(np.log(ws)*2)) #N es el primer entero superior

print(f" epsilon = {ep}, orden = {n} ")