# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pylab as pl 

tomb = np.linspace(-5,5,30).reshape((5,6))
print(tomb)
print('-'*73)
print (np.mean(tomb,axis=0))

tomb2 = np.arange(50)*0.1

pl.plot(tomb, "D")
pl.show()

pl.plot(tomb2, "rs")
pl.show()

pl.plot(tomb2, tomb2**2)
pl.show()