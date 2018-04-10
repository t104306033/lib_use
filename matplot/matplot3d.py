#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:36:56 2018

@author: wei
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # import 3D module

# create 3D figure
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d') 
ax = Axes3D(fig)

# set X1, X2 array of value
X1 = np.arange(-10, 10, 1)
X2 = np.arange(-10, 10, 1)
X1, X2 = np.meshgrid(X1, X2)    # X1, X2 mesh to grid  
F = 2*X1**2 + X2**2 + X1*X2 + 4*X1 + X2

ax.plot_surface(X1, X2, F, rstride=1, cstride=1, cmap=plt.get_cmap('jet'))
''' colormap色表 
網上很多人愛用 rainbow 
但我個人偏好 jet，因為它明度比較高 
色表可以參考[matplotlib官方文檔](https://matplotlib.org/users/colormaps.html) 
''' 
plt.show()


