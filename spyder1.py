# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Ez is komment
"""

import numpy as np 
from matplotlib import pylab as pl
from mpl_toolkits.mplot3d import axes3d

#beallitjuk az abra meretet
pl.rcParams['figure.figsize'] = 10, 10

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.sin(np.linspace(0, 10, 100))
y = np.cos(np.linspace(0, 10, 100))
z = x*y

ax.scatter(x, y, z, c='g', marker = 'o' )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

pl.show() #es akkor jelenjen meg





