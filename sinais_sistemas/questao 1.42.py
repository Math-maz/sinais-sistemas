from scipy import signal
import numpy as np


import matplotlib.pyplot as plt
t = np.linspace(0, 6, 1257, endpoint=False)


a = np.arange (-2*np.pi, 2*np.pi, 0.01)
b = 2*np.sin(a)
for n in range(2, 2002, 1):
     b = b - 2.*((-1.)**n/n)*np.sin(n*a)
plt.plot(a, b, 'b-')
plt.show()

amplitude = 5
plt.plot(t, amplitude * signal.square(2 * np.pi * 20 * t, duty=(b+1)/2))
plt.ylim(-6, 6)
plt.show()


plt.figure()
sig = np.sin(2 * np.pi * t)
pwm = signal.square(2 * np.pi * 30 * t, duty=(sig + 1)/2)
plt.subplot(2, 1, 1)
plt.plot(t, sig)
plt.subplot(2, 1, 2)
plt.plot(t, pwm)
plt.ylim(-1.5, 1.5)

plt.show()



a = np.arange (-2*np.pi, 2*np.pi, 0.01)
b = 2*np.sin(a)
for n in range (2,1002,1):
     b = b - 2.*((-1.)**n/n)*np.sin(n*a)

plt.plot (a,b, 'b-')
plt.plot(a, 5*signal.square(2 * np.pi * 5 * a))
plt.ylabel ('f(x)')
plt.grid()
plt.title ('(a)')
plt.show()