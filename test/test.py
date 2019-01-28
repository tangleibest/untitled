import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

t = np.linspace(0, math.pi, 1000)
x = np.sin(t)
y = np.cos(t) + np.power(x, 2.0 / 3)  # 心型曲线的参数方程

plt.scatter(x, y, c=y, cmap=plt.cm.Reds, edgecolor='none', s=40)
plt.scatter(-x, y, c=y, cmap=plt.cm.Reds, edgecolor='none', s=40)  # 渐变颜色曲线
plt.axis([-2, 2, -2, 2])  # 坐标轴范围
plt.xlabel('love', fontsize=14)
plt.ylabel('you', fontsize=14)
plt.title("I love you", fontsize=30)
plt.show()