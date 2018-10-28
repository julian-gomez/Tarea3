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
	arregloFourier[i] = a.real
#Es necesario usar la parte real de este arreglo.
frecuencias = fftfreq(numeroPuntos,dt)
plt.figure()
plt.plot(frecuencias,abs(arregloFourier), label = "Transformada Fourier")
plt.savefig("CalderonJulian_TF.pdf")
plt.close()
#Con el siguiente codigo se verifica que la transformada es correcta
"""transformada = abs(fft(datosSignal[:,1]).real)
plt.figure()
plt.plot(frecuencias,transformada - abs(arregloFourier), label = "Transformada Fourier")
plt.show()
plt.close()"""

frecuenciasPrincipales = []
for i in range(numeroPuntos):
	if(arregloFourier[i] >= 200.0 and frecuencias[i] >= 0.0):
		frecuenciasPrincipales.append(frecuencias[i])
print "Las frecuencias principales son: ", frecuenciasPrincipales

#Haremos el filtro pasabandas usando como frecuencias de corte 1000 Hz

arregloFiltrado = np.zeros((numeroPuntos))
for i in range(numeroPuntos):
	if(abs(frecuencias[i]) <= 1000.0):
		arregloFiltrado[i] = arregloFourier[i]
#Haremos la transformada inversa
inversa = ifft(arregloFiltrado)
plt.figure()
plt.plot(datosSignal[:,0],inversa.real)
plt.plot(datosSignal[:,0],datosSignal[:,1])
plt.savefig("CalderonJulian_filtrada.pdf")
plt.close()

plt.figure()
plt.plot(datosIncom[:,0],datosIncom[:,1])
plt.show()
fourierInc = fft(datosIncom[:,1])
frec = fftfreq(len(datosIncom[:,1]), datosIncom[1,0] - datosIncom[0,0])















