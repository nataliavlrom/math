import matplotlib.pyplot as plt
import numpy as np

# окружность
x1 = []
x2 = []
y1 = []
y2 = []
r = 100

for i in range(r+1):
    x1.append(-i)
    x2.append(i)
    y1.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))

plt.figure(figsize=(5, 5))
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y1)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# эллипс
x1 = []
x2 = []
y1 = []
y2 = []
a = 100
b = 25
for i in range(101):
    x1.append(i)
    x2.append(-i)
    y1.append(np.sqrt(b ** 2 * (1 - (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 * (1 - (i ** 2 / a ** 2))))
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y1)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# гипербола
x1 = []
x2 = []
y1 = []
y2 = []
a = 1000
b = 100
for i in range(1001):
    x1.append(i)
    x2.append(-i)
    y1.append(np.sqrt(b ** 2 * (1 + (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 * (1 + (i ** 2 / a ** 2))))
plt.figure(figsize=(5, 5))
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x2, y1)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
