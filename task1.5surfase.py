import matplotlib.pyplot as plt
import numpy as np

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# параллельные плоскости
fig = figure()
ax = Axes3D(fig)
X = np.arange(-100, 100, 1)
Y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(X, Y)
Z1 = 1 - 2*X - 5*Y
Z2 = 500 - 2*X - 5*Y
ax.plot_surface(X, Y, Z1)
ax.plot_wireframe(X, Y, Z2)
show()

# параболоид
fig = figure()
ax = Axes3D(fig)
X = np.arange(-100, 100, 1)
Y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(X, Y)
Z = X ** 2 + Y ** 2
ax.plot_wireframe(X, Y, Z)
show()

#гиперболоид
fig = figure()
ax = Axes3D(fig)
X = np.arange(-100, 100, 1)
Y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(X, Y)
Z = X ** 2 - Y ** 2
ax.plot_wireframe(X, Y, Z)
show()

# конус
fig = figure()
ax = Axes3D(fig)
X = np.arange(-100, 100, 1)
Y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)
Z1 = - np.sqrt(X ** 2 + Y ** 2)
ax.plot_wireframe(X, Y, Z)
ax.plot_wireframe(X, Y, Z1)
show()