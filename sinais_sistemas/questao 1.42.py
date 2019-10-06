from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)
amplitude = 5
frequencia = 20
ciclo_trabalho = 0.6

for ciclo in range(1, 6):
     onda_quadrada = amplitude * signal.square(2 * np.pi * frequencia * t, duty=ciclo/10)
     dente_serra = amplitude * signal.sawtooth(2 * np.pi * frequencia * t, width=ciclo/10)
     fig, axs = plt.subplots(2)
     fig.suptitle('Aproximação de Ondas Periódicas de Tempo Contínuo com Ciclo: ' + str(ciclo/10))
     axs[0].plot(t, onda_quadrada, color='red')
     axs[1].plot(t, dente_serra, color='green')
plt.show()


# plt.figure()
# sig = np.sin(2 * np.pi * t)
# pwm = signal.square(2 * np.pi * 30 * t, duty=(sig + 1)/2)
# plt.subplot(2, 1, 1)
# plt.plot(t, sig)
# plt.subplot(2, 1, 2)
# plt.plot(t, pwm)
# plt.ylim(-1.5, 1.5)
#
# plt.show()
