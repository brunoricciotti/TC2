# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:37:54 2022

@author: bruno
"""

# Inicialización e importación de módulos

# Módulos para Jupyter
import warnings
warnings.filterwarnings('ignore')

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from splane import pzmap, GroupDelay, bodePlot, plot_plantilla, analyze_sys
from scipy.signal import TransferFunction


fig_sz_x = 10
fig_sz_y = 7
fig_dpi = 100 # dpi

fig_font_size = 16

mpl.rcParams['figure.figsize'] = (fig_sz_x,fig_sz_y)
plt.rcParams.update({'font.size':fig_font_size})


fs = 1000 # Hz
nyq_frec = fs / 2

# Plantilla

# filter design
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)

bp_sos_butter = sig.iirdesign([frecs[2],frecs[3]],[frecs[1],frecs[4]],ripple,atenuacion,analog=False,ftype='butter',output='sos')

num,den = sig.iirdesign([frecs[2],frecs[3]],[frecs[1],frecs[4]],ripple,atenuacion,analog=False,ftype='butter',output='ba')

w  = np.append(np.logspace(-1, 0.8, 250), np.logspace(0.9, 1.6, 250) )
w  = np.append(w, np.linspace(110, nyq_frec, 100, endpoint=True) ) / nyq_frec * np.pi

w = [*range(0,1, )]
H = sig.sosfreqz(bp_sos_butter, 2048)

# w = w / np.pi * nyq_frec

# plt.figure()

# plt.plot(w, 20*np.log10(np.abs(H[1])+1e-12), label='IIR-Butter {:d}'.format(bp_sos_butter.shape[0]*2) )
  

# plot_plantilla(filter_type = 'bandpass', fpass = frecs[[2, 3]]* nyq_frec, ripple = ripple , fstop = frecs[ [1, 4] ]* nyq_frec, attenuation = atenuacion, fs = fs)


# my_dig_filter = sig.TransferFunction(num,den,dt = 1/fs) #al indicar dt le decimos a la funcion que la transferencia es en Z
# analyze_sys(my_dig_filter,'filtro',digital = False)

