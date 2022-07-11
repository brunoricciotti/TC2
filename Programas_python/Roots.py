# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 02:37:15 2022

@author: bruno
"""

from sympy import  *
import numpy as np
from sympy.abc import s
from IPython.display import display, Math
from splane import pzmap, GroupDelay, bodePlot
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt

coeffs_den=[0,0,0,0,4,0,4,0,2]

root = np.roots(coeffs_den)

display(root)

my_tf = TransferFunction( [1], coeffs_den )

pzmap(my_tf, 4) #S plane pole/zero plot