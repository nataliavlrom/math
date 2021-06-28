# 1 Напишите код, который будет переводить полярные координаты в декартовы.
# 2 Напишите код, который будет рисовать график окружности в полярных координатах.
# 3 Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
import matplotlib.pyplot as plt
import numpy as np
import math

# 1
def pol_decart(r,alfa):
    x = r*math.cos(alfa)
    y = r*math.sin(alfa)
    return x, y

print(pol_decart(1,45))


# 2
alfa = np.arange(0, 2, 1/180)*np.pi
plt.polar(alfa, [1]*len(alfa))
plt.show()


#3
a = np.arange(1, 6, 4)
b = np.arange(1, 6, 4)
plt.polar(a, b)
plt.show()
