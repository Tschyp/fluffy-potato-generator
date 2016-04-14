# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pylab as pl 
from mpl_toolkits.mplot3d import axes3d

pl.rcParams['figure.figsize'] = 10,10 #beállítjuk az ábra méretét

fig = pl.figure()
ax = fig.add_subplot(111,projection='3d')

x = np.sin(np.linspace(0,100,1000))
y = np.cos(np.linspace(0,100,1000))
z = x*y
ax.scatter(x,y,z,c='r',marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pl.show() #és akkor jelenjen meg

