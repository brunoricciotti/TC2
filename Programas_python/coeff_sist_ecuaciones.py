# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 02:32:27 2022

Resuelve sistemas de ecuaciones y te grafica los polos y ceros

@author: bruno
"""

from sympy import  *
import numpy as np
from sympy.abc import s
from IPython.display import display, Math
from splane import pzmap, GroupDelay, bodePlot
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt

a, b, c, d, e = symbols("a,b,c,d,e")

ec1 = Eq(a, 0.51)
ec2 = Eq(e,1)
ec3 = Eq(2*a*c - b*b, 0)
ec4 = Eq(-2*d*b + c*c +2*a*e, 0)
ec5 = Eq(2*c*e -d*d, 0)

respuesta = solve([ec1,ec2,ec3,ec4,ec5],a,b,c,d,e)#Salen varios resultados

coeff = [a,b,c,d,e]

#Uso el que me da raices  complejas conjugadas     

for i in range(4):
    if all((np.roots(respuesta[i]).real) < 0) :
        coeff = list(respuesta[i])
        my_roots = np.roots(respuesta[i])
        
coeff = eval(str(coeff))
my_tf = TransferFunction( [1], coeff )

pzmap(my_tf, 4) #S plane pole/zero plot      