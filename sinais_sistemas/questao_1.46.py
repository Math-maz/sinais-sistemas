import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift

t = np.arange(-4, 8, 1)
fx = np.heaviside(t, 1)
plt.step(t, fx)
plt.show()
gx = - shift(np.heaviside(t, 1), 6, cval=0)
plt.step(t, gx)
plt.show()
plt.step(t, fx + gx)
plt.show()
