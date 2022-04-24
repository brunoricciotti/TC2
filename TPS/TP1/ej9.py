# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:06:23 2022

@author: bruno
"""


import sympy as sp
from sympy.abc import s
from IPython.display import display, Math

Vi, Vo, Vx = sp.symbols("Vi, Vo, Vx")
R1, Z2, R3, R4, Z5, C2, C5 = sp.symbols("R1, Z2, R3, R4, Z5, C2, C5")

aa = sp.solve([  #despeja Vi y Vo en base a las ecuaciones (Me quedan en funcion de Vx)
                Vi/R1 -Vx*((1/R1) + (1/R3) + (1/R4) + (1/Z2)) + Vo/R4, 
                Vx + Vo*(R3/Z5)
                ], 
                [Vi, Vo])

transf_func = aa[Vo]/aa[Vi] #Aca defino mi transf_funct como el cociente entre Vo y Vi (Vo/Vi). Tambien es simbolica


# Ejercicio 7.a: Pasatodo de 1er orden

tf7a = transf_func.subs(Z2, 1/(s*C2)) #reemplazo Y1 e Y2 por sus respectivos valores simbolicos
tf7a = tf7a.subs(Z5, 1/(s*C5))

num, den = sp.fraction(sp.simplify(sp.expand(tf7a)))  #simplificamos y separamos numerador y denominador


num = sp.Poly(num,s)
den = sp.Poly(den,s)


k = sp.simplify(num.LC() / den.LC()) #obtenemos la constante, y la simplificamos

num = num.monic() #hacemos que el numerador y denominador sean monicos
den = den.monic()

den_coeffs = den.all_coeffs()
wo = den_coeffs[-1]

tf7a_final = sp.Mul(k,num/den, evaluate=False)

print('')
print('################')
print('# Ejercicio 9 #')
print('################')
display(tf7a_final)
display(Math( r' \omega_o = ' + sp.latex(wo) ))

#le asigno valores a las variables simbolicas

tf7a_final.subs({R1:1,R3:1,R4:1, C2: 1, C5:0.01})
