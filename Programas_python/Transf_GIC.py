# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 00:50:43 2022

@author: bruno
"""


import sympy as sp
from sympy.abc import s
from IPython.display import display, Math

Vi, Vo, VA, VB = sp.symbols("Vi, Vo, VA, VB")
R1, Z, R2, R5, C = sp.symbols("R1, Z, R2, R5, C")

aa = sp.solve([  #despeja Vi y Vo en base a las ecuaciones (Me quedan en funcion de Vx)
                (Vi - VA)*(1/Z) - VA/R1 + (VB - VA)/R2,
                VA - (VB + Vo)*0.5, 
                (Vo-VA)*(1/Z) + (Vi - VA)*(1/R5)
                ], 
                [Vi, Vo, VA])

transf_func = aa[Vo]/aa[Vi] #Aca defino mi transf_funct como el cociente entre Vo y Vi (Vo/Vi). Tambien es simbolica


# Ejercicio 7.a: Pasatodo de 1er orden

tf7a = transf_func.subs(Z, 1/(s*C)) #reemplazo Y1 e Y2 por sus respectivos valores simbolicos

num, den = sp.fraction(sp.simplify(sp.expand(tf7a)))  #simplificamos y separamos numerador y denominador


num = sp.Poly(num,s)
den = sp.Poly(den,s)


k = sp.simplify(num.LC() / den.LC()) #obtenemos la constante, y la simplificamos

num = num.monic() #hacemos que el numerador y denominador sean monicos
den = den.monic()

den_coeffs = den.all_coeffs()
wo = den_coeffs[-1]

tf7a_final = sp.Mul(k,num/den, evaluate=False)