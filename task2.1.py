import matplotlib.pyplot as plt
import numpy as np

# y = k * cos(x - a) + b

x = np.linspace(-2 * np.pi, 3 * np.pi, 301)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(x + np.pi))
plt.plot(x, 0.5 * np.cos(x + np.pi/2) + 0.5)
plt.plot(x, 0.5 * np.cos(x - np.pi/2) - 0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()