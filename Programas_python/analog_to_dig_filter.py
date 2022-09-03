# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:40:55 2022

@author: bruno
"""

#Este script sirve para obtener la version digital de un filtro analogico

import numpy as np
import math as m
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt
from splane import analyze_sys, pretty_print_bicuad_omegayq


wo =2*np.pi*6e3
fs = 100e3 #frecuencia de muestreo

num_s = [1,0,0] #numerador de filtro analogico
den_s = [1,wo*np.sqrt(2),wo**2] #denominador de filtro analogico

num_z,den_z = sig.bilinear(num_s,den_s,fs = fs) #transformo a digital

my_dig_filter = sig.TransferFunction(num_z,den_z,dt = 1/fs) #al indicar dt le decimos a la funcion que la transferencia es en Z
analyze_sys(my_dig_filter,'filtro')


