# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 02:29:00 2022

@author: bruno
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

k= 1

num = np.array([k*1,7,k*6]) 
den = np.array([1,5, 6])

pretty_print_bicuad_omegayq(num,den)

tf = sig.TransferFunction(num,den)
    
plt.close('all')
analyze_sys(tf, 'TP1')
