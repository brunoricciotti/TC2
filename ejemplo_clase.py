# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:08:40 2022

@author: bruno
"""
from sympy import  *
import numpy as np
from sympy.abc import s
from IPython.display import display, Math
from splane import pzmap, GroupDelay, bodePlot
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import math as m

w,T=symbols("w,T")
T = 1/(1+((0.259))*(8*w**4 - 8*w**2 +1)**2)


num, den = fraction(simplify(expand(T)))  #simplificamos y separamos numerador y denominador

display(T)

num = Poly(num,s)
den = Poly(den,s)

T = num/den
display(T)

coeff = (den.all_coeffs())

