# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:31:58 2016

@author: user
"""

from matplotlib import pyplot as pl
from matplotlib.path import Path
import matplotlib.patches as patches

def vonal(sokszog):
    x,y = [], []
    for a,b in sokszog+[sokszog[0]]:
        x.append(a)
        y.append(b)
    return x,y

sokszog = [(0.,0.), (100.,50.), (150., 60.), (80.,80.), (0.,0.)]
x, y = vonal(sokszog)
pl.plot(x,y, "-")
pl.show()