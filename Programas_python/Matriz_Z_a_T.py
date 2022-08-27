# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:50:50 2022

@author: bruno
"""



import sympy as sp
import numpy as np
from sympy.abc import s
from IPython.display import display, Math

Vi, Vo, VA, VB = sp.symbols("Vi, Vo, VA, VB")
C,R,L1,L3 = sp.symbols("C,R,L1,L3")

Za = sp.Matrix([[s*L1 + 1/(s*C),1/(s*C)],[1/(s*C),s*L3 + 1/(s*C)]])

Zb = sp.Matrix([[R,R],[R,R]])

Ta = sp.Matrix([[Za[0]/Za[2],Za.det()/Za[2]],[1/Za[2],Za[3]/Za[2]]])

Tb = sp.Matrix([[Zb[0]/Zb[2],Zb.det()/Zb[2]],[1/Zb[2],Zb[3]/Zb[2]]])

Tt = Ta.multiply(Tb) #Hago el producto matricial

display(Tt)