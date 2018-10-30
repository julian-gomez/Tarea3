import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy import interpolate
#Obtenemos los datos de los dos archivos
datosIncom = np.genfromtxt("incompletos.dat", delimiter = ",")
datosSignal = np.genfromtxt("signal.dat", delimiter = ",")

plt.figure()
plt.plot(datosSignal[:,0], datosSignal[:,1], label = "Datos signal")
plt.legend()
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
plt.plot(frecuencias,abs(arregloFourier),label = "Transformada Fourier")
plt.xlim(-2000,2000)
plt.legend()
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
plt.plot(datosSignal[:,0],inversa.real, label = "Senial Filtrada")
plt.legend()
plt.savefig("CalderonJulian_filtrada.pdf")
plt.close()


"""plt.figure()
plt.plot(datosIncom[:,0],datosIncom[:,1])
plt.show()
fourierInc = fft(datosIncom[:,1])
frec = fftfreq(len(datosIncom[:,1]), datosIncom[1,0] - datosIncom[0,0])
plt.plot(frec,abs(fourierInc))
plt.show()"""

print "No es posible realizar Fourier sobre estos datos ya que se tienen pocos tiempos y el dt es amplio, por lo cual se tiene diferencias altas tanto en las frecuencias como en la definicion de la transformada"

interT = np.linspace(min(datosIncom[:,0]),max(datosIncom[:,0]), 512)
cuadratico = interpolate.interp1d(datosIncom[:,0],datosIncom[:,1], "quadratic")(interT)
cubico = interpolate.interp1d(datosIncom[:,0],datosIncom[:,1], "cubic")(interT)
fourierX2 = fft(cuadratico).real
fourierX3 = fft(cubico).real
frec2 = fftfreq(512,interT[1] -interT[0])
plt.figure()
plt.subplot(311)
plt.plot(frecuencias,abs(arregloFourier), label = "Transformada Fourier Signal")
plt.xlim(-2000,2000)
plt.legend()
plt.subplot(312)
plt.plot(frec2, abs(fourierX2), label = "Transformada Fourier Cuadratico")
plt.xlim(-2000,2000)
plt.legend()
plt.subplot(313)
plt.plot(frec2, abs(fourierX3), label = "Transformada Fourier Cubico")
plt.xlim(-2000,2000)
plt.legend()
plt.savefig("CalderonJulian_TF_interpola.pdf")
plt.close()

print "Entre la cuadratica y la original se tiene una diferencia entre los picos. La senial cuadratica alcanza valores menores. Asi mismo, el ruido es mayor en la cuadratica"
print "Lo mismo ocurre entre la cubica y la original (Hay poca diferencia entre cuadratica y cubica)"

#Filtraremos la senial

filtroX2 = np.zeros((512))
filtroX3 = np.zeros((512))

filtroMenorX2 = np.zeros((512))
filtroMenorX3 = np.zeros((512))

for i in range(512):
	if(abs(frec2[i]) <= 1000.0):
		filtroX2[i] = fourierX2[i]
		filtroX3[i] = fourierX3[i]


for i in range(512):
	if(abs(frec2[i]) <= 500.0):
		filtroMenorX2[i] = fourierX2[i]
		filtroMenorX3[i] = fourierX3[i]

arregloFiltrado500 = np.zeros((numeroPuntos))
for i in range(numeroPuntos):
	if(abs(frecuencias[i]) <= 500.0):
		arregloFiltrado500[i] = arregloFourier[i]

inversa500 = ifft(arregloFiltrado500)
inversaX2 = ifft(filtroX2)
inversaX3 = ifft(filtroX3)
inversaMenorX2 = ifft(filtroMenorX2)
inversaMenorX3 = ifft(filtroMenorX3)

plt.figure()
plt.subplot(321)
plt.plot(interT, inversaX2, label = "Filtro cuadratica 1000")
plt.legend()
plt.subplot(323)
plt.plot(interT, inversaX3, label = "Filtro cubica 1000")
plt.legend()
plt.subplot(325)
plt.plot(datosSignal[:,0],inversa.real, label = "Signal Filtrada 1000")
plt.legend()
plt.subplot(322)
plt.plot(interT, inversaMenorX2, label = "Filtro cuadratica 500")
plt.legend()
plt.subplot(324)
plt.plot(interT, inversaMenorX3, label = "Filtro cubica 500")
plt.legend()
plt.subplot(326)
plt.plot(datosSignal[:,0],inversa500.real, label = "Signal Filtrada 500")
plt.legend()
plt.savefig("CalderonJulian_2Filtros.pdf")
plt.close()









