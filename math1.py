import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(0, 2.5, 0.05)
y1 = np.cos(math.pi * t)
y2 = np.cos(math.pi * t * 2)
plt.plot(t,y1,t,y2)
plt.show()