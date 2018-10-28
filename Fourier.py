import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
#Obtenemos los datos de los dos archivos
datosIncom = np.genfromtxt("incompletos.dat", delimiter = ",")
datosSignal = np.genfromtxt("signal.dat", delimiter = ",")

plt.figure()
plt.plot(datosSignal[:,0], datosSignal[:,1], label = "Datos signal")
plt.savefig("CalderonJulian_signal.pdf")
plt.close()
dt = datosSignal[1,0] - datosSignal[0,0]
numeroPuntos = len(datosSignal[:,0])

arregloFourier = np.zeros((numeroPuntos))
for i in range(numeroPuntos):
	a = 0.0
	for k in range(numeroPuntos):
		a += datosSignal[k,1]*np.exp(-2.0j*np.pi*k*i/numeroPuntos)
	arregloFourier[i] = abs(a)
#Es necesario usar la parte real de este arreglo.
frecuencias = fftfreq(numeroPuntos,dt)
plt.figure()
plt.plot(frecuencias,arregloFourier, label = "Transformada Fourier")
plt.savefig("CalderonJulian_TF.pdf")
plt.close()
#Con el siguiente codigo se verifica que la transformada es correcta
"""transformada = abs(fft(datosSignal[:,1]))
plt.figure()
plt.plot(frecuencias,transformada - arregloFourier, label = "Transformada Fourier")
plt.show()
plt.close()"""


