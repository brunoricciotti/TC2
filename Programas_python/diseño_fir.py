# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:34:01 2022

@author: bruno
"""

from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np

cant_coef = 1111

#####################
## tipos de filtro ##
#####################

#tipo_filtro = 'lp' # pasa bajo
#tipo_filtro = 'hp' # pasa alto
tipo_filtro = 'bp' # pasa banda
#tipo_filtro = 'bs'  # elimina banda

# plantilla
ripple = 0.5 # dB
atenuacion = 40 # dB

fs = 1000 # Hz
nyq_frec = fs / 2

ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz


if tipo_filtro == 'lp':
    # pasa bajo
    frecs = [0.0,  0.5,     0.8,          1.0]
    gains = [0,   -ripple, -atenuacion,   -atenuacion] # dB

elif tipo_filtro == 'hp':
    # pasa alto
    frecs = [0.0,         0.5,     1.0]
    gains = [-atenuacion, -ripple, 0.0] # dB

elif tipo_filtro == 'bp':
    # pasa banda
    frecs = [0.0,         ws1/fs/2,     wp1/fs/2, wp2/fs/2,     ws2/fs/2, 1]
    gains = [-atenuacion,-atenuacion, -ripple, -ripple, -atenuacion, -atenuacion]

else:
    # elimina banda
    frecs = [0.0, 0.3,     0.4,        0.6,         0.7,     1.0]
    gains = [0.0, -ripple, -atenuacion, -atenuacion, -ripple, 0.0]
    
gains = 10**(np.array(gains)/20)
    
fs = 1.0/np.pi

# algunas ventanas para evaluar
#win_name = 'boxcar'
#win_name = 'hamming'
win_name = 'blackmanharris'
#win_name = 'flattop'


# FIR design
num = sig.firwin2(cant_coef, frecs, gains , window=win_name )
den = 1.0


ww, hh = sig.freqz(num, den)
ww = ww / np.pi

plt.figure()

plt.plot(ww, 20 * np.log10(abs(hh)))


plt.plot(frecs, 20*np.log10(gains), 'rx', label='plantilla' )

plt.title('FIR designed by window method')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')

axes_hdl = plt.gca()
axes_hdl.legend()

plt.show()

plt.figure()

plt.plot(ww, np.unwrap(np.angle(hh)) )

plt.title('FIR designed by window method')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Fase [rad]')
plt.grid(which='both', axis='both')
plt.show()
