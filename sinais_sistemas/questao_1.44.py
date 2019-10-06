import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-0.002, 0.002, 0.0001)
a_values = [500, 750, 1000]
for a in a_values:
    fx = 20*np.sin(2*np.pi*1000*t - np.pi/3) * np.exp(-a*t)
    plt.plot(t, fx)
    plt.show()
