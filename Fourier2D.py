import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.fftpack import fft2, ifft2, fftshift
from scipy.linalg import dft
from matplotlib.pyplot import imread
#Lectura imagen tomado de: https://facundoq.github.io/courses/aa2018/res/04_imagenes_numpy.html
imagen = imread("arbol.png")
tamanio = len(imagen[0,:])
#Hallaremos la transformada de Fourier de dicha matriz (La cual es cuadrada)
transformada = fft2(imagen)
nueva = fftshift(transformada)
plt.figure()
plt.imshow(nueva.real,norm = LogNorm())
plt.colorbar()
plt.savefig("CalderonJulian_FT2D.pdf")
plt.close()

#Ahora, haremos el filtro
filtro = np.zeros((tamanio,tamanio))
for i in range(tamanio):
	for j in range(tamanio):
		if(abs(transformada[i,j]) <= 1500.0 or abs(transformada[i,j]) >= 5000.0):
			filtro[i,j] = transformada[i,j]

plt.figure()
plt.imshow(fftshift(filtro), norm = LogNorm())
plt.colorbar()
plt.savefig("CalderonJulian_FT2D_filtrada.pdf")
plt.close()


imagenFiltrada = ifft2(filtro).real
plt.figure()
plt.imshow(imagenFiltrada,plt.cm.gray)
plt.savefig("CalderonJulian_Imagen_filtrada.pdf")


