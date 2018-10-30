import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
from scipy.linalg import dft
from skimage import io
#Lectura imagen tomado de: https://facundoq.github.io/courses/aa2018/res/04_imagenes_numpy.html
imagen = io.imread("arbol.png")/255.0
tamanio = len(imagen[0,:])
#Hallaremos la transformada de Fourier de dicha matriz (La cual es cuadrada)
m = dft(tamanio)
matrizTransformada = m.dot(imagen).real

plt.imshow(matrizTransformada)
plt.colorbar()
plt.show()



