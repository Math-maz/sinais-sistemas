import numpy as np
import matplotlib.pyplot as plt

F = 0.1
n = np.arange(-0.5*F, 0.5*F, 0.001)
wn = np.cos(2*np.pi * F * n)
plt.plot(n, wn)
# plt.ylim(-, 6)
plt.show()
