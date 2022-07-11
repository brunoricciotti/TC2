# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:21:11 2022

@author: bruno
"""


import sympy as sp
import numpy as np
from sympy.abc import s
from IPython.display import display, Math

Vi, Vo, VA, VB = sp.symbols("Vi, Vo, VA, VB")
C,R,L1,L2 = sp.symbols("C,R,L1,L2")

Yb = sp.Matrix([[s*C + 1/(s*L2),-1/(s*L2)],[-1/(s*L2),1/R + 1/(s*L2)]])

Ya = sp.Matrix([[1/(s*L1),-1/(s*L1)],[-1/(s*L1),1/(s*L1)]])

Ta = sp.Matrix([[-Ya[3]/Ya[2],-1/Ya[2]],[-Ya.det()/Ya[2],-Ya[0]/Ya[2]]])

Tb = sp.Matrix([[-Yb[3]/Yb[2],-1/Yb[2]],[-Yb.det()/Yb[2],-Yb[0]/Yb[2]]])

Tt = Ta.multiply(Tb) #Hago el producto matricial

display(Tt)