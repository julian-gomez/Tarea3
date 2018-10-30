import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.fftpack import fft2, ifft2, fftshift
from scipy.linalg import dft
from skimage import io
#Lectura imagen tomado de: https://facundoq.github.io/courses/aa2018/res/04_imagenes_numpy.html
imagen = io.imread("arbol.png")/255.0
tamanio = len(imagen[0,:])
#Hallaremos la transformada de Fourier de dicha matriz (La cual es cuadrada)
transformada = fft2(imagen)

nueva = fftshift(transformada)
plt.figure()
plt.imshow(nueva.real)
plt.colorbar()
plt.savefig("CalderonJulian_FT2D.pdf")
plt.close()

#Ahora, haremos el filtro

escalaC = 0.1
escalaF = 0.2
numeroFil = len(nueva[:,0])
numeroCol = len(nueva[0,:])

transformada[int(numeroFil*escalaF):int(numeroFil*(1-escalaF)),:] = 0.0
transformada[:,int(numeroCol*escalaC):int(numeroCol*(1-escalaC))] = 0.0
plt.figure()
plt.imshow(transformada.real, norm = LogNorm(vmin = 5))
plt.colorbar()
plt.savefig("CalderonJulian_FT2D_filtrada.pdf")
plt.close()

imagenFiltrada = ifft2(transformada).real
plt.figure()
plt.imshow(imagenFiltrada,plt.cm.gray)
plt.show()















