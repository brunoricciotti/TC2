# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 02:29:00 2022

@author: bruno
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

w = 2*np.pi*10000

num = np.array([15]) 
den = np.array([1,6,15,15])


tf = sig.TransferFunction(num,den)
    
plt.close('all')
analyze_sys(tf, 'TP1')
